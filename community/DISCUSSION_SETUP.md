# DevSphere Discussions Setup Guide

This guide is the administrative playbook for configuring DevSphere's GitHub Discussions. It records what is verified, what must be done manually, and how to confirm the result.

> **Status at the time of writing (3 November 2026):**
>
> - Discussions are **enabled** for `Sumit-tech01/DevSphere-Community`.
> - The repository still has GitHub's **default categories**: Announcements, General, Ideas, Polls, Q&A, and Show and tell.
> - Three launch discussions exist, all currently filed under **Announcements**:
>   - #1 Welcome to DevSphere
>   - #2 Introduce Yourself to DevSphere
>   - #3 DevSphere Project Showcase
>
> The 12-category structure below is the **target configuration**. It has **not** been applied automatically. GitHub does not expose a repository-file or public REST endpoint for creating discussion categories, so an administrator must create them in the GitHub web interface.

---

## 1. Why this is manual

GitHub Discussions categories are repository settings, not files. Adding Markdown documents to a repository cannot create categories, change discussion formats, or move existing discussions.

The GitHub GraphQL API supports creating discussions and changing a discussion's category, but category **creation and deletion** are handled through the repository's Discussions settings in the web interface. The repository's automated setup therefore stops at documentation and post preparation.

**Verified limitation:** The available GraphQL mutations are `createDiscussion`, `updateDiscussion`, `deleteDiscussion`, and related comment/answer mutations. No discussion-category creation mutation is available.

## 2. Target category architecture

Create the categories in this order. Use the exact names, emojis, descriptions, and formats.

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

1. Open [Repository Settings → General](https://github.com/Sumit-tech01/DevSphere-Community/settings).
2. In the **Features** section, confirm **Discussions** is checked.
3. If it is not checked, enable it and save. This is a one-time setting.

### Step 2 — Open the category manager

1. Go to the [Discussions tab](https://github.com/Sumit-tech01/DevSphere-Community/discussions).
2. In the left sidebar, find **Categories**.
3. Click the **pencil icon** next to Categories.
4. The **Manage discussion categories** page opens.

### Step 3 — Reuse or rename the default categories

Rename these defaults instead of creating duplicates:

| Current default | Action | New name | New emoji | New format | New description |
| --- | --- | --- | --- | --- | --- |
| Announcements | Keep | Announcements | 📣 | Announcement | Official DevSphere news, launches, policy updates, and roadmap announcements. |
| General | Rename | General Discussion | 💬 | Open-ended discussion | Community conversations, technology topics, and ideas that do not fit elsewhere. |
| Q&A | Rename | Questions & Help | 🙋 | Question and answer | Ask technical questions and mark the reply that solves your problem. |
| Show and tell | Rename | Project Showcase | 🚀 | Open-ended discussion | Share what you are building, request feedback, and discover community projects. |

To rename: click the pencil icon next to the category, update the emoji, name, description, and format, then click **Save changes**.

### Step 4 — Create the remaining eight categories

Click **New category** and create each of these using the table in [section 2](#2-target-category-architecture):

1. Introductions
2. Programming
3. AI & Machine Learning
4. Web Development
5. App Development
6. Hackathons & Challenges
7. Collaboration
8. Career & Opportunities

Each category name and emoji pair must be unique. GitHub allows up to 25 categories per repository; DevSphere uses 12.

### Step 5 — Remove the unused defaults

The target structure does not include **Ideas** or **Polls**.

1. Open each category and confirm it has no discussions.
2. If a category is empty, click the trash icon next to it and confirm deletion.
3. If it contains discussions, choose a destination category during deletion so nothing is lost.
4. Do not delete **Announcements**.

If you prefer to keep **Ideas**, you may retain it as a 13th category for community suggestions. The documented target is 12 categories; keeping one extra is acceptable but should be recorded as a deliberate change.

### Step 6 — Order the categories

On the **Manage discussion categories** page, drag categories into the order shown in [section 2](#2-target-category-architecture). The sidebar order is the first thing new members see, so keep the journey intentional:

1. Welcome: Announcements, Introductions
2. Community: General Discussion
3. Learn: Programming, AI & Machine Learning, Web Development, App Development
4. Build: Project Showcase, Questions & Help, Hackathons & Challenges, Collaboration
5. Grow: Career & Opportunities

### Step 7 — Move the three launch discussions

The existing discussions are currently under Announcements. After the new categories exist:

| Discussion | Move to |
| --- | --- |
| #1 Welcome to DevSphere — The Global Developer Community | **Announcements** (keep) |
| #2 Introduce Yourself to DevSphere | **Introductions** |
| #3 DevSphere Project Showcase — What Are You Building? | **Project Showcase** |

**Option A — Web interface**

1. Open the discussion.
2. Click the **...** menu in the top-right of the discussion.
3. Choose **Change category** (or open the edit view and select the category, depending on the GitHub interface version).
4. Select the destination and save.
5. Verify the category label appears on the discussion.

**Option B — GraphQL API (advanced)**

After creating the categories, list their IDs:

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

1. Pin the official welcome announcement in **Announcements**.
2. Pin **Introduce Yourself** in **Introductions**.
3. Pin **Share Your Projects** in **Project Showcase**.
4. Add labels such as `announcement`, `introduction`, `showcase`, `challenge`, and `question` where they help filtering.
5. Keep pinned posts to a small set; too many pinned threads bury new conversations.

### Step 9 — Assign category moderators (when the team grows)

In the category settings, add moderators who have shown consistent, fair judgment. Category moderators can help move posts and enforce the [Community Guidelines](COMMUNITY_GUIDELINES.md). Do not assign moderation rights before the person has read the [Moderation Policy](MODERATION_POLICY.md).

### Step 10 — Verify the configuration

Complete this checklist after setup:

- [ ] Discussions is enabled in repository settings.
- [ ] Twelve categories exist with the documented names and emojis.
- [ ] Announcements uses the **Announcement** format.
- [ ] Questions & Help uses the **Question and answer** format.
- [ ] All other categories use **Open-ended discussion**.
- [ ] Ideas and Polls are removed or intentionally retained and documented.
- [ ] Categories appear in the intended order.
- [ ] Discussion #1 is in Announcements.
- [ ] Discussion #2 is in Introductions.
- [ ] Discussion #3 is in Project Showcase.
- [ ] Pinned posts are relevant and current.
- [ ] A test question can be marked as answered in Questions & Help.
- [ ] A non-maintainer account cannot start a discussion in Announcements.
- [ ] Category links open without a 404.
- [ ] The README category table matches the live categories.

## 4. Category links

After configuration, the category URLs should follow this pattern:

```text
https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/<slug>
```

Expected slugs, subject to GitHub's slug generation:

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

Twelve ready-to-publish posts are in [`community/discussions/`](discussions/README.md). Each file includes hidden metadata comments with the recommended title, category, format, and labels.

**Publishing rules:**

- Publish the **launch announcement** first.
- Publish **Introduce Yourself** and **Share Your Projects** next, then pin them.
- Space the remaining posts over the first two weeks instead of publishing everything at once.
- Do not republish a discussion that already exists. The three launch discussions should be moved and updated rather than duplicated.
- Personalize dates, challenge numbers, and links before posting.
- Verify that links resolve and that no placeholder text remains.

## 6. Troubleshooting

| Problem | Likely cause | Solution |
| --- | --- | --- |
| No pencil icon next to Categories | Insufficient permission | Ask a repository admin or confirm you have maintain/admin access |
| Cannot delete a category | Category contains discussions | Choose a destination category when deleting, or move discussions first |
| Category name is rejected | Name/emoji pair already exists | Use a unique name and emoji combination |
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
| Category creation | ❌ Manual — no supported repository-file or category-creation API |
| Renaming default categories | ❌ Manual |
| Moving existing discussions | ❌ Manual (or GraphQL after categories exist) |
| Pinning posts | ❌ Manual |
| Assigning moderators | ❌ Manual |
| Publishing the 12 posts | ❌ Manual, intentionally not automated to avoid duplicates |
| Social preview upload | ❌ Manual — GitHub does not expose a REST endpoint for social preview images |

When the manual steps are complete, update the status note at the top of this document with the date and the verified category count.

---

**Related documents:** [Discussion Guide](DISCUSSION_GUIDE.md) · [Community Guidelines](COMMUNITY_GUIDELINES.md) · [Moderation Policy](MODERATION_POLICY.md) · [Ready-to-publish posts](discussions/README.md)
