# DevSphere Discussions Setup Guide

This is the administrative reference for DevSphere's GitHub Discussions. It records the verified live configuration, the checks that remain manual, and the procedure for maintaining the category structure over time.

> **Live status verified 3 November 2026:**
>
> - Discussions are **enabled** for `Sumit-tech01/DevSphere-Community`.
> - **Exactly 12 categories exist** with clean names and stable slugs.
> - Emoji metadata is returned for **12/12 categories**.
> - Launch discussions #1, #2, and #3 are in **Announcements**, **Introductions**, and **Project Showcase**. All three are pinned.
> - The social preview is uploaded and matches `assets/branding/social-preview.png`.
>
> `python3 scripts/verify_discussions.py` reports **AUTOMATED CHECKS PASS**. One manual UI check remains: confirm that Announcements uses the **Announcement** format and only maintainers can start discussions.

---

## 1. Why this is manual

GitHub Discussions categories are repository settings, not files. Adding Markdown documents to a repository cannot create categories, change discussion formats, or move existing discussions.

The GitHub GraphQL API supports creating discussions and changing a discussion's category, but category **creation and deletion** are handled through the repository's Discussions settings in the web interface. The repository's automated setup therefore stops at documentation and verification.

**Verified limitation:** the available GraphQL mutations include `createDiscussion`, `updateDiscussion`, `deleteDiscussion`, and related comment and answer mutations. No discussion-category creation mutation is available.

## 2. Category architecture

Use the exact names, emojis, descriptions, and formats below when maintaining or recreating a category.

| Order | Emoji | Category name | Format | Description |
| --- | --- | --- | --- | --- |
| 1 | 📣 | **Announcements** | Announcement | Official DevSphere news, launches, policy updates, and roadmap announcements. |
| 2 | 👋 | **Introductions** | Open-ended discussion | Introduce yourself, share your background, and meet other members. |
| 3 | 💬 | **General Discussion** | Open-ended discussion | Community conversations, technology topics, and ideas that do not fit elsewhere. |
| 4 | 💻 | **Programming** | Open-ended discussion | Languages, algorithms, architecture, tooling, and software engineering practice. |
| 5 | 🤖 | **AI & Machine Learning** | Open-ended discussion | Machine learning, deep learning, LLMs, generative AI, evaluation, and responsible AI. |
| 6 | 🌐 | **Web Development** | Open-ended discussion | Frontend, backend, React, Next.js, Node.js, accessibility, and web performance. |
| 7 | 📱 | **App Development** | Open-ended discussion | Android, iOS, Flutter, React Native, and cross-platform product development. |
| 8 | 🚀 | **Project Showcase** | Open-ended discussion | Share what you are building, request feedback, and discover community projects. |
| 9 | 🙋 | **Questions & Help** | Question and answer | Ask technical questions and mark the reply that solves your problem. |
| 10 | 🏆 | **Hackathons & Challenges** | Open-ended discussion | Coding challenges, hackathons, competitions, teams, and results. |
| 11 | 🤝 | **Collaboration** | Open-ended discussion | Find teammates, reviewers, co-founders, and open-source collaborators. |
| 12 | 🎓 | **Career & Opportunities** | Open-ended discussion | Jobs, internships, scholarships, fellowships, and career advice. |

### Why these formats?

- **Announcements (Announcement):** only maintainers and administrators can start discussions, keeping official updates signal-rich. Anyone can reply unless the thread is locked.
- **Questions & Help (Question and answer):** supports accepted answers, making solutions easier to find.
- **All other categories (Open-ended discussion):** any member can start a conversation, which is essential for a community-driven space.
- **No Polls category:** polls can still be created in open-ended categories when a decision needs community input. A dedicated Polls category adds clutter without adding participation.

### Recognition program mapping

The Developer Spotlight and Community Recognition program deliberately uses existing categories:

| Program need | Existing category |
| --- | --- |
| Program announcements and published profiles | **Announcements** |
| Nominations, questions, and Builder of the Month nominations | **General Discussion** |
| Project Review Friday submissions | **Project Showcase** |
| Collaboration and teammate matching | **Collaboration** |

Do not create a separate `Spotlight`, `Recognition`, or `Nominations` category. It would add a 13th category, fragment the conversation, and require changes to the verified architecture. See the [recognition publishing guide](discussions/recognition/README.md).

## 3. Verified live configuration

| Check | Status |
| --- | --- |
| Discussions enabled | ✅ Verified |
| Exactly 12 categories | ✅ Verified by the read-only verifier |
| Category names contain no embedded emoji | ✅ Verified |
| Emoji metadata returned for every category | ✅ 12/12 |
| Questions & Help uses the question-and-answer format | ✅ Verified via `isAnswerable` |
| Announcements uses the Announcement format | ⏳ Confirm in the GitHub UI |
| Launch post #1 in Announcements | ✅ Verified |
| Launch post #2 in Introductions | ✅ Verified |
| Launch post #3 in Project Showcase | ✅ Verified |
| Launch posts #1–#3 pinned | ✅ Verified |
| Category sidebar order matches the table above | ⏳ Visual check in the GitHub UI |
| Social preview uploaded | ✅ Verified |
| Repository validation and Markdown lint | ✅ Passing |

The GraphQL API returns categories alphabetically, not in sidebar order. Confirm the visible order in the repository interface.

## 4. Verify the configuration

Run the read-only verifier from the repository root:

```bash
python3 scripts/verify_discussions.py
```

The script checks the category count, names, slugs, emoji metadata, discussion placement, and pinned posts. It does **not** change GitHub settings.

Expected automated result:

```text
Categories: 12/12
Emoji metadata returned for 12/12 categories.
#1 -> Announcements
#2 -> Introductions
#3 -> Project Showcase
Pinned discussions: #1, #2, #3
Result: AUTOMATED CHECKS PASS
```

### Manual UI checks

1. Open **Settings → General → Features** and confirm **Discussions** is enabled.
2. Open the category manager and confirm the visible sidebar order matches [the architecture table](#2-category-architecture).
3. Open **Announcements** and confirm the format is **Announcement** and that a non-maintainer account cannot start a discussion.
4. Confirm every category link below opens without a 404.
5. Keep pinned posts to three or four.

## 5. Category links

The live category links use these exact slugs:

| Category | Live URL |
| --- | --- |
| Announcements | [Open](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/announcements) |
| Introductions | [Open](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/introductions) |
| General Discussion | [Open](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/general-discussion) |
| Programming | [Open](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/programming) |
| AI & Machine Learning | [Open](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/ai-machine-learning) |
| Web Development | [Open](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/web-development) |
| App Development | [Open](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/app-development) |
| Project Showcase | [Open](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/project-showcase) |
| Questions & Help | [Open](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/questions-help) |
| Hackathons & Challenges | [Open](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/hackathons-challenges) |
| Collaboration | [Open](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/collaboration) |
| Career & Opportunities | [Open](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/career-opportunities) |

Do not guess a category URL. Open the category from the sidebar and copy the real link.

## 6. Recreating or editing a category

You need **maintain** or **admin** permission.

1. Open the [Discussions tab](https://github.com/Sumit-tech01/DevSphere-Community/discussions).
2. In the left sidebar, find **Categories** and click the pencil icon.
3. To edit a category, change its name, emoji, description, or format in place. Avoid deleting a category that contains discussions.
4. To create a missing category, click **New category** and use the exact name, emoji, description, and format from [the architecture table](#2-category-architecture).
5. Each category name and emoji pair must be unique. GitHub allows up to 25 categories per repository; DevSphere uses exactly 12.
6. Drag categories into the intended order and save.
7. Re-run the verifier and complete the manual UI checks.

Do not create a duplicate category when one already exists under a slightly different name. Edit the existing category instead.

## 7. Publishing the prepared posts

Twelve draft files are in [`community/discussions/`](discussions/README.md). Each file includes hidden metadata comments with the recommended title, category, format, and labels. Three drafts correspond to live discussions #1, #2, and #3; use them only as reference copy or to refresh the existing bodies. The other nine can be published when there is capacity to respond.

**Publishing rules:**

- Do not publish drafts **01**, **03**, or **04** as new threads. Keep #1, #2, and #3 and refresh them in place.
- Space new posts over several weeks instead of publishing everything at once.
- Personalize dates, challenge numbers, and links before posting.
- Verify that links resolve and that no placeholder text remains.
- Do not publish a thread unless there is capacity to reply.
- Keep the pinned set small.

## 8. Troubleshooting

| Problem | Likely cause | Solution |
| --- | --- | --- |
| No pencil icon next to Categories | Insufficient permission | Ask a repository admin or confirm you have maintain/admin access |
| Cannot delete a category | Category contains discussions | Choose a destination category when deleting, or move discussions first |
| Category name is rejected | Name/emoji pair already exists | Use a unique name and emoji combination |
| Category name shows a leading hyphen or duplicated emoji | Emoji was typed into the **Name** field | Edit the category, remove the emoji from **Name**, then choose it with the emoji picker |
| More than 12 categories appear | An extra category was created | Review the list and remove only an empty, unintended category |
| A launch post is not pinned | Pin action was not run | Open the discussion's **⋯** menu and choose **Pin**; no GraphQL pin mutation is available |
| "Change category" is missing | Interface version or permissions | Use the edit view or GraphQL `updateDiscussion` with `categoryId` |
| Category link returns 404 | Wrong slug or category not created | Open the category from the sidebar and copy the real URL |
| Announcements allows member posts | Wrong format selected | Edit the category and set format to **Announcement** |
| Q&A has no accepted answer | Wrong format selected | Edit the category and set format to **Question and answer** |
| Existing discussions disappeared | A category was deleted | Check the destination category selected during deletion |

## 9. Maintenance

- Review categories **quarterly** or when a category consistently receives misplaced posts.
- Do not create a new category for every technology; add one only when there is sustained conversation.
- Move misplaced discussions instead of deleting them.
- Update pinned posts when challenges, policies, or programs change.
- Record category changes in the [changelog](../CHANGELOG.md).
- Re-run the verifier after any structural change.

## 10. Automation status

| Task | Status |
| --- | --- |
| Discussions enabled | ✅ Verified |
| Repository files and discussion drafts | ✅ In this repository |
| Twelve categories with clean names and slugs | ✅ Verified |
| Emoji metadata | ✅ 12/12 verified |
| Moving existing discussions | ✅ Completed; #1–#3 are correctly categorized |
| Pinning launch posts | ✅ #1–#3 pinned |
| Social preview upload | ✅ Uploaded and verified |
| Announcement format / maintainer-only posting | ⏳ Manual UI confirmation |
| Category sidebar order | ⏳ Manual UI confirmation |
| Assigning moderators | Optional; do this when there is a consistent team |
| Publishing the remaining posts | Manual and optional; do it only with response capacity |

After any manual change, update the status note at the top of this document and re-run `python3 scripts/verify_discussions.py`.

---

**Related documents:** [Discussion Guide](DISCUSSION_GUIDE.md) · [Community Guidelines](COMMUNITY_GUIDELINES.md) · [Moderation Policy](MODERATION_POLICY.md) · [Ready-to-publish posts](discussions/README.md) · [Recognition publishing guide](discussions/recognition/README.md) · [Developer Spotlight](DEVELOPER_SPOTLIGHT.md) · [Launch Playbook](LAUNCH_PLAYBOOK.md)
