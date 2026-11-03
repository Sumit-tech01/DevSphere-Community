#!/usr/bin/env python3
"""Validate the DevSphere community repository.

Checks:
- Required files and directory structure.
- Markdown internal links and same-document anchors.
- Duplicate file content.
- SVG well-formedness and accessibility metadata.
- PNG signatures.
- JSON and YAML syntax (when PyYAML is available).
- Issue template metadata and label consistency.
- Discussion post count, metadata, and duplicate titles.
- Placeholder markers and missing trailing newlines.

Run from the repository root:
    python3 scripts/validate_repository.py
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent

errors: list[str] = []
warnings: list[str] = []

REQUIRED_FILES = [
    "README.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "LICENSE",
    "CHANGELOG.md",
    ".gitignore",
    ".markdownlint.json",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/ISSUE_TEMPLATE/project_showcase.md",
    ".github/ISSUE_TEMPLATE/general_contribution.md",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/workflows/markdown-validation.yml",
    "assets/branding/README.md",
    "assets/branding/logo.svg",
    "assets/branding/logo-mark.svg",
    "assets/branding/banner.svg",
    "assets/branding/social-preview.svg",
    "assets/branding/favicon.svg",
    "assets/branding/logo.png",
    "assets/branding/logo-mark.png",
    "assets/branding/banner.png",
    "assets/branding/social-preview.png",
    "assets/branding/favicon.png",
    "community/COMMUNITY_GUIDELINES.md",
    "community/DISCUSSION_GUIDE.md",
    "community/DISCUSSION_SETUP.md",
    "community/MODERATION_POLICY.md",
    "community/MEMBER_ROLES.md",
    "community/COMMUNITY_ROADMAP.md",
    "community/discussions/README.md",
    "resources/README.md",
    "resources/programming.md",
    "resources/artificial-intelligence.md",
    "resources/web-development.md",
    "resources/open-source.md",
    "challenges/README.md",
    "challenges/CHALLENGE_TEMPLATE.md",
    "challenges/challenge-001.md",
    "scripts/validate_repository.py",
]

EXPECTED_DISCUSSION_POSTS = 12

KNOWN_LABELS = {
    "announcement",
    "launch",
    "welcome",
    "introduction",
    "showcase",
    "feedback",
    "collaboration",
    "ai-ml",
    "web-development",
    "challenge",
    "challenge-001",
    "hackathon",
    "career",
    "opportunities",
    "open-source",
    "community",
    "question",
    "resource",
    "discussion",
    "good first issue",
    "help wanted",
    "bug",
    "enhancement",
    "documentation",
    "needs-triage",
}

EXTERNAL_PREFIXES = (
    "http://",
    "https://",
    "mailto:",
    "tel:",
    "ftp://",
    "data:",
)

FENCED_CODE_RE = re.compile(
    r"(?ms)^[ \t]*(`{3,}|~{3,})[^\n]*\n.*?^[ \t]*\1[ \t]*$"
)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
HTML_COMMENT_RE = re.compile(r"(?s)<!--.*?-->")
LINK_RE = re.compile(
    r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)"
)
MD_HEADING_RE = re.compile(r"(?m)^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
HTML_HEADING_RE = re.compile(r"(?is)<h([1-6])[^>]*>(.*?)</h\1>")
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b|Lorem ipsum", re.IGNORECASE)


def add_error(message: str) -> None:
    errors.append(message)


def add_warning(message: str) -> None:
    warnings.append(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_code_and_comments(text: str) -> str:
    text = FENCED_CODE_RE.sub("", text)
    text = INLINE_CODE_RE.sub("", text)
    return HTML_COMMENT_RE.sub("", text)


def clean_heading_text(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[*_~]", "", text)
    return unquote(text).strip()


def slugify(text: str) -> str:
    text = clean_heading_text(text).lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s", "-", text)
    return text


def collect_anchors(text: str) -> set[str]:
    clean = strip_code_and_comments(text)
    headings: list[tuple[int, str]] = []

    for match in MD_HEADING_RE.finditer(clean):
        headings.append((match.start(), match.group(2)))

    for match in HTML_HEADING_RE.finditer(clean):
        headings.append((match.start(), match.group(2)))

    headings.sort(key=lambda item: item[0])

    anchors: set[str] = set()
    counts: dict[str, int] = {}

    for _, raw in headings:
        base = slugify(raw)
        if not base:
            continue
        index = counts.get(base, 0)
        slug = base if index == 0 else f"{base}-{index}"
        counts[base] = index + 1
        anchors.add(slug)

    return anchors


def check_links(path: Path, text: str, anchor_cache: dict[Path, set[str]]) -> None:
    clean = strip_code_and_comments(text)
    relative_path = path.relative_to(ROOT)

    for match in LINK_RE.finditer(clean):
        destination = match.group(1).strip()
        if not destination:
            continue

        if destination.startswith("<") and destination.endswith(">"):
            destination = destination[1:-1].strip()

        if destination.startswith(EXTERNAL_PREFIXES):
            continue

        if destination.startswith("#"):
            anchor = unquote(destination[1:])
            if anchor and anchor not in anchor_cache[path]:
                add_error(
                    f"{relative_path}: missing anchor '#{anchor}' in the same file"
                )
            continue

        target_part, _, anchor = destination.partition("#")
        target_part = target_part.split("?", 1)[0]
        target_part = unquote(target_part)

        if not target_part:
            continue

        if target_part.startswith("/"):
            target = (ROOT / target_part.lstrip("/")).resolve()
        else:
            target = (path.parent / target_part).resolve()

        try:
            target.relative_to(ROOT)
        except ValueError:
            add_warning(
                f"{relative_path}: link points outside the repository: {destination}"
            )
            continue

        if not target.exists():
            add_error(f"{relative_path}: missing link target '{destination}'")
            continue

        if anchor and target.suffix.lower() == ".md":
            if target not in anchor_cache:
                anchor_cache[target] = collect_anchors(read_text(target))
            if unquote(anchor) not in anchor_cache[target]:
                add_error(
                    f"{relative_path}: missing anchor '#{anchor}' in "
                    f"{target.relative_to(ROOT)}"
                )


def check_discussion_posts() -> None:
    posts = sorted(
        p
        for p in (ROOT / "community" / "discussions").glob("*.md")
        if p.name != "README.md" and re.match(r"^\d{2}-", p.name)
    )

    if len(posts) != EXPECTED_DISCUSSION_POSTS:
        add_error(
            "community/discussions: expected "
            f"{EXPECTED_DISCUSSION_POSTS} posts, found {len(posts)}"
        )

    titles: dict[str, Path] = {}
    required_metadata = ("Title:", "Category:", "Format:", "Labels:")

    for post in posts:
        text = read_text(post)
        metadata_match = re.search(r"(?s)<!--(.*?)-->", text)
        if not metadata_match:
            add_error(f"{post.relative_to(ROOT)}: missing hidden metadata comment")
            continue

        metadata = metadata_match.group(1)
        for field in required_metadata:
            if field not in metadata:
                add_error(
                    f"{post.relative_to(ROOT)}: metadata is missing '{field}'"
                )

        title_match = re.search(r"^Title:\s*(.+)$", metadata, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()
            if title in titles:
                add_error(
                    "duplicate discussion title: "
                    f"'{title}' in {post.name} and {titles[title].name}"
                )
            titles[title] = post

            first_heading = re.search(r"(?m)^#\s+(.+)$", text)
            if first_heading and first_heading.group(1).strip() != title:
                add_warning(
                    f"{post.relative_to(ROOT)}: H1 does not match the "
                    "metadata title exactly"
                )

        labels_match = re.search(r"^Labels:\s*(.+)$", metadata, re.MULTILINE)
        if labels_match:
            for label in [item.strip() for item in labels_match.group(1).split(",")]:
                if label and label not in KNOWN_LABELS:
                    add_error(
                        f"{post.relative_to(ROOT)}: unknown label '{label}'"
                    )


def check_issue_templates() -> None:
    template_dir = ROOT / ".github" / "ISSUE_TEMPLATE"
    for template in sorted(template_dir.glob("*.md")):
        text = read_text(template)
        if not text.startswith("---"):
            add_error(f"{template.relative_to(ROOT)}: missing YAML front matter")
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            add_error(f"{template.relative_to(ROOT)}: malformed front matter")
            continue

        try:
            import yaml  # type: ignore
        except ImportError:
            continue

        try:
            data = yaml.safe_load(parts[1]) or {}
        except Exception as exc:  # noqa: BLE001 - report parser message
            add_error(f"{template.relative_to(ROOT)}: invalid YAML: {exc}")
            continue

        for key in ("name", "about", "title", "labels"):
            if key not in data:
                add_error(
                    f"{template.relative_to(ROOT)}: front matter missing '{key}'"
                )

        raw_labels = data.get("labels", "")
        if isinstance(raw_labels, str):
            labels = [label.strip() for label in raw_labels.split(",") if label.strip()]
        elif isinstance(raw_labels, list):
            labels = [str(label).strip() for label in raw_labels]
        else:
            labels = []

        for label in labels:
            if label not in KNOWN_LABELS:
                add_error(
                    f"{template.relative_to(ROOT)}: label '{label}' is not in "
                    "the documented label set"
                )


def check_svgs() -> None:
    for svg in sorted((ROOT / "assets" / "branding").glob("*.svg")):
        try:
            tree = ET.parse(svg)
        except ET.ParseError as exc:
            add_error(f"{svg.relative_to(ROOT)}: invalid XML: {exc}")
            continue

        root = tree.getroot()
        if not root.tag.endswith("svg"):
            add_error(f"{svg.relative_to(ROOT)}: root element is not <svg>")
        if not root.get("viewBox"):
            add_error(f"{svg.relative_to(ROOT)}: missing viewBox")
        if not root.get("role"):
            add_warning(f"{svg.relative_to(ROOT)}: missing role attribute")
        if root.find(".//{http://www.w3.org/2000/svg}title") is None:
            add_warning(f"{svg.relative_to(ROOT)}: missing <title> element")


def check_pngs() -> None:
    for png in sorted((ROOT / "assets" / "branding").glob("*.png")):
        signature = png.read_bytes()[:8]
        if signature != b"\x89PNG\r\n\x1a\n":
            add_error(f"{png.relative_to(ROOT)}: not a valid PNG file")


def check_yaml_and_json() -> None:
    try:
        import yaml  # type: ignore
    except ImportError:
        add_warning(
            "PyYAML is not installed; workflow YAML syntax was not validated"
        )
        yaml = None

    if yaml is not None:
        for yaml_file in sorted((ROOT / ".github").rglob("*.yml")):
            try:
                yaml.safe_load(read_text(yaml_file))
            except Exception as exc:  # noqa: BLE001 - report parser message
                add_error(f"{yaml_file.relative_to(ROOT)}: invalid YAML: {exc}")

    for workflow in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
        text = read_text(workflow)
        if "pull_request_target" in text:
            add_error(
                f"{workflow.relative_to(ROOT)}: pull_request_target is not allowed"
            )
        if re.search(r"\bsecrets\.", text):
            add_error(
                f"{workflow.relative_to(ROOT)}: secrets must not be used in "
                "this community repository"
            )
        if "permissions:" not in text:
            add_error(f"{workflow.relative_to(ROOT)}: missing permissions block")
        if "contents: write" in text:
            add_error(
                f"{workflow.relative_to(ROOT)}: contents: write is not allowed"
            )

    try:
        json.loads(read_text(ROOT / ".markdownlint.json"))
    except json.JSONDecodeError as exc:
        add_error(f".markdownlint.json: invalid JSON: {exc}")


def check_content_quality(markdown_files: list[Path]) -> None:
    for path in markdown_files:
        text = read_text(path)
        relative = path.relative_to(ROOT)

        if not text.strip():
            add_error(f"{relative}: file is empty")
            continue

        if not text.endswith("\n"):
            add_error(f"{relative}: file does not end with a newline")

        for match in PLACEHOLDER_RE.finditer(text):
            line = text[: match.start()].count("\n") + 1
            add_error(
                f"{relative}:{line}: placeholder marker "
                f"'{match.group(0)}' found"
            )


def check_duplicates(files: list[Path]) -> None:
    hashes: dict[str, Path] = {}
    for path in files:
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest in hashes:
            add_error(
                "duplicate file content: "
                f"{path.relative_to(ROOT)} and {hashes[digest].relative_to(ROOT)}"
            )
        else:
            hashes[digest] = path


def main() -> int:
    print("DevSphere repository validation")
    print("=" * 34)

    for required in REQUIRED_FILES:
        if not (ROOT / required).exists():
            add_error(f"missing required file: {required}")

    markdown_files = sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts and "node_modules" not in path.parts
    )

    anchor_cache: dict[Path, set[str]] = {}
    for path in markdown_files:
        anchor_cache[path] = collect_anchors(read_text(path))

    for path in markdown_files:
        check_links(path, read_text(path), anchor_cache)

    check_discussion_posts()
    check_issue_templates()
    check_svgs()
    check_pngs()
    check_yaml_and_json()
    check_content_quality(markdown_files)
    check_duplicates(markdown_files)

    external_links = 0
    for path in markdown_files:
        clean = strip_code_and_comments(read_text(path))
        for match in LINK_RE.finditer(clean):
            if match.group(1).strip().startswith(("http://", "https://")):
                external_links += 1

    print(f"Markdown files checked: {len(markdown_files)}")
    print(f"External links found:   {external_links}")
    print(f"Warnings:               {len(warnings)}")
    print(f"Errors:                 {len(errors)}")

    if warnings:
        print("\nWarnings")
        for warning in warnings:
            print(f"  - {warning}")

    if errors:
        print("\nErrors")
        for error in errors:
            print(f"  - {error}")
        print("\nValidation failed.")
        return 1

    print("\nValidation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
