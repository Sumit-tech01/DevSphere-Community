#!/usr/bin/env python3
"""Read-only verification of the DevSphere Discussions configuration.

Requires an authenticated GitHub CLI session with access to the repository.
No data is modified.

Exit codes:
    0  All required checks pass.
    1  Configuration is incomplete or incorrect.
    2  The GitHub query failed.
"""

from __future__ import annotations

import json
import subprocess
import sys

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

EXPECTED_DISCUSSIONS = {
    1: "Announcements",
    2: "Introductions",
    3: "Project Showcase",
}

QUERY = f"""
query {{
  repository(owner: "{OWNER}", name: "{NAME}") {{
    discussionCategories(first: 25) {{
      totalCount
      nodes {{ name isAnswerable }}
    }}
    discussions(first: 10) {{
      nodes {{ number title category {{ name }} }}
    }}
    pinnedDiscussions(first: 10) {{
      nodes {{ discussion {{ number }} }}
    }}
  }}
}}
"""


def run_query() -> dict:
    result = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={QUERY}"],
        capture_output=True,
        text=True,
        check=False,
    )
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

    if "errors" in payload:
        print("GitHub returned errors:", file=sys.stderr)
        for error in payload["errors"]:
            print(f"- {error.get('message', error)}", file=sys.stderr)
        raise SystemExit(2)

    return payload["data"]["repository"]


def main() -> int:
    repo = run_query()
    categories = repo["discussionCategories"]["nodes"]
    discussions = repo["discussions"]["nodes"]
    pinned = {node["discussion"]["number"] for node in repo["pinnedDiscussions"]["nodes"]}

    actual = {category["name"]: category["isAnswerable"] for category in categories}
    by_name = {category["name"]: category for category in categories}
    expected = dict(EXPECTED_CATEGORIES)
    failures: list[str] = []
    warnings: list[str] = []
    prefixed_names = {
        name
        for name in actual
        for expected_name in expected
        if name != expected_name and name.endswith(expected_name)
    }

    print("DevSphere Discussions verification")
    print("==================================")
    print(f"Repository: {OWNER}/{NAME}")
    print(f"Categories: {len(categories)}/12")
    print()

    for name, _ in EXPECTED_CATEGORIES:
        if name in actual:
            if actual[name] != expected[name]:
                print(f"  [!] {name}: wrong format (isAnswerable={actual[name]})")
                failures.append(f"Wrong format for category: {name}")
            elif name == "Introductions" and by_name[name]["emoji"] == ":hash:":
                print("  [!] Introductions: uses the # emoji; choose 👋 in the emoji picker")
                failures.append("Introductions uses the wrong emoji")
            else:
                print(f"  [x] {name}")
            continue

        prefixed = next(
            (candidate for candidate in actual if candidate != name and candidate.endswith(name)),
            None,
        )
        if prefixed is not None:
            print(f"  [!] {name}: name includes an emoji ({prefixed!r})")
            print(f"      Set the Name field to {name!r} and choose the emoji separately.")
            failures.append(f"Category name includes an emoji: {prefixed}")
        else:
            print(f"  [ ] {name}: missing")
            failures.append(f"Missing category: {name}")

    unexpected = [name for name in actual if name not in expected and name not in prefixed_names]

    if unexpected:
        print()
        print("Unexpected categories:")
        for name in unexpected:
            print(f"  - {name}")
        failures.append("Unexpected categories present: " + ", ".join(unexpected))

    if len(categories) != 12:
        failures.append(f"Expected 12 categories, found {len(categories)}")

    # The API returns categories alphabetically, not in sidebar order. Verify
    # sidebar order in the GitHub interface instead of guessing from this list.

    print()
    print("Discussions:")
    by_number = {discussion["number"]: discussion for discussion in discussions}
    for number, expected_category in EXPECTED_DISCUSSIONS.items():
        discussion = by_number.get(number)
        if discussion is None:
            print(f"  [ ] #{number}: not found")
            failures.append(f"Discussion #{number} not found")
            continue
        category = discussion["category"]["name"]
        if category == expected_category:
            print(f"  [x] #{number} {discussion['title']} -> {category}")
        elif category.endswith(expected_category):
            print(f"  [x] #{number} {discussion['title']} -> {category} (category name needs cleanup)")
        else:
            print(f"  [ ] #{number} {discussion['title']} -> {category} (expected {expected_category})")
            failures.append(f"Discussion #{number} is in {category}, expected {expected_category}")

    print()
    print("Pinned discussions:")
    for number in (1, 2, 3):
        if number in pinned:
            print(f"  [x] #{number}")
        else:
            print(f"  [ ] #{number}: not pinned")
            failures.append(f"Discussion #{number} is not pinned")

    if warnings:
        print()
        print("Warnings:")
        for warning in warnings:
            print(f"  - {warning}")

    print()
    if failures:
        print(f"Result: NOT READY — {len(failures)} check(s) need attention.")
        return 1

    print("Result: READY — all required Discussions checks pass.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
