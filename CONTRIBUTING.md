# Contributing to DevSphere

Thank you for your interest in improving DevSphere. This repository contains the community's policies, learning resources, discussion playbook, challenge system, and brand assets. Contributions of every size are welcome — from fixing a broken link to proposing a new community program.

This guide explains how to contribute safely, clearly, and in a way that is easy to review.

---

## Table of contents

- [Before you contribute](#before-you-contribute)
- [Ways to contribute](#ways-to-contribute)
- [Contribution workflow](#contribution-workflow)
- [Commit messages](#commit-messages)
- [Pull request standards](#pull-request-standards)
- [Writing and documentation standards](#writing-and-documentation-standards)
- [Brand and design contributions](#brand-and-design-contributions)
- [Challenge submissions](#challenge-submissions)
- [Review process](#review-process)
- [Local validation](#local-validation)
- [Community expectations](#community-expectations)
- [License](#license)

---

## Before you contribute

1. Read the **[Code of Conduct](CODE_OF_CONDUCT.md)** and **[Community Guidelines](community/COMMUNITY_GUIDELINES.md)**. They apply to every contribution.
2. Search existing [issues](https://github.com/Sumit-tech01/DevSphere-Community/issues), [pull requests](https://github.com/Sumit-tech01/DevSphere-Community/pulls), and [discussions](https://github.com/Sumit-tech01/DevSphere-Community/discussions) to avoid duplicate work.
3. For a small fix — a typo, a broken link, a formatting issue — you can open a pull request directly.
4. For a significant change — a new section, policy, category, resource collection, or brand asset — open an issue first so the approach can be discussed.
5. Never include passwords, API keys, tokens, private personal information, or confidential material in an issue, discussion, commit, or pull request.

If you are unsure where to start, read **[SUPPORT.md](SUPPORT.md)** or ask in the **Questions & Help** discussion category.

## Ways to contribute

| Contribution | Where it belongs |
| --- | --- |
| Report a broken link, typo, or invalid template | [Bug report](.github/ISSUE_TEMPLATE/bug_report.md) or a focused pull request |
| Suggest a new resource, section, or program | [Feature request](.github/ISSUE_TEMPLATE/feature_request.md) |
| Share a project with the community | [Project showcase](.github/ISSUE_TEMPLATE/project_showcase.md) or Discussions |
| Improve documentation, policies, or templates | Pull request |
| Propose a coding challenge | Issue using the challenge template idea, then a pull request to `challenges/` |
| Improve branding or accessibility | Pull request with before/after context |
| Answer community questions | Discussions — no repository change required |
| Review another contributor's work | Pull request review or a constructive discussion reply |

## Contribution workflow

### 1. Fork the repository

Use the **Fork** button on GitHub, then clone your fork:

```bash
git clone https://github.com/<your-username>/DevSphere-Community.git
cd DevSphere-Community
```

Add the upstream repository so you can stay current:

```bash
git remote add upstream https://github.com/Sumit-tech01/DevSphere-Community.git
git fetch upstream
```

### 2. Create a focused branch

Always branch from the latest `main`:

```bash
git checkout main
git pull upstream main
git checkout -b docs/improve-discussion-guide
```

Use a short, descriptive branch name:

| Prefix | Use for |
| --- | --- |
| `docs/` | Documentation, policies, resources |
| `fix/` | Broken links, typos, template errors |
| `feat/` | New community resources or sections |
| `brand/` | Branding and visual assets |
| `challenge/` | Challenge content |
| `ci/` | Validation workflows and tooling |

Keep one logical change per branch. Avoid mixing unrelated formatting, content, and configuration changes in the same pull request.

### 3. Make your changes

- Follow the existing structure, tone, and formatting.
- Use relative links for files inside this repository.
- Use official documentation URLs for external resources.
- Add descriptive `alt` text to images.
- Check spelling, grammar, and heading hierarchy.
- Do not add placeholder text, fake statistics, invented partnerships, or unverified claims.
- Do not add paid services, tracking scripts, or unnecessary dependencies.

### 4. Validate locally

Run the checks described in [Local validation](#local-validation). Fix any failures before opening a pull request.

### 5. Commit your changes

Write a clear commit message using the format described in [Commit messages](#commit-messages).

### 6. Push and open a pull request

```bash
git push origin docs/improve-discussion-guide
```

Open a pull request against `Sumit-tech01/DevSphere-Community:main` and complete the pull request template. Include:

- A short summary of the change.
- Why the change is useful.
- The files or sections affected.
- Screenshots for visual changes, if relevant.
- Validation commands you ran and their results.

### 7. Respond to review

Maintainers may request changes. Treat review as a collaboration, not a judgment. Keep the conversation focused on the contribution and update the pull request when you are ready.

## Commit messages

Use a clear, imperative style. [Conventional Commits](https://www.conventionalcommits.org/) are preferred:

```text
<type>(<scope>): <short summary>
```

Examples:

```text
docs(community): clarify the moderation appeal process
fix(resources): replace retired React documentation link
feat(challenges): add challenge 002 template
brand(logo): refine social preview spacing
ci(validation): check relative markdown links
```

Recommended types: `docs`, `fix`, `feat`, `brand`, `ci`, `chore`, `refactor`.

Guidelines:

- Keep the subject line under 72 characters.
- Use the imperative mood: "add", not "added" or "adds".
- Explain **why** in the body when the change is not obvious.
- Reference related issues with `Closes #123` when appropriate.
- Do not use vague messages such as "update", "changes", or "fix stuff".

## Pull request standards

A pull request is ready for review when:

- It addresses one clear problem or improvement.
- It follows the repository structure and naming conventions.
- All relative links resolve.
- Markdown passes the configured lint rules.
- SVG files are valid XML and include accessible titles.
- No secrets, private data, or credentials are included.
- The pull request template is complete.
- The contributor has read and followed the Code of Conduct.

Please do **not**:

- Force-push to `main` or to another contributor's branch.
- Delete or rewrite someone else's work without discussion.
- Open a pull request that only reformats unrelated files.
- Include generated files that the repository does not need.
- Add a dependency without explaining why it is necessary and free to use.

Maintainers may close a pull request that is inactive for an extended period after a reminder, or that does not align with the community's scope. You are always welcome to reopen the conversation.

## Writing and documentation standards

### Voice and tone

- Write for a global audience. Avoid idioms that may not translate well.
- Be direct, warm, and professional.
- Prefer short paragraphs and scannable lists.
- Explain acronyms on first use.
- Do not assume a specific country, time zone, education system, or currency.

### Formatting

- Use ATX headings (`#`, `##`, `###`) and do not skip heading levels.
- Use sentence case for headings, except for proper nouns and established titles.
- Use fenced code blocks with a language identifier when possible.
- Use tables for comparisons and quick reference, not for long prose.
- Keep line lengths readable; the linter does not enforce a hard limit.
- End files with a single newline.

### Links

- Prefer relative links for repository content: `[Contributing](CONTRIBUTING.md)`.
- Use full URLs only for external sites.
- Verify every link before submitting.
- Link to official documentation whenever possible.
- Do not link to paywalled, pirated, or unverified resources.
- Use descriptive link text; avoid "click here".

### Originality and attribution

- Write original explanations. Do not copy text from other websites without permission.
- Quote sparingly and attribute clearly.
- Respect licenses and trademarks.
- If you use an image or asset, confirm that it can be redistributed and record the source.

### Accuracy

- Test commands and code samples before submitting.
- Do not claim that a feature, category, or integration exists unless it has been verified.
- Do not invent community statistics, sponsors, partners, awards, or member counts.
- Label proposals and future plans clearly.

## Brand and design contributions

The DevSphere visual identity is defined in [`assets/branding/`](assets/branding/). Before changing a logo, banner, social preview, or color token:

1. Open an issue describing the problem and the proposed direction.
2. Preserve the core identity: geometric sphere, connected nodes, subtle letter D, and the palette in the [brand guidelines](assets/branding/README.md).
3. Provide SVG source and rendered PNG previews.
4. Check legibility at small sizes and on both light and dark backgrounds.
5. Do not use third-party logos, trademarks, or copyrighted artwork.

## Challenge submissions

Coding challenges are practice opportunities, not repository merge requests.

- Submit your solution as a **Project Showcase** discussion using the title format specified in the challenge.
- Include a repository link, a live demo if available, the technologies used, and a short reflection.
- Do not commit another participant's solution to this repository.
- If you want to improve the challenge itself — instructions, evaluation criteria, or resources — open an issue or pull request instead.
- Keep feedback specific, constructive, and focused on the work.

## Review process

1. **Triage.** A maintainer checks the pull request for scope, completeness, and template compliance.
2. **Review.** A maintainer or contributor reviews content, links, formatting, and accessibility.
3. **Revision.** The contributor addresses feedback and re-runs validation.
4. **Approval.** At least one maintainer approval is required before merge.
5. **Merge.** The maintainer chooses the appropriate merge method and keeps the history clear.
6. **Follow-up.** Related issues are closed and, when useful, the change is noted in the changelog.

Review timelines are best-effort. DevSphere is a volunteer community, so please be patient and feel free to ask for a status update after a reasonable period.

## Local validation

The repository uses free, GitHub-native checks. You can run the same checks locally.

### Required

```bash
# Validate required files, relative links, SVG syntax, and workflow YAML
python3 scripts/validate_repository.py
```

### Markdown linting

```bash
npx --yes markdownlint-cli2 "**/*.md"
```

The configuration is in [`.markdownlint.json`](.markdownlint.json). If `npx` is unavailable, install Node.js from [nodejs.org](https://nodejs.org/en/download) or rely on the GitHub Actions workflow.

### SVG validation

```bash
xmllint --noout assets/branding/*.svg
```

### Git hygiene

```bash
git status
git diff --check
git log --oneline -5
```

`git diff --check` catches trailing whitespace and conflict markers.

The GitHub Actions workflow runs the validation script and markdown linting on every push and pull request to `main`.

## Community expectations

- Be respectful and assume good intent.
- Give credit and cite sources.
- Accept feedback gracefully and offer it kindly.
- Do not spam, self-promote excessively, or contact maintainers privately with unsolicited sales messages.
- Do not disclose security vulnerabilities publicly; follow [SECURITY.md](SECURITY.md).
- Do not use contributions to harvest personal data or promote scams.

Repeated violations may lead to moderation action under the [Moderation Policy](community/MODERATION_POLICY.md).

## License

By contributing, you agree that your contribution will be licensed under the repository's [MIT License](LICENSE), and you confirm that you have the right to submit it. Brand assets remain subject to the usage notes in the [brand guidelines](assets/branding/README.md).

---

Thank you for helping DevSphere become a thoughtful, useful, and welcoming community.

**Questions?** Read [SUPPORT.md](SUPPORT.md) or start a discussion in the **Questions & Help** category.
