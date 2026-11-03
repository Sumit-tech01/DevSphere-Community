# DevSphere Discussion Guide

GitHub Discussions is the central meeting place for DevSphere. This guide explains how to choose the right category, write a useful post, ask a question that gets answered, and keep conversations valuable for future readers.

> **For administrators:** GitHub Discussions categories cannot be created from repository files. See the [Discussions Setup Guide](DISCUSSION_SETUP.md) for the exact manual configuration.

---

## 1. Why Discussions?

Discussions are better than chat for a global community because they are:

- **Searchable.** Future members can find the answer without asking again.
- **Structured.** Categories and accepted answers keep knowledge organized.
- **Asynchronous.** People can participate across time zones.
- **Connected to the repository.** Discussions are part of the DevSphere GitHub home.
- **Free.** No additional platform or subscription is required.

Use Discussions for conversation, questions, showcases, collaboration, opportunities, and community programs. Use [issues](https://github.com/Sumit-tech01/DevSphere-Community/issues) for concrete changes to this repository.

## 2. Category map

| # | Category | Format | Use it for | Avoid |
| --- | --- | --- | --- | --- |
| 1 | **Announcements** | Announcement | Official updates, launches, policy changes, roadmap news | Member questions or project promotion |
| 2 | **Introductions** | Open-ended | Meeting the community and sharing your background | Recruiting or selling |
| 3 | **General Discussion** | Open-ended | Technology conversation, community ideas, open topics | Support requests that belong in Q&A |
| 4 | **Programming** | Open-ended | Languages, algorithms, architecture, tooling, code design | Job posts or unrelated promotion |
| 5 | **AI & Machine Learning** | Open-ended | ML, deep learning, LLMs, evaluation, responsible AI | Hype, fearmongering, or unverified claims |
| 6 | **Web Development** | Open-ended | Frontend, backend, React, Next.js, Node.js, accessibility, performance | Generic project showcases |
| 7 | **App Development** | Open-ended | Android, iOS, Flutter, React Native, mobile product work | Desktop or web-only topics |
| 8 | **Project Showcase** | Open-ended | Sharing projects, demos, and requesting feedback | Repetitive promotion or link drops |
| 9 | **Questions & Help** | Q&A | Specific technical questions with an answerable solution | Open-ended debate or showcases |
| 10 | **Hackathons & Challenges** | Open-ended | Events, challenges, team formation, results | Fake opportunities or paid bootcamp ads |
| 11 | **Collaboration** | Open-ended | Finding teammates, reviewers, co-founders, and contributors | Hiring posts (use Career) |
| 12 | **Career & Opportunities** | Open-ended | Jobs, internships, scholarships, career advice | Scams, fees, or MLM offers |

### Format notes

- **Announcement:** only maintainers can start discussions; replies may be enabled or locked.
- **Open-ended:** anyone can start a discussion; no accepted answer.
- **Q&A:** anyone can ask; replies can be marked as the answer.
- **Poll:** optional for community decisions; use sparingly and explain the context.

## 3. Choosing the right category

Ask yourself:

1. **Is this an official community update?** → Announcements
2. **Am I introducing myself?** → Introductions
3. **Do I need a solution to a specific technical problem?** → Questions & Help (Q&A)
4. **Am I sharing something I built?** → Project Showcase
5. **Am I looking for people to build with?** → Collaboration
6. **Is this about a language or engineering practice?** → Programming
7. **Is this about AI, web, or mobile specifically?** → The matching area category
8. **Is this about an event or challenge?** → Hackathons & Challenges
9. **Is this about a job, internship, or career?** → Career & Opportunities
10. **Everything else?** → General Discussion

If a post belongs somewhere else, a moderator may move it and leave a short note. This keeps the community navigable.

## 4. Writing a strong discussion

### Title

A good title is specific and searchable.

| Weak | Strong |
| --- | --- |
| "Help" | "React `useEffect` runs twice in development with StrictMode" |
| "My project" | "TaskFlow — an open-source Kanban board built with Next.js and Supabase" |
| "Looking for team" | "Seeking a Flutter developer for a 6-week accessibility app prototype" |
| "AI question" | "How do I evaluate a RAG pipeline when I have no labeled data?" |

### Body

Include:

- **Context:** what you are building, learning, or trying to decide.
- **Details:** versions, constraints, and relevant background.
- **Evidence:** code, errors, screenshots, or links.
- **Ask:** the specific response you want.
- **Effort:** what you have already tried.

### Formatting

- Use `##` headings for long posts.
- Use fenced code blocks with a language tag.
- Use bullet lists for steps and requirements.
- Link to official documentation rather than reposting it.
- Add alt text to screenshots.
- Remove secrets and personal data before posting.

### Example question template

````markdown
## What I am trying to do

I am building a small inventory API with Node.js and PostgreSQL.

## What happens

The server starts, but the first request fails with:

```text
Error: connect ECONNREFUSED 127.0.0.1:5432
```

## What I tried

- Confirmed PostgreSQL is running with `pg_isready`.
- Checked that the connection string uses the correct port.
- Tried the same connection string from `psql`.

## Environment

- Node.js 22
- PostgreSQL 16
- macOS 15

## Question

What else should I check before changing the connection pool configuration?
````

## 5. Asking questions in Q&A

1. Search for an existing answer first.
2. Choose **Questions & Help**.
3. Write a specific title and a complete description.
4. Add code, logs, and environment details.
5. Respond to clarifying questions.
6. When a reply solves your problem, **mark it as the answer**.
7. If you solve it yourself, post the solution and mark it.
8. Thank the people who helped, without pressuring them for more.

Do not delete a question after it is answered; the thread may help someone else.

## 6. Sharing a project

Use this structure:

```markdown
## Project name

One sentence describing what it does.

## The problem

Who is it for, and why does it matter?

## What I built

Key features, architecture, and notable technical decisions.

## Demo and repository

- Demo:
- Repository:
- Screenshots:

## Stack

Languages, frameworks, databases, and infrastructure.

## What I want feedback on

Be specific: UX, performance, code structure, naming, accessibility, or positioning.

## What is next

Known limitations and the next milestone.
```

Keep promotion proportional. Explain, do not just drop a link.

## 7. Finding collaborators

A collaboration post should include:

- Project name and one-line description.
- Current stage: idea, prototype, MVP, or production.
- The work that needs help.
- Required skills and nice-to-have skills.
- Time commitment and expected duration.
- Collaboration model: volunteer, open source, revenue share, or paid.
- Ownership, credit, and licensing expectations.
- How to express interest.

Be honest about uncertainty. Do not promise equity, funding, or users you do not have.

## 8. Sharing opportunities

Career and opportunity posts should include:

- Role or opportunity title.
- Organization and a link to the official source.
- Location, remote policy, and eligibility.
- Compensation range if available.
- Application process and deadline.
- Whether the poster is the employer, a recruiter, or sharing on behalf of someone else.

Do not post:

- Opportunities that require an upfront fee.
- "Unlimited earning" or commission-only roles disguised as jobs.
- Requests for identity documents or bank details.
- Recruiter spam or duplicate posts.

## 9. Community programs

### Weekly coding challenge

Challenge threads are posted in **Hackathons & Challenges**. Read the challenge brief, submit in **Project Showcase** using the requested title, and keep feedback constructive. Solutions are not merged into this repository.

### Weekly feedback thread

A recurring **General Discussion** thread invites suggestions about categories, resources, moderation, and community programs. Not every suggestion can be implemented, but every good-faith suggestion will be read.

### Open-source opportunities

Share issues, projects, and maintainers looking for help in **Collaboration** or **Open Source**-related discussions. Include the skill level, time estimate, and a direct link.

## 10. Notifications and following

- Use the **Subscribe** button on a discussion to receive updates.
- Watch the repository for announcements.
- Follow specific categories from the Discussions page.
- Mute a thread if it becomes noisy; do not use mute to avoid accountability for your own post.
- Mention people only when their input is genuinely needed.

## 11. What not to post

- Spam, referral links, or repeated promotion.
- Harassment, hate speech, or personal attacks.
- Credentials, private data, or doxxing.
- Piracy, malware, or instructions for abuse.
- Duplicate posts across multiple categories.
- Low-effort AI-generated answers you cannot verify.
- Off-topic political or religious debate.
- Recruiting that violates the [Community Guidelines](COMMUNITY_GUIDELINES.md).

## 12. If your post gets moderated

Moderation is about protecting the community, not silencing disagreement. If a post is edited, moved, locked, or removed, a moderator may explain why. Read the [Moderation Policy](MODERATION_POLICY.md) and use the appeal process if you believe a mistake was made.

## 13. For maintainers and moderators

- Welcome new members in Introductions.
- Keep pinned posts current.
- Move misplaced discussions instead of deleting them when possible.
- Mark answers in Q&A only when they genuinely resolve the question.
- Lock heated threads before they become harmful.
- Document repeated issues so the guidelines can improve.
- Review the category structure quarterly.

---

**A good discussion respects the reader's time and leaves the community with something reusable.**

If you are new, start with [Introduce Yourself](https://github.com/Sumit-tech01/DevSphere-Community/discussions) and read the [Community Guidelines](COMMUNITY_GUIDELINES.md).
