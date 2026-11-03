# DevSphere Discussions Setup Guide

This guide is the administrative playbook for configuring DevSphere's GitHub Discussions. It records what is verified, what must be done manually, and how to confirm the result.

> **Live status verified 3 November 2026:**
>
> - Discussions are **enabled** for `Sumit-tech01/DevSphere-Community`.
> - **16 categories currently exist:** the 12 target categories plus four legacy categories (Ideas, Polls, Q&A, and Show and tell).
> - **11 of the 12 target categories have the emoji embedded in the Name field.** Their slugs begin with a hyphen, for example `-introductions` and `-general-discussion`. The Name field must be cleaned up and the emoji selected separately.
> - Three launch discussions exist:
>   - #1 Welcome to DevSphere, in **Announcements**, pinned.
>   - #2 Introduce Yourself to DevSphere, in **Introductions**, not pinned.
>   - #3 DevSphere Project Showcase, in **Project Showcase**, not pinned.
> - The social preview is uploaded and matches `assets/branding/social-preview.png`.
>
> The 12-category structure is present but not yet clean. Run `python3 scripts/verify_discussions.py` for the current live check.

---

## 1. Why this is manual

GitHub Discussions categories are repository settings, not files. Adding Markdown documents to a repository cannot create categories, change discussion formats, or move existing discussions.

The GitHub GraphQL API supports creating discussions and changing a discussion's category, but category **creation and deletion** are handled through the repository's Discussions settings in the web interface. The repository's automated setup therefore stops at documentation and post preparation.

**Verified limitation:** The available GraphQL mutations are `createDiscussion`, `updateDiscussion`, `deleteDiscussion`, and related comment/answer mutations. No discussion-category creation mutation is available.

## 2. Target category architecture

The target architecture is below. Use the exact names, emojis, descriptions, and formats when cleaning up or recreating a category.

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

## 3. Apply the configuration

You need **maintain** or **admin** permission on the repository.

### Step 1 — Confirm Discussions is enabled

1. Open the repository on GitHub, then go to **Settings → General**. The **Settings** tab is visible only to users with maintain or admin permission.
2. In the **Features** section, confirm **Discussions** is checked.
3. If it is not checked, enable it and save. This is a one-time setting.

### Step 2 — Open the category manager

1. Go to the [Discussions tab](https://github.com/Sumit-tech01/DevSphere-Community/discussions).
2. In the left sidebar, find **Categories**.
3. Click the **pencil icon** next to Categories.
4. The **Manage discussion categories** page opens.

### Step 3 — Remove the embedded emoji from category names

Eleven target categories were created with the emoji inside the **Name** field. This produces slugs beginning with a hyphen. Edit each category in place: remove the emoji from the Name field, then choose the emoji with the picker.

| Current live name | Correct Name field | Emoji | Format |
| --- | --- | --- | --- |
| 👋 Introductions | Introductions | 👋 | Open-ended discussion |
| 💬 General Discussion | General Discussion | 💬 | Open-ended discussion |
| 💻 Programming | Programming | 💻 | Open-ended discussion |
| 🤖 AI & Machine Learning | AI & Machine Learning | 🤖 | Open-ended discussion |
| 🌐 Web Development | Web Development | 🌐 | Open-ended discussion |
| 📱 App Development | App Development | 📱 | Open-ended discussion |
| 🚀 Project Showcase | Project Showcase | 🚀 | Open-ended discussion |
| ❓ Questions & Help | Questions & Help | 🙋 | Question and answer |
| 🏆 Hackathons & Challenges | Hackathons & Challenges | 🏆 | Open-ended discussion |
| 🤝 Collaboration | Collaboration | 🤝 | Open-ended discussion |
| 💼 Career & Opportunities | Career & Opportunities | 🎓 | Open-ended discussion |

**Announcements** already has a plain name and the 📣 emoji. Do not delete a target category that contains a discussion; edit it in place instead.

### Step 4 — Create any missing categories

All 12 target categories were present at the 3 November 2026 audit, so no creation is currently required. If a target category is missing, click **New category** and use its exact name, emoji, description, and format from the table in [section 2](#2-target-category-architecture). Do not create a duplicate when the category exists under a slightly different name; edit the existing category instead.

Each category name and emoji pair must be unique. GitHub allows up to 25 categories per repository; DevSphere uses exactly 12.

### Step 5 — Remove the four legacy categories

The target structure does not include **Ideas**, **Polls**, **Q&A**, or **Show and tell**. All four were empty at the 3 November 2026 audit.

1. Open each category and confirm it has no discussions.
2. If a category is empty, click the trash icon next to it and confirm deletion.
3. If it contains discussions, choose a destination category during deletion so nothing is lost.
4. Do not delete **Announcements** or any target category.

The documented target is exactly 12 categories. Do not keep extra categories unless the change is deliberate and recorded.

### Step 6 — Order the categories

On the **Manage discussion categories** page, drag categories into the order shown in [section 2](#2-target-category-architecture). The sidebar order is the first thing new members see, so keep the journey intentional:

1. Welcome: Announcements, Introductions
2. Community: General Discussion
3. Learn: Programming, AI & Machine Learning, Web Development, App Development
4. Build: Project Showcase, Questions & Help, Hackathons & Challenges, Collaboration
5. Grow: Career & Opportunities

### Step 7 — Verify the three launch discussions

The category move was completed on 3 November 2026. Discussion URLs are unchanged because they use the discussion number.

| Discussion | Current category | Status |
| --- | --- | --- |
| #1 Welcome to DevSphere — The Global Developer Community | **Announcements** | Keep; pinned |
| #2 Introduce Yourself to DevSphere | **Introductions** | Moved; pin pending |
| #3 DevSphere Project Showcase — What Are You Building? | **Project Showcase** | Moved; pin pending |

Do not create duplicate discussions. If a discussion needs to be moved again, use one of the options below.

**Option A — Web interface**

1. Open the discussion.
2. Click the **...** menu in the top-right of the discussion.
3. Choose **Change category** (or open the edit view and select the category, depending on the GitHub interface version).
4. Select the destination and save.
5. Verify the category label appears on the discussion.

**Option B — GraphQL API (advanced)**

List the category and discussion IDs:

```bash
gh api graphql -f query='
query {
  repository(owner: "Sumit-tech01", name: "DevSphere-Community") {
    discussionCategories(first: 25) {
      nodes { id name }
    }
  }
}'
```

Then update each discussion. Replace the category and discussion IDs with the values from your repository:

```bash
gh api graphql -f query='
mutation {
  updateDiscussion(input: {
    discussionId: "D_kwDO...",
    categoryId: "DIC_kwDO..."
  }) {
    discussion { number title category { name } }
  }
}'
```

Do not paste tokens into commands; the authenticated `gh` CLI handles credentials.

### Step 8 — Pin and label the launch posts

1. Confirm #1 is pinned in **Announcements** — verified.
2. Pin #2 in **Introductions** — pending.
3. Pin #3 in **Project Showcase** — pending.
4. Add labels such as `announcement`, `introduction`, `showcase`, `challenge`, and `question` where they help filtering.
5. Keep pinned posts to a small set; too many pinned threads bury new conversations.

GitHub's GraphQL API exposes no discussion-pin mutation, so pinning must be done in the web interface.

### Step 9 — Assign category moderators (when the team grows)

In the category settings, add moderators who have shown consistent, fair judgment. Category moderators can help move posts and enforce the [Community Guidelines](COMMUNITY_GUIDELINES.md). Do not assign moderation rights before the person has read the [Moderation Policy](MODERATION_POLICY.md).

### Step 10 — Verify the configuration

Status verified on 3 November 2026:

- [x] Discussions is enabled in repository settings.
- [ ] Exactly twelve categories exist with the documented names and emojis.
- [ ] Category names contain no embedded emoji.
- [x] #1 is in Announcements.
- [x] #2 is in Introductions.
- [x] #3 is in Project Showcase.
- [x] #1 is pinned.
- [ ] #2 and #3 are pinned.
- [x] Questions & Help uses the **Question and answer** format.
- [ ] Announcements uses the **Announcement** format.
- [x] All other target categories are non-answerable.
- [ ] Ideas, Polls, Q&A, and Show and tell are removed.
- [ ] Categories appear in the intended order.
- [ ] A test question can be marked as answered in Questions & Help.
- [ ] A non-maintainer account cannot start a discussion in Announcements.
- [ ] Category links use clean slugs and open without a 404.
- [ ] The README category table matches the live categories.

## 4. Category links

After configuration, the category URLs should follow this pattern:

```text
https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/<slug>
```

Until Step 3 is complete, the live slugs for the 11 affected categories begin with a hyphen, for example `-introductions`. Use the links from the live sidebar rather than guessing. The table below is the expected slug after the Name field is cleaned up; GitHub may regenerate it when the category is edited.

| Category | Expected slug |
| --- | --- |
| Announcements | `announcements` |
| Introductions | `introductions` |
| General Discussion | `general-discussion` |
| Programming | `programming` |
| AI & Machine Learning | `ai-machine-learning` |
| Web Development | `web-development` |
| App Development | `app-development` |
| Project Showcase | `project-showcase` |
| Questions & Help | `questions-help` |
| Hackathons & Challenges | `hackathons-challenges` |
| Collaboration | `collaboration` |
| Career & Opportunities | `career-opportunities` |

Verify each slug in the browser before adding category-specific links to the README. Do not guess a URL and publish it as working.

## 5. Publishing the prepared posts

Twelve draft files are in [`community/discussions/`](discussions/README.md). Each file includes hidden metadata comments with the recommended title, category, format, and labels. Three drafts correspond to the live discussions #1, #2, and #3; use them only as reference copy or to refresh the existing bodies. The other nine are ready to publish.

**Publishing rules:**

- Do not publish drafts **01**, **03**, or **04** as new threads. Keep #1, #2, and #3 and refresh them in place.
- Update and pin the existing **Introduce Yourself** (#2) and **Project Showcase** (#3) posts.
- Space the remaining nine posts over the first two weeks instead of publishing everything at once.
- Personalize dates, challenge numbers, and links before posting.
- Verify that links resolve and that no placeholder text remains.

## 6. Troubleshooting

| Problem | Likely cause | Solution |
| --- | --- | --- |
| No pencil icon next to Categories | Insufficient permission | Ask a repository admin or confirm you have maintain/admin access |
| Cannot delete a category | Category contains discussions | Choose a destination category when deleting, or move discussions first |
| Category name is rejected | Name/emoji pair already exists | Use a unique name and emoji combination |
| Category name shows a leading hyphen or duplicated emoji | Emoji was typed into the **Name** field | Edit the category, remove the emoji from **Name**, then choose it with the emoji picker |
| 16 categories remain instead of 12 | Legacy categories are still present | Delete **Ideas**, **Polls**, **Q&A**, and **Show and tell** after moving any discussions |
| A launch post is not pinned | Pin action was not run | Open the discussion's **⋯** menu and choose **Pin**; no GraphQL pin mutation is available |
| "Change category" is missing | Interface version or permissions | Use the edit view or GraphQL `updateDiscussion` with `categoryId` |
| Category link returns 404 | Wrong slug or category not created | Open the category from the sidebar and copy the real URL |
| Announcements allows member posts | Wrong format selected | Edit the category and set format to **Announcement** |
| Q&A has no accepted answer | Wrong format selected | Edit the category and set format to **Question and answer** |
| Existing discussions disappeared | A category was deleted | Check the destination category selected during deletion |

## 7. Maintenance

- Review categories **quarterly** or when a category consistently receives misplaced posts.
- Do not create a new category for every technology; add one only when there is sustained conversation.
- Move misplaced discussions instead of deleting them.
- Update pinned posts when challenges, policies, or programs change.
- Record category changes in the [changelog](../CHANGELOG.md).
- Re-run the verification checklist after any structural change.

## 8. What was automated and what was not

| Task | Status |
| --- | --- |
| Discussions enabled | ✅ Verified enabled |
| Repository files and discussion drafts | ✅ Created in this repository |
| Target category creation | ✅ 12 target categories present (completed manually 3 November 2026) |
| Category name cleanup | ❌ Manual — 11 names still embed the emoji |
| Legacy category removal | ❌ Manual — Ideas, Polls, Q&A, and Show and tell remain |
| Moving existing discussions | ✅ Completed 3 November 2026 — #2 and #3 moved via GraphQL; URLs unchanged |
| Pinning posts | ⚠️ Partial — #1 pinned; #2 and #3 pending |
| Assigning moderators | ❌ Optional/manual |
| Publishing the remaining posts | ❌ Manual — nine remaining; drafts 01, 03, and 04 duplicate live threads |
| Social preview upload | ✅ Uploaded and verified 3 November 2026 — matches `assets/branding/social-preview.png` |

After the remaining cleanup, update the status note at the top of this document and re-run `python3 scripts/verify_discussions.py`.

---

**Related documents:** [Discussion Guide](DISCUSSION_GUIDE.md) · [Community Guidelines](COMMUNITY_GUIDELINES.md) · [Moderation Policy](MODERATION_POLICY.md) · [Ready-to-publish posts](discussions/README.md)
