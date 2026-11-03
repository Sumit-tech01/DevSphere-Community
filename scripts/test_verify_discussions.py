#!/usr/bin/env python3
"""Unit tests for the Discussions verifier's API compatibility handling.

Run from the repository root:
    python3 -m unittest discover -s scripts -p 'test_*.py'
"""

from __future__ import annotations

import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))

import verify_discussions as verifier  # noqa: E402

OMIT = object()


class VerifierTests(unittest.TestCase):
    def make_repository(
        self,
        *,
        emoji: object = ":wave:",
        omit_emoji: tuple[str, ...] = (),
        null_emoji: tuple[str, ...] = (),
        category_overrides: dict[str, dict[str, object]] | None = None,
        extra_categories: list[dict[str, object]] | None = None,
        drop_categories: tuple[str, ...] = (),
        pinned: tuple[int, ...] = (1, 2, 3),
        discussion_overrides: dict[int, dict[str, object]] | None = None,
    ) -> dict[str, object]:
        overrides = category_overrides or {}
        categories: list[dict[str, object]] = []

        for name, answerable in verifier.EXPECTED_CATEGORIES:
            if name in drop_categories:
                continue
            category: dict[str, object] = {
                "name": name,
                "slug": verifier.EXPECTED_SLUGS[name],
                "isAnswerable": answerable,
            }
            if name in omit_emoji:
                pass
            elif name in null_emoji:
                category["emoji"] = None
            elif emoji is not OMIT:
                category["emoji"] = emoji
            category.update(overrides.get(name, {}))
            categories.append(category)

        categories.extend(extra_categories or [])

        discussions: list[dict[str, object]] = []
        for number, expected_category in verifier.EXPECTED_DISCUSSIONS.items():
            discussion: dict[str, object] = {
                "number": number,
                "title": f"Discussion {number}",
                "category": {
                    "name": expected_category,
                    "slug": verifier.EXPECTED_SLUGS[expected_category],
                },
            }
            discussion.update((discussion_overrides or {}).get(number, {}))
            discussions.append(discussion)

        return {
            "discussionCategories": {
                "totalCount": len(categories),
                "nodes": categories,
            },
            "discussions": {"nodes": discussions},
            "pinnedDiscussions": {
                "nodes": [{"discussion": {"number": number}} for number in pinned]
            },
        }

    def run_main(self, repository: dict[str, object]) -> tuple[int, str]:
        output = io.StringIO()
        with patch.object(verifier, "run_query", return_value=repository):
            with redirect_stdout(output):
                code = verifier.main()
        return code, output.getvalue()

    def test_clean_configuration_passes_with_manual_announcement_check(self) -> None:
        code, output = self.run_main(self.make_repository())

        self.assertEqual(0, code)
        self.assertIn("AUTOMATED CHECKS PASS", output)
        self.assertIn("Emoji metadata returned for 12/12 categories", output)
        self.assertIn("Announcements: confirm in the GitHub UI", output)

    def test_missing_emoji_is_manual_not_a_failure(self) -> None:
        code, output = self.run_main(self.make_repository(omit_emoji=("Introductions",)))

        self.assertEqual(0, code)
        self.assertIn("emoji metadata unavailable", output)
        self.assertIn("Emoji metadata unavailable for: Introductions", output)
        self.assertNotIn("Introductions uses the wrong emoji", output)
        self.assertIn("confirm the intended emoji", output)

    def test_null_emoji_is_manual_not_a_failure(self) -> None:
        code, output = self.run_main(self.make_repository(null_emoji=("Introductions",)))

        self.assertEqual(0, code)
        self.assertIn("Emoji metadata unavailable for: Introductions", output)
        self.assertNotIn("Introductions uses the wrong emoji", output)

    def test_all_emoji_missing_does_not_crash(self) -> None:
        code, output = self.run_main(self.make_repository(emoji=OMIT))

        self.assertEqual(0, code)
        self.assertIn("Emoji metadata unavailable:", output)
        self.assertIn("AUTOMATED CHECKS PASS", output)

    def test_missing_slug_is_a_warning_not_a_crash(self) -> None:
        code, output = self.run_main(
            self.make_repository(
                category_overrides={"Introductions": {"slug": None}},
            )
        )

        self.assertEqual(0, code)
        self.assertIn("Slug not returned for category: Introductions", output)
        self.assertIn("confirm the category URL", output)

    def test_wrong_introductions_emoji_still_fails(self) -> None:
        code, output = self.run_main(self.make_repository(emoji=":hash:"))

        self.assertEqual(1, code)
        self.assertIn("Introductions: uses the # emoji", output)

    def test_embedded_emoji_in_name_fails(self) -> None:
        code, output = self.run_main(
            self.make_repository(
                category_overrides={
                    "Introductions": {
                        "name": "👋 Introductions",
                        "slug": "-introductions",
                    }
                }
            )
        )

        self.assertEqual(1, code)
        self.assertIn("name includes extra text or an emoji", output)
        self.assertIn("Category name includes extra text or an emoji", output)

    def test_wrong_qa_format_fails(self) -> None:
        code, output = self.run_main(
            self.make_repository(
                category_overrides={"Questions & Help": {"isAnswerable": False}}
            )
        )

        self.assertEqual(1, code)
        self.assertIn("Wrong format for category: Questions & Help", output)

    def test_missing_answerable_field_is_not_ready(self) -> None:
        code, output = self.run_main(
            self.make_repository(
                category_overrides={"Questions & Help": {"isAnswerable": None}}
            )
        )

        self.assertEqual(1, code)
        self.assertIn("format unavailable (isAnswerable missing or null)", output)
        self.assertIn("confirm the category format", output)

    def test_wrong_category_count_fails(self) -> None:
        code, output = self.run_main(
            self.make_repository(drop_categories=("Collaboration",))
        )

        self.assertEqual(1, code)
        self.assertIn("Expected 12 categories, found 11", output)

    def test_unexpected_legacy_category_fails(self) -> None:
        code, output = self.run_main(
            self.make_repository(
                extra_categories=[
                    {
                        "name": "Ideas",
                        "slug": "ideas",
                        "emoji": ":bulb:",
                        "isAnswerable": False,
                    }
                ]
            )
        )

        self.assertEqual(1, code)
        self.assertIn("Unexpected categories present: Ideas", output)

    def test_wrong_discussion_assignment_fails(self) -> None:
        code, output = self.run_main(
            self.make_repository(
                discussion_overrides={
                    2: {
                        "category": {
                            "name": "General Discussion",
                            "slug": "general-discussion",
                        }
                    }
                }
            )
        )

        self.assertEqual(1, code)
        self.assertIn(
            "Discussion #2 is in General Discussion, expected Introductions", output
        )

    def test_unpinned_discussion_fails(self) -> None:
        code, output = self.run_main(self.make_repository(pinned=(1, 2)))

        self.assertEqual(1, code)
        self.assertIn("Discussion #3 is not pinned", output)

    def test_malformed_discussion_category_does_not_crash(self) -> None:
        code, output = self.run_main(
            self.make_repository(discussion_overrides={2: {"category": None}})
        )

        self.assertEqual(1, code)
        self.assertIn("Discussion #2 has no readable category", output)


if __name__ == "__main__":
    unittest.main()
