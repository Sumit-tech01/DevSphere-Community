#!/usr/bin/env python3
"""Read-only verification of the DevSphere Discussions configuration.

Requires an authenticated GitHub CLI session with access to the repository.
No data is modified.

Exit codes:
    0  All automated checks pass. Manual UI checks may still be listed.
    1  Configuration is incomplete or incorrect.
    2  The GitHub query failed.
"""

from __future__ import annotations

import json
import subprocess
import sys
from typing import Any

OWNER = "Sumit-tech01"
NAME = "DevSphere-Community"

EXPECTED_CATEGORIES = [
    ("Announcements", False),
    ("Introductions", False),
    ("General Discussion", False),
    ("Programming", False),
    ("AI & Machine Learning", False),
    ("Web Development", False),
    ("App Development", False),
    ("Project Showcase", False),
    ("Questions & Help", True),
    ("Hackathons & Challenges", False),
    ("Collaboration", False),
    ("Career & Opportunities", False),
]

EXPECTED_SLUGS = {
    "Announcements": "announcements",
    "Introductions": "introductions",
    "General Discussion": "general-discussion",
    "Programming": "programming",
    "AI & Machine Learning": "ai-machine-learning",
    "Web Development": "web-development",
    "App Development": "app-development",
    "Project Showcase": "project-showcase",
    "Questions & Help": "questions-help",
    "Hackathons & Challenges": "hackathons-challenges",
    "Collaboration": "collaboration",
    "Career & Opportunities": "career-opportunities",
}

EXPECTED_DISCUSSIONS = {
    1: "Announcements",
    2: "Introductions",
    3: "Project Showcase",
}

# `emoji` is optional metadata. Request it explicitly, but do not assume the
# API will always return it. Missing emoji data is reported as a manual UI
# check rather than treated as a wrong emoji.
QUERY = f"""
query {{
  repository(owner: "{OWNER}", name: "{NAME}") {{
    discussionCategories(first: 25) {{
      totalCount
      nodes {{ name slug emoji isAnswerable }}
    }}
    discussions(first: 10) {{
      nodes {{ number title category {{ name slug }} }}
    }}
    pinnedDiscussions(first: 10) {{
      nodes {{ discussion {{ number }} }}
    }}
  }}
}}
"""


def as_dict(value: Any) -> dict[str, Any]:
    """Return a dictionary value, or an empty dictionary for null/malformed data."""
    return value if isinstance(value, dict) else {}


def as_list(value: Any) -> list[Any]:
    """Return a list value, or an empty list for null/malformed data."""
    return value if isinstance(value, list) else []


def connection_nodes(value: Any) -> list[dict[str, Any]]:
    """Safely extract nodes from a GraphQL connection."""
    connection = as_dict(value)
    return [node for node in as_list(connection.get("nodes")) if isinstance(node, dict)]


def run_query() -> dict[str, Any]:
    try:
        result = subprocess.run(
            ["gh", "api", "graphql", "-f", f"query={QUERY}"],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError as error:
        print(f"Could not run `gh`: {error}", file=sys.stderr)
        print("Install GitHub CLI and run `gh auth status`.", file=sys.stderr)
        raise SystemExit(2) from error

    if result.returncode != 0:
        print("GitHub query failed.", file=sys.stderr)
        print(result.stderr.strip(), file=sys.stderr)
        print("Run `gh auth status` and confirm repository access.", file=sys.stderr)
        raise SystemExit(2)

    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as error:
        print(f"Could not parse GitHub response: {error}", file=sys.stderr)
        raise SystemExit(2) from error

    if not isinstance(payload, dict):
        print("GitHub returned an unexpected response shape.", file=sys.stderr)
        raise SystemExit(2)

    errors = payload.get("errors")
    if errors:
        print("GitHub returned errors:", file=sys.stderr)
        for error in as_list(errors):
            if isinstance(error, dict):
                print(f"- {error.get('message', error)}", file=sys.stderr)
            else:
                print(f"- {error}", file=sys.stderr)
        raise SystemExit(2)

    data = as_dict(payload.get("data"))
    repository = data.get("repository")
    if not isinstance(repository, dict):
        print("GitHub response did not include repository data.", file=sys.stderr)
        raise SystemExit(2)
    return repository


def main() -> int:
    repository = run_query()
    category_connection = as_dict(repository.get("discussionCategories"))
    categories = connection_nodes(category_connection)
    discussions = connection_nodes(repository.get("discussions"))
    pinned_nodes = connection_nodes(repository.get("pinnedDiscussions"))

    expected = dict(EXPECTED_CATEGORIES)
    failures: list[str] = []
    warnings: list[str] = []
    manual_checks: list[str] = []
    by_name: dict[str, dict[str, Any]] = {}
    category_names: list[str] = []

    for category in categories:
        raw_name = category.get("name")
        if not isinstance(raw_name, str) or not raw_name.strip():
            failures.append("Category entry is missing a usable name")
            continue
        category_names.append(raw_name)
        if raw_name in by_name:
            failures.append(f"Duplicate category name: {raw_name}")
            continue
        by_name[raw_name] = category

    print("DevSphere Discussions verification")
    print("==================================")
    print(f"Repository: {OWNER}/{NAME}")
    print(f"Categories: {len(categories)}/12")
    print()

    prefixed_names: set[str] = set()

    for name, expected_answerable in EXPECTED_CATEGORIES:
        if name in by_name:
            category = by_name.get(name, {})
            slug = category.get("slug")
            category_label = f"{name} [{slug}]" if isinstance(slug, str) and slug else name
            answerable = category.get("isAnswerable")

            if not isinstance(answerable, bool):
                print(f"  [!] {category_label}: format unavailable (isAnswerable missing or null)")
                print("      Confirm the category format in the GitHub web interface.")
                failures.append(f"Could not verify format for category: {name}")
                manual_checks.append(
                    f"{name}: confirm the category format in the GitHub UI because "
                    "the API did not return isAnswerable."
                )
            elif answerable != expected_answerable:
                print(f"  [!] {category_label}: wrong format (isAnswerable={answerable})")
                failures.append(f"Wrong format for category: {name}")
            else:
                print(f"  [x] {category_label}")

            if name == "Introductions":
                emoji = category.get("emoji")
                if not isinstance(emoji, str) or not emoji:
                    print("      [ ] Introductions: emoji metadata unavailable — confirm 👋 visually")
                elif emoji == ":hash:":
                    print("      [!] Introductions: uses the # emoji; choose 👋 in the emoji picker")
                    failures.append("Introductions uses the wrong emoji")

            expected_slug = EXPECTED_SLUGS.get(name)
            if not isinstance(slug, str) or not slug:
                warnings.append(f"Slug not returned for category: {name}")
                manual_checks.append(f"{name}: confirm the category URL in the GitHub UI.")
            elif expected_slug and slug != expected_slug:
                warnings.append(
                    f"Unexpected slug for {name}: {slug!r} (expected {expected_slug!r})"
                )
                manual_checks.append(
                    f"{name}: confirm the category link uses the expected slug {expected_slug!r}."
                )
            continue

        candidate = next(
            (
                actual_name
                for actual_name in category_names
                if actual_name != name and name in actual_name
            ),
            None,
        )
        candidate_by_slug = next(
            (
                actual_name
                for actual_name, category in by_name.items()
                if category.get("slug") == EXPECTED_SLUGS.get(name)
            ),
            None,
        )

        if candidate is not None:
            prefixed_names.add(candidate)
            candidate_slug = by_name.get(candidate, {}).get("slug")
            print(
                f"  [!] {name}: name includes extra text or an emoji "
                f"({candidate!r}, slug={candidate_slug!r})"
            )
            print(f"      Set the Name field to {name!r} and choose the emoji separately.")
            failures.append(f"Category name includes extra text or an emoji: {candidate}")
        elif candidate_by_slug is not None:
            prefixed_names.add(candidate_by_slug)
            print(
                f"  [!] {name}: slug matches but the returned name is "
                f"{candidate_by_slug!r}"
            )
            failures.append(f"Category name does not match expected name: {candidate_by_slug}")
        else:
            print(f"  [ ] {name}: missing")
            failures.append(f"Missing category: {name}")

    unexpected = [
        name for name in category_names if name not in expected and name not in prefixed_names
    ]

    if unexpected:
        print()
        print("Unexpected categories:")
        for name in unexpected:
            print(f"  - {name}")
        failures.append("Unexpected categories present: " + ", ".join(unexpected))

    if len(categories) != 12:
        failures.append(f"Expected 12 categories, found {len(categories)}")

    declared_count = category_connection.get("totalCount")
    if isinstance(declared_count, int) and declared_count != len(categories):
        warnings.append(
            f"Category totalCount ({declared_count}) does not match returned nodes "
            f"({len(categories)})."
        )

    missing_emoji: list[str] = []
    for name in expected:
        category = by_name.get(name)
        if category is None:
            continue
        emoji = category.get("emoji")
        if not isinstance(emoji, str) or not emoji:
            missing_emoji.append(name)
    if missing_emoji:
        print()
        print("Emoji metadata unavailable:")
        for name in missing_emoji:
            print(
                f"  [ ] {name}: emoji field missing or null — confirm visually"
            )
        warnings.append("Emoji metadata unavailable for: " + ", ".join(missing_emoji))
        manual_checks.append(
            "Emoji display: confirm the intended emoji is selected separately for: "
            + ", ".join(missing_emoji)
            + "."
        )
    elif category_names:
        print()
        print(f"Emoji metadata returned for {len(category_names)}/{len(category_names)} categories.")

    # The API returns categories alphabetically, not in sidebar order. Verify
    # sidebar order in the GitHub interface instead of guessing from this list.

    print()
    print("Discussions:")
    by_number: dict[int, dict[str, Any]] = {}
    for discussion in discussions:
        number = discussion.get("number")
        if not isinstance(number, int):
            failures.append("Discussion entry is missing a usable number")
            continue
        if number in by_number:
            warnings.append(f"Duplicate discussion number in response: {number}")
            continue
        by_number[number] = discussion

    for number, expected_category in EXPECTED_DISCUSSIONS.items():
        discussion = by_number.get(number)
        if discussion is None:
            print(f"  [ ] #{number}: not found")
            failures.append(f"Discussion #{number} not found")
            continue
        title = discussion.get("title")
        if not isinstance(title, str) or not title:
            title = "(untitled)"
        discussion_category = as_dict(discussion.get("category"))
        category_name = discussion_category.get("name")
        category_slug = discussion_category.get("slug")
        category_label = (
            f"{category_name} [{category_slug}]"
            if isinstance(category_slug, str) and category_slug
            else str(category_name)
        )
        if not isinstance(category_name, str) or not category_name:
            print(f"  [ ] #{number} {title} -> category unavailable")
            failures.append(f"Discussion #{number} has no readable category")
        elif category_name == expected_category:
            print(f"  [x] #{number} {title} -> {category_label}")
        elif category_name.endswith(f" {expected_category}"):
            print(
                f"  [x] #{number} {title} -> {category_label} "
                "(category name needs cleanup)"
            )
            warnings.append(
                f"Discussion #{number} category name needs cleanup: {category_name!r}"
            )
        else:
            print(
                f"  [ ] #{number} {title} -> {category_label} "
                f"(expected {expected_category})"
            )
            failures.append(
                f"Discussion #{number} is in {category_name}, expected {expected_category}"
            )

    print()
    print("Pinned discussions:")
    pinned: set[int] = set()
    for node in pinned_nodes:
        discussion = as_dict(node.get("discussion"))
        number = discussion.get("number")
        if isinstance(number, int):
            pinned.add(number)
        else:
            warnings.append("Pinned discussion entry is missing a usable number")

    for number in EXPECTED_DISCUSSIONS:
        if number in pinned:
            print(f"  [x] #{number}")
        else:
            print(f"  [ ] #{number}: not pinned")
            failures.append(f"Discussion #{number} is not pinned")

    # GitHub's GraphQL API does not expose the Announcement format flag, so it
    # cannot be verified programmatically.
    manual_checks.append(
        "Announcements: confirm in the GitHub UI that the format is Announcement "
        "and that only maintainers can start discussions. The API does not expose "
        "this format flag."
    )

    if failures:
        print()
        print("Failures:")
        for failure in failures:
            print(f"  - {failure}")

    if warnings:
        print()
        print("Warnings:")
        for warning in warnings:
            print(f"  - {warning}")

    if manual_checks:
        print()
        print("Manual UI checks:")
        for check in manual_checks:
            print(f"  - {check}")

    print()
    if failures:
        print(f"Result: NOT READY — {len(failures)} check(s) need attention.")
        return 1

    if manual_checks:
        check_label = "check" if len(manual_checks) == 1 else "checks"
        remain_label = "remains" if len(manual_checks) == 1 else "remain"
        print(
            "Result: AUTOMATED CHECKS PASS — "
            f"{len(manual_checks)} manual UI {check_label} {remain_label}."
        )
        return 0

    print("Result: READY — all required Discussions checks pass.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
