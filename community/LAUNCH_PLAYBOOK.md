# DevSphere Launch Playbook

This playbook covers the public launch of DevSphere: the 14-day publishing schedule, the first-100-member plan, launch copy, profile promotion, moderation operations, and new-member onboarding.

It does **not** replace the [Community Guidelines](COMMUNITY_GUIDELINES.md), [Moderation Policy](MODERATION_POLICY.md), or [Discussion Setup Guide](DISCUSSION_SETUP.md). It is the operating plan that ties them together.

> **Status (3 November 2026):** the repository, documentation, branding, and discussion drafts are complete. The social preview is uploaded and verified. Category names, formats, legacy-category cleanup, and pinned posts require manual attention. Run `python3 scripts/verify_discussions.py` for the current GitHub state.

---

## 1. Launch frame

| Item | Decision |
| --- | --- |
| Recommended launch | **Monday, 9 November 2026, 09:00 UTC** |
| Preparation window | 3–8 November 2026 |
| Launch owner | Founder |
| Primary platform | GitHub Discussions |
| Cost | Free; no paid membership or infrastructure |
| Primary goal | A credible, useful community with real participation |

### What "member" means here

GitHub does not have a "join community" button. For DevSphere, a **member** is a person who participates: introduces themselves, asks a question, answers one, shares a project, gives feedback, or joins a challenge.

Stars, forks, and watchers are support signals, not membership. Do not describe them as members.

### Success signals

Track these instead of vanity numbers:

- New introductions.
- Questions that receive a useful answer.
- Project threads with specific feedback.
- Challenge participation and completed submissions.
- People who return and participate again.
- Members helping other members without a maintainer prompting them.

### Honesty rules

- No fake accounts, testimonials, partnerships, sponsors, or statistics.
- No bought followers, engagement pods, or coordinated upvoting.
- No mass unsolicited direct messages.
- No guaranteed outcomes such as jobs, followers, or income.
- Disclose affiliation when sharing DevSphere anywhere.
- Follow each platform's self-promotion rules.

---

## 2. Pre-launch checklist

Complete this before the launch post goes live.

| Task | Where | Status at preparation |
| --- | --- | --- |
| Confirm Discussions is enabled | Repository settings | Verified enabled |
| Confirm discussions #1–#3 are preserved | Discussions | Verified |
| Confirm #1 is pinned | Announcements | Verified pinned |
| Create the 12 categories | Discussions settings | Pending manual |
| Move #2 to Introductions | Discussions | Pending categories |
| Move #3 to Project Showcase | Discussions | Pending categories |
| Publish the "Start Here" post | Introductions | Pending |
| Upload the social preview | Settings → General | Verified uploaded 3 November 2026 |
| Confirm CI is green | Actions | Verified |
| Re-check all launch links | Repository | Verified at preparation |
| Prepare the founder introduction | General Discussion | Drafted below |
| Prepare the LinkedIn announcement | LinkedIn | Drafted below |
| Prepare the GitHub profile block | Profile README | Drafted below |
| Build a warm-contact list | Private | Founder task |
| Confirm the launch date and time | Calendar | Pending |

### Link and permission checks

1. Open the repository in a private browsing window.
2. Confirm the README renders, images load, and the Discussions link works.
3. Confirm the repository is public.
4. Confirm the Actions workflow is green on `main`.
5. Confirm no credentials, private data, or unfinished placeholder text are present.

---

## 3. 14-day publishing schedule

The schedule starts on the recommended launch date. Adjust the dates, not the spacing.

**Do not publish discussion drafts 01, 03, or 04.** They duplicate existing discussions #1, #2, and #3. Preserve the existing threads and their URLs.

| Day | Date | Action | Category | Source |
| --- | --- | --- | --- | --- |
| 1 | Mon 9 Nov | Keep #1 pinned as the official announcement | Announcements | Existing #1 |
| 1 | Mon 9 Nov | Move #2 and pin it | Introductions | Existing #2 |
| 1 | Mon 9 Nov | Move #3 and pin it | Project Showcase | Existing #3 |
| 1 | Mon 9 Nov | Publish "Welcome to DevSphere — Start Here" | Introductions | Draft 02 |
| 2 | Tue 10 Nov | Publish the founder introduction and ask what members are building | General Discussion | Section 6 below |
| 3 | Wed 11 Nov | No new thread; reply to introductions and showcase posts | — | — |
| 4 | Thu 12 Nov | Publish "Open-Source Contribution Opportunities" | Collaboration | Draft 11 |
| 5 | Fri 13 Nov | No new thread; welcome new members and answer questions | — | — |
| 6 | Sat 14 Nov | Publish the AI and machine learning discussion | AI & Machine Learning | Draft 06 |
| 7 | Sun 15 Nov | Rest or reply only; publish a week-one note only if there are real updates | — | — |
| 8 | Mon 16 Nov | Publish the web development discussion | Web Development | Draft 07 |
| 9 | Tue 17 Nov | No new thread; invite specific warm contacts to real conversations | — | — |
| 10 | Wed 18 Nov | Publish the Challenge 001 progress thread | Hackathons & Challenges | Draft 08 |
| 11 | Thu 19 Nov | No new thread; answer challenge questions and review submissions | — | — |
| 12 | Fri 20 Nov | Publish the career and opportunities discussion | Career & Opportunities | Draft 10 |
| 13 | Sat 21 Nov | Post a challenge check-in comment; give feedback to participants | Hackathons & Challenges | Draft 08 thread |
| 14 | Sun 22 Nov | Publish the first weekly feedback thread and review launch metrics | General Discussion | Draft 12 |

### Week 3 queue

Do not rush these into the first 14 days:

- "Find Project Collaborators" — Collaboration — Draft 05.
- "Hackathons & Competitions" — Hackathons & Challenges — Draft 09.
- A Programming seed prompt.
- An App Development seed prompt.

### Scheduling rules

- Publish at most one new thread per day.
- Leave at least one empty day between major posts.
- Reply to every new thread within 24 hours during launch month.
- Do not publish a thread unless there is capacity to respond to it.
- Do not create a second thread for a topic that already has an active discussion.
- If a topic gets no response, reply with a useful prompt instead of reposting it.
- Keep pinned posts to three or four.

---

## 4. Category setup and verification

The full procedure is in the [Discussion Setup Guide](DISCUSSION_SETUP.md). This is the execution checklist for the current repository state.

### State observed on 3 November 2026

- Discussions is enabled.
- All 12 target categories exist, but 11 of them have the emoji embedded in the **Name** field. This produces slugs that begin with a hyphen, such as `-general-discussion`.
- Four legacy categories remain: Ideas, Polls, Q&A, and Show and tell. They contain no discussions and can be deleted.
- Discussion #1 is in Announcements, #2 is in Introductions, and #3 is in Project Showcase. Their URLs did not change when #2 and #3 were moved.
- #1 is pinned. #2 and #3 still need to be pinned manually.
- No discussion category creation API, REST endpoint, or `gh` command is available.

### Manual checklist

> **Fix names in place.** Select the category, remove the emoji from the **Name** field, and choose the emoji with the picker. Do not delete and recreate a target category that already contains a discussion; deleting a category can move its discussions.

- [ ] **Announcements** — keep the name plain and the 📣 emoji; confirm the **Announcement** format.
- [ ] **Introductions** — Name `Introductions`, emoji 👋, open-ended format.
- [ ] **General Discussion** — Name `General Discussion`, emoji 💬, open-ended format.
- [ ] **Programming** — Name `Programming`, emoji 💻, open-ended format.
- [ ] **AI & Machine Learning** — Name `AI & Machine Learning`, emoji 🤖, open-ended format.
- [ ] **Web Development** — Name `Web Development`, emoji 🌐, open-ended format.
- [ ] **App Development** — Name `App Development`, emoji 📱, open-ended format.
- [ ] **Project Showcase** — Name `Project Showcase`, emoji 🚀, open-ended format.
- [ ] **Questions & Help** — Name `Questions & Help`, emoji 🙋, question-and-answer format.
- [ ] **Hackathons & Challenges** — Name `Hackathons & Challenges`, emoji 🏆, open-ended format.
- [ ] **Collaboration** — Name `Collaboration`, emoji 🤝, open-ended format.
- [ ] **Career & Opportunities** — Name `Career & Opportunities`, emoji 🎓, open-ended format.
- [ ] Delete **Ideas**, **Polls**, **Q&A**, and **Show and tell** after confirming each is empty.
- [ ] Confirm the final count is exactly 12.
- [ ] Order the categories: Announcements, Introductions, General Discussion, Programming, AI & Machine Learning, Web Development, App Development, Project Showcase, Questions & Help, Hackathons & Challenges, Collaboration, Career & Opportunities.
- [ ] Confirm #1 is in Announcements, #2 is in Introductions, and #3 is in Project Showcase.
- [ ] Pin #2 and #3. GitHub's GraphQL API exposes no discussion-pin mutation, so use the web interface.
- [ ] Verify every category link opens without a 404.

### Verification command

Run this after setup:

```bash
python3 scripts/verify_discussions.py
```

The script is read-only. It checks the category count, names, formats, discussion placement, and pinned posts. It exits with status `1` until every required check passes.

For a raw category listing:

```bash
gh api graphql -f query='
query {
  repository(owner: "Sumit-tech01", name: "DevSphere-Community") {
    discussionCategories(first: 25) {
      nodes { name emoji isAnswerable }
    }
  }
}' --jq '.data.repository.discussionCategories.nodes[] | [.name, .emoji, .isAnswerable] | @tsv'
```

Expected results:

- Exactly 12 rows.
- Announcements is present.
- Questions & Help has `true` for `isAnswerable`.
- Every other category has `false`.
- No Ideas, Polls, Q&A, or Show and tell rows.

### Discussion placement check

```bash
gh api graphql -f query='
query {
  repository(owner: "Sumit-tech01", name: "DevSphere-Community") {
    discussions(first: 10) {
      nodes { number title category { name } }
    }
  }
}'
```

Expected: #1 in Announcements, #2 in Introductions, #3 in Project Showcase.

### Moving discussions without changing URLs

A GitHub discussion URL uses its number, for example `/discussions/2`. Changing the category does not change that number, so the URL is preserved.

After the categories exist, list their IDs and the discussion IDs:

```bash
gh api graphql -f query='
query {
  repository(owner: "Sumit-tech01", name: "DevSphere-Community") {
    discussionCategories(first: 25) { nodes { id name } }
    discussions(first: 10) { nodes { id number title } }
  }
}'
```

Then update only the category:

```bash
gh api graphql -f query='
mutation {
  updateDiscussion(input: {
    discussionId: "DISCUSSION_ID",
    categoryId: "CATEGORY_ID"
  }) {
    discussion { number title category { name } }
  }
}'
```

Do not run the mutation until the target categories exist. Do not paste tokens into commands; the authenticated `gh` CLI handles credentials.

---

## 5. Social preview

### Verified file state

| Check | Result |
| --- | --- |
| File | `assets/branding/social-preview.png` |
| Format | PNG |
| Dimensions | 1280 × 640 |
| Size | Approximately 194 KB |
| Visual check | Passed at full size and at 640 × 320 |
| Branding | Consistent with the DevSphere palette, wordmark, and sphere/D mark |

The image contains the DevSphere wordmark, the line "Connect. Code. Collaborate. Create.", a short community description, the sphere/D mark, and the repository URL. The text remains readable when scaled down for a social card.

### Upload status

**Verified uploaded on 3 November 2026.** The repository now serves a custom social card from `repository-images.githubusercontent.com`. The downloaded card is 1280 × 640 PNG and is byte-identical to `assets/branding/social-preview.png` (SHA-256 `e27461d3...4cb334`). GitHub still does not expose a public API for uploading this image, so the setting remains manual.

### Manual upload steps

1. Open the repository on GitHub while signed in as an administrator.
2. Go to **Settings → General**.
3. Find **Social preview**.
4. Click **Edit** or **Upload an image**.
5. Select `assets/branding/social-preview.png`.
6. Save the change.
7. Verify in a private browsing window or a link-preview inspector that the new card appears.
8. Do not claim the upload is complete until the preview is visible outside your own browser session.

---

## 6. Founder introduction

Use this as the Day 2 General Discussion post. Keep the facts current. Adjust any education or company detail before publishing if it has changed.

**Title:** Why I'm building DevSphere — and what I hope you'll do here

> Hi, I'm Sumit Suresh Jagtap Patil. I'm a developer and AI engineer from Pune, India. I study CSE (Data Science) at ADYPU × NxtWave and build Clariyo, a student ecosystem for mentorship, hackathons, careers, and founder community.
>
> I started DevSphere because most of what I know came from other people: a patient answer to a basic question, a code review that pointed at the real problem, or someone sharing an opportunity they did not have to share.
>
> That kind of help is hard to find when you are learning alone. I wanted a place where it is normal.
>
> DevSphere is free and lives on GitHub Discussions. There is no application, no membership fee, and no private group to join. You need a GitHub account and a genuine interest in building.
>
> Here is what I hope you will do:
>
> - Introduce yourself. A short hello is enough.
> - Ask the question you have been holding back.
> - Share something you are building, even if it is unfinished.
> - Answer one question or give one piece of specific feedback.
>
> I will be reading and replying. If something is confusing, broken, or missing, tell me.
>
> To start: introduce yourself in **Introductions**, then tell us what you are building in **Project Showcase**.
>
> I'll go first: I'm building Clariyo and DevSphere. What are you building?

### Personalization notes

- Add one true sentence about the moment that made you want to build DevSphere.
- Do not add a title, credential, or achievement that is not accurate.
- Keep the tone conversational. This is an introduction, not a press release.
- If you change the founder name format in the repository, use the same format here.

---

## 7. LinkedIn launch announcement

Publish this on launch day. Keep the link in the post or in the first comment, and reply to comments for at least the first two hours.

> Today I'm opening DevSphere — a free, GitHub-native community for developers who want to learn, build, and collaborate in public.
>
> Most communities ask you to join another platform. DevSphere lives where the work already is: GitHub Discussions.
>
> Inside, you'll find space for:
>
> - Programming and software engineering
> - AI and machine learning
> - Web and app development
> - Project feedback and collaboration
> - Coding challenges
> - Career and open-source opportunities
>
> There is no fee, no application, and no private group to join. You need a GitHub account and a real interest in building.
>
> I started DevSphere because the best parts of my own learning came from other people: a code review, a patient answer, a shared opportunity. I want that kind of help to be easier to find.
>
> If you're learning, building, hiring, or looking for collaborators, you're welcome.
>
> Start here: https://github.com/Sumit-tech01/DevSphere-Community/discussions
>
> Tell me what you're working on. I'll be in the discussions.

### Publishing notes

- Do not add member counts, growth claims, or testimonials.
- Do not tag people who did not agree to be tagged.
- Use three to five relevant hashtags, not a wall of them.
- Put the direct Introductions link in the first comment.
- If the post gets questions, answer them in the comments instead of reposting.

---

## 8. GitHub profile promotion

These are recommendations. Do not change the profile without reviewing the result.

### High-impact actions

1. **Pin the repository.** On the GitHub profile, choose **Customize your pins** and pin `DevSphere-Community`.
2. **Add a profile README section.** Keep it short and link to Discussions.
3. **Set a profile status for launch week.** For example: "Opening DevSphere this week."
4. **Add the repository to the profile bio or website field** if there is room. The current profile website points to the portfolio; do not remove it without a replacement plan.
5. **Star and watch the repository** from the founder account so updates appear in the GitHub feed.
6. **Check name consistency.** The repository uses "Sumit Suresh Jagtap Patil"; the GitHub profile display name currently reads "Jagtap Sumit Suresh." Aligning them is optional but reduces confusion during launch.

### Profile README block

```markdown
### DevSphere

A free, GitHub-native developer community for programming, AI and machine learning, web and app development, project feedback, collaboration, and career growth.

[Join the Discussions →](https://github.com/Sumit-tech01/DevSphere-Community/discussions)
```

### Guardrails

- Do not rewrite the entire profile README for launch.
- Do not add DevSphere colors to the profile if they clash with the existing profile design.
- Do not claim the community is larger or older than it is.
- Do not ask for stars in exchange for anything.

---

## 9. First 100 members

### Working goal

Reach **100 participating accounts by 31 January 2027**. This is a working target, not a guarantee. A participant is someone who introduces themselves, comments, asks a question, shares a project, or joins a challenge.

If the target is not reached, review the channels and the content instead of inflating the number.

### Phase 1 — Launch window (days 1–14)

- Personally invite 20–30 people you already know. Ask for one genuine action: read a thread, share a project, or ask a question. Do not ask for a star.
- Publish the LinkedIn announcement and reply to every comment.
- Add DevSphere to the GitHub profile.
- Welcome every introduction within 24 hours.
- Run Challenge 001 and give feedback on every submission.
- Ask five developers for one piece of honest feedback on the community structure. Do not ask them to post fake activity.

### Phase 2 — Useful content (days 15–45)

- Publish two useful technical threads per week.
- Turn one strong discussion into a short article on Dev.to or Hashnode, with a link back to the specific thread.
- Invite maintainers to share real "good first issue" opportunities in Collaboration.
- Spotlight three member projects with permission.
- Share a build-in-public update on LinkedIn every two weeks, not every day.
- Join two or three relevant Discord or Slack communities and participate before sharing a link.

### Phase 3 — Distribution (days 46–90)

- Give one workshop or short talk at a university club or local meetup, if invited.
- Pitch one podcast or newsletter with a story about building a community in public, not a bare promotion.
- Ask active members to start their own discussions. The goal is member-led activity, not founder-led content.
- Run a second challenge with a clear brief and a reasonable time window.
- Publish a 90-day retrospective with real numbers and what changed.

### Channel plan

| Channel | Action | Guardrail |
| --- | --- | --- |
| Warm network | Personal, one-to-one invitations | No mass copy-paste; no pressure to join |
| LinkedIn | Launch post, then a useful update every two weeks | No engagement pods; no fake testimonials |
| GitHub profile | Pin, README block, status, star/watch | Do not spam followers |
| X, Bluesky, Mastodon | Build-in-public notes and links to specific threads | Follow each platform's promotion norms |
| Dev.to / Hashnode | Two practical articles tied to real discussions | Disclose that you founded the community |
| Reddit | Participate in communities that allow it | Read the rules; no drive-by link drops |
| Discord / Slack | Ask moderators before sharing | Use designated channels only |
| Campus / meetups | Offer a workshop or Q&A | Do not claim an official partnership |
| Open source | Invite real good-first-issue posts | No fake affiliation or endorsement |
| Newsletters / podcasts | Pitch the build-in-public story | No paid placement disguised as editorial |

### Weekly growth rhythm

| Day | Focus |
| --- | --- |
| Monday | Review the previous week's numbers and pick one improvement |
| Tuesday | Publish one technical thread or article |
| Wednesday | Reply to every open discussion and welcome new members |
| Thursday | Send five personal invitations or follow-ups |
| Friday | Share a challenge, career, or open-source thread |
| Weekend | Rest; reply only to active conversations |

### Metrics to track

- Repository views and clones from GitHub traffic insights, where available.
- Stars, forks, and watchers, treated as support signals.
- New discussion authors.
- Comments per discussion.
- Returning authors week over week.
- Introductions.
- Challenge submissions and feedback given.
- Referral sources, if GitHub provides them.

Do not publish a public dashboard that compares members or ranks people.

---

## 10. Weekly discussion calendar

After the 14-day launch, use a sustainable cadence. Three or four new threads per week is enough.

| Day | Thread | Notes |
| --- | --- | --- |
| Monday | Technical prompt | Rotate Programming, AI & Machine Learning, Web Development, and App Development |
| Wednesday | Project Showcase feedback | Ask for one specific question and give specific feedback |
| Friday | Career, open source, or collaboration | Rotate the theme; do not post all three |
| Sunday | Challenge check-in or weekly feedback | Use Draft 12 only when there is something to review |
| As needed | Announcements | Only for real news, policy changes, or milestones |

### Monthly rhythm

- Week 1: technical focus and a new challenge, if one is ready.
- Week 2: project feedback and member spotlight.
- Week 3: career, open source, and collaboration.
- Week 4: retrospective, roadmap update, and next month's prompt.

Do not open a thread just to fill the calendar. An empty day is better than a low-effort post.

---

## 11. Moderation workflow

The [Moderation Policy](MODERATION_POLICY.md) defines the rules and enforcement levels. This is the operating workflow.

### Daily routine

1. Check new discussions and reports once in the morning and once in the evening.
2. Welcome new introductions.
3. Move misplaced threads to the right category.
4. Answer or route unanswered questions.
5. Check link previews and pinned posts for stale information.

### Report handling

1. **Acknowledge** the report privately as soon as practical. Aim for 24 hours; do not promise 24/7 coverage.
2. **Assess immediate safety.** Threats, doxxing, credentials, malware, and exploitation come first.
3. **Preserve evidence.** Save links and context before deleting anything. Do not download or run untrusted files.
4. **Classify** the issue using the levels in the Moderation Policy.
5. **Act with the least intervention** that resolves the problem: private note, edit, move, hide, lock, remove, restrict, or block.
6. **Document** the decision privately: date, discussion, rule, action, and rationale. Do not publish personal data.
7. **Inform** the reporter at an appropriate level of detail.
8. **Escalate** serious or ambiguous cases to another maintainer when one exists. At launch, the founder handles escalations.
9. **Report** threats, coordinated fraud, or illegal content to GitHub and, when necessary, the relevant authorities.

### Common situations

| Situation | First action | Escalation |
| --- | --- | --- |
| Off-topic post | Move to the correct category and leave a short note | Repeat offense → warning |
| Duplicate thread | Lock the duplicate and link to the canonical thread | Repetition → warning |
| Spam or affiliate link | Remove content, lock if needed | Report coordinated activity to GitHub |
| Harassment or hate speech | Remove content and restrict the account | Report to GitHub; preserve evidence |
| Credentials posted | Remove immediately and tell the person to rotate the secret | Review repository history if committed |
| Security vulnerability | Follow the process in `SECURITY.md`; do not discuss details publicly | Private fix and disclosure |
| Doxxing or private data | Remove immediately; preserve minimal evidence | Report to GitHub; consider authorities |
| Founder conflict of interest | Recuse and ask another maintainer to review | Appoint a second reviewer before launch scale |

### Moderation guardrails

- Do not argue with a disruptive person in public.
- Do not publish private reports or identifying details.
- Do not use moderation powers to win technical disagreements.
- Do not promise confidentiality you cannot keep; explain the limits.
- Do not moderate while angry. Pause and ask for a second opinion when possible.
- Do not claim a moderation team exists before it does.

---

## 12. New-member onboarding

### Day 0 — welcome

When a new introduction appears, reply within 24 hours with a short, specific welcome. Avoid copy-paste that ignores what the person wrote.

Template:

> Welcome, [name]. Glad you're here. You mentioned [specific detail] — that's a useful place to start.
>
> Three good next steps:
>
> 1. Read the [Community Guidelines](COMMUNITY_GUIDELINES.md).
> 2. Share what you're building in **Project Showcase**, even if it's early.
> 3. Ask one specific question in **Questions & Help** when you get stuck.
>
> No pressure to post every day. Reading and lurking are welcome too.

### First seven days

| Day | Suggested action |
| --- | --- |
| 0 | Introduce yourself in Introductions |
| 1 | Read the guidelines and the Start Here post |
| 2 | Comment on one thread or answer one question |
| 3 | Share a project, a work-in-progress, or a learning note |
| 5 | Try Challenge 001 or give feedback to one submission |
| 7 | Tell us what would make DevSphere more useful |

### Operating rules

- Welcome manually while the community is small. Automation can wait.
- Do not send unsolicited direct messages to every new member.
- Do not tag people in unrelated threads.
- Track introductions in a private sheet only if needed for follow-up. Do not publish personal data.
- If volume grows, consider a GitHub Action for a single welcome comment, with rate limits and an opt-out. Do not build it before it is needed.

---

## 13. Launch-day runbook

| Time | Action |
| --- | --- |
| T-1 day | Confirm categories, pinned posts, social preview, links, and CI. Make no risky changes. |
| 09:00 UTC | Publish the Start Here post; move and pin #2 and #3; confirm #1 is pinned. |
| 09:15 UTC | Publish the LinkedIn announcement. |
| 09:30 UTC | Update the GitHub profile status and pin the repository. |
| 10:00 UTC | Send 10–15 personal invitations to people you already know. |
| 12:00 UTC | Reply to every comment and welcome every introduction. |
| 17:00 UTC | Check links, notifications, and the first-day questions. |
| End of day | Write a short private note: what worked, what confused people, what to fix tomorrow. |

Do not post a "we reached X members" update unless the number is real and the definition is clear.

---

## 14. Launch readiness checklist

### Verified complete

- [x] Repository is public with `main` as the default branch.
- [x] Description, homepage, and 12 topics are set.
- [x] Discussions is enabled.
- [x] Discussions #1, #2, and #3 are preserved.
- [x] #2 is in Introductions and #3 is in Project Showcase; their URLs are unchanged.
- [x] #1 is pinned in Announcements.
- [x] Repository validation and Markdown lint pass.
- [x] The social preview file is 1280 × 640, visually readable, uploaded, and verified against the repository OG image.
- [x] Twelve discussion drafts are reviewed and indexed.
- [x] Community guidelines, moderation policy, and roles are documented.
- [x] Launch schedule and growth plan are documented in this playbook.

### Pending manual actions

- [ ] Remove the embedded emoji from the 11 category names and select each emoji separately.
- [ ] Delete the empty Ideas, Polls, Q&A, and Show and tell categories.
- [ ] Pin #2 and #3.
- [ ] Publish the Start Here post.
- [ ] Publish the founder introduction.
- [ ] Publish the LinkedIn announcement.
- [ ] Update the GitHub profile promotion block.
- [ ] Confirm the launch date and time.

### Final gate

Launch only when the categories, pinned posts, social preview, and discussion placement checks pass. If a manual step is incomplete, say so; do not describe the configuration as finished.

---

## 15. After the first 14 days

1. Review which threads received replies and which did not.
2. Ask five members what they expected and what was missing.
3. Keep the cadence at three or four new threads per week.
4. Move from founder-led prompts to member-led discussions.
5. Update the roadmap with what actually happened, not what was planned.
6. Re-run the category and discussion placement checks after any structural change.
7. Record meaningful changes in the changelog.

The launch is not a one-day event. The first 14 days set the tone; the next 90 decide whether the community is useful enough to stay.
