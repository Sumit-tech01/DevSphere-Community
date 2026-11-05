# DevSphere Open-Source Guide

A practical guide to making your first open-source contribution and growing into a reliable contributor. It focuses on the workflow and communication that maintainers actually see; the curated link collection lives in [Open Source Resources](../resources/open-source.md).

> **No contribution is owed to you.** Maintainers are often volunteers. A pull request is a proposal, not a guarantee of merge, payment, mentorship, or employment.

## What open source is — and is not

Open source means software is released under a license that permits use, study, modification, and distribution under certain conditions. It does not mean:

- The maintainer must accept your change.
- The project owes you free support.
- You can ignore the license or attribution.
- Every issue is beginner-friendly.
- Contribution is a shortcut to a job.

Read the project's license. If there is no license, the code is not automatically open source.

## Before your first contribution

1. **Learn the Git basics.** `status`, `add`, `commit`, `branch`, `switch`, `merge`, `log`, and `push`.
2. **Create a GitHub account** and set a display name and profile photo if you are comfortable.
3. **Read the project's `README.md`, `CONTRIBUTING.md`, and `CODE_OF_CONDUCT.md`.**
4. **Search open and closed issues** before starting work.
5. **Run the project locally** and confirm the test command works.
6. **Choose a small, specific problem.** Documentation, tests, and reproducible bugs are excellent starts.

If the setup instructions are wrong, fixing them is a legitimate contribution. Say what failed and include the environment details.

## Finding beginner-friendly work

| Platform | What it offers | Link |
| --- | --- | --- |
| **GitHub good-first-issue topic** | Repositories and issues labeled for newcomers | [github.com/topics/good-first-issue](https://github.com/topics/good-first-issue) |
| **GitHub help-wanted topic** | Projects asking for help | [github.com/topics/help-wanted](https://github.com/topics/help-wanted) |
| **Good First Issue** | Curated beginner-friendly issues | [goodfirstissue.dev](https://goodfirstissue.dev/) |
| **Up For Grabs** | Projects welcoming new contributors | [up-for-grabs.net](https://up-for-grabs.net/) |
| **First Contributions** | A safe practice repository | [firstcontributions.github.io](https://firstcontributions.github.io/) |
| **First Timers Only** | Guidance for first-time contributors | [firsttimersonly.com](https://www.firsttimersonly.com/) |
| **Open Source Guides** | How to contribute and maintain projects | [opensource.guide](https://opensource.guide/) |

A label is not a guarantee that an issue is ready. Check:

- Is the issue open and assigned to someone?
- Is there a clear expected behavior?
- Does a maintainer confirm the approach?
- Is the repository active and reviewing pull requests?
- Is the required skill level realistic for you?

## Read the project before changing it

| File or surface | What to look for |
| --- | --- |
| `README` | Purpose, setup, supported versions, test command |
| `CONTRIBUTING` | Branch names, commit style, tests, review process |
| `CODE_OF_CONDUCT` | Expected behavior and reporting route |
| `LICENSE` | What you may do and what attribution is required |
| Issue tracker | Existing reports, maintainers' decisions, scope |
| Pull requests | Review tone, test expectations, merge patterns |
| CI configuration | Commands that must pass |
| Release notes | How changes are documented and shipped |

If the contribution guide and the maintainer's comment conflict, ask for clarification in the issue rather than guessing.

## Fork, clone, and branch

### Fork and clone

```bash
# Replace OWNER and REPOSITORY with the project you are contributing to.
git clone https://github.com/OWNER/REPOSITORY.git
cd REPOSITORY
git remote add upstream https://github.com/OWNER/REPOSITORY.git
git remote -v
```

If you are working from your own fork, clone your fork instead and add the original repository as `upstream`.

### Keep your fork current

```bash
git switch main
git pull upstream main
git push origin main
```

Use the default branch name of the project if it is not `main`.

### Create a focused branch

```bash
git switch -c fix/describe-the-change
```

Branch names should describe the work. Examples: `docs/install-notes`, `fix/null-cursor`, `test/retry-policy`.

## Make the change

- Keep the diff focused on one problem.
- Follow the existing style, even if you prefer another.
- Add or update tests for behavior changes.
- Update documentation when behavior or setup changes.
- Remove debug prints and unrelated formatting churn.
- Run the project's formatter, linter, and tests.
- Do not upgrade dependencies unless the issue requires it.

### Commit messages

A clear commit message explains what changed and why.

```text
fix(api): reject cursors with invalid signatures

The pagination cursor was decoded before signature verification,
which allowed malformed input to reach the query layer. Verify the
signature first and add a regression test for a tampered cursor.
```

Conventional Commits is optional unless the project requires it. Never claim a fix you did not verify.

## Open the pull request

A good pull request includes:

- A title that describes the change.
- A link to the issue, for example `Closes #123`.
- The problem and the chosen approach.
- Tests or manual verification steps.
- Screenshots for visual changes.
- Known limitations or follow-up work.
- A request for the specific review you need.

### Pull request checklist

- [ ] I read the contribution guide.
- [ ] The change is limited to one problem.
- [ ] I added or updated tests.
- [ ] I ran the relevant checks locally.
- [ ] I updated documentation when needed.
- [ ] I removed secrets, private data, and debug output.
- [ ] I linked the issue and explained the approach.
- [ ] I can respond to review feedback.

If the project uses a draft pull request, open a draft early to get direction before polishing. Do not open a draft and then disappear for weeks without a status note.

## Code review

Review is a conversation about the code. It is not a verdict on your worth.

When you receive feedback:

1. Read the whole review before replying.
2. Ask for clarification when a comment is ambiguous.
3. Fix blocking issues; explain disagreements with evidence.
4. Resolve conversations only when the concern is addressed.
5. Push additional commits; do not force-push someone else's branch.
6. Thank the reviewer, even when the answer is no.

When you review someone else:

- Ask questions before assuming a mistake.
- Distinguish correctness from preference.
- Suggest a test or a smaller change when possible.
- Do not rewrite the contributor's branch without permission.
- Approve only when you understand the change.

## Communicate with maintainers

- Comment on the issue before starting significant work.
- Use the project's preferred channel; do not mass-mention maintainers.
- Include reproduction steps, versions, logs, and what you tried.
- Be patient. A volunteer may take days or weeks.
- Do not send repeated "any update?" messages.
- If you must move on, say so and unassign yourself.
- Never pressure a maintainer for free labor, priority review, or employment.

## Common contribution types

| Contribution | Beginner-friendly? | What good looks like |
| --- | --- | --- |
| Fix a typo | Yes | Correct, scoped, no unrelated formatting |
| Improve documentation | Yes | Accurate setup steps and tested commands |
| Add a test | Yes | Fails before the fix, passes after |
| Fix a small bug | Yes | Reproducer, focused patch, regression test |
| Improve accessibility | Intermediate | Real user impact and verification |
| Refactor | Intermediate–Advanced | Behavior preserved, tests prove it |
| Add a feature | Advanced | Accepted design, tests, docs, review |
| Triage issues | Intermediate | Reproduces, labels, asks useful questions |
| Maintain a release | Advanced | Changelog, compatibility, security review |

## Maintainership

Maintaining is more than merging code. A healthy small project has:

- A README with setup and support boundaries.
- A license.
- A contribution guide.
- A code of conduct.
- Issue and pull request templates.
- Tests and CI.
- A security policy.
- A release and changelog process.
- A plan for saying no and stepping back.

Use [Open Source Guides — Starting a Project](https://opensource.guide/starting-a-project/), [Maintaining Balance](https://opensource.guide/maintaining-balance-for-open-source-maintainers/), and the [DevSphere open-source resources](../resources/open-source.md) for deeper guidance.

## Security

- Never commit credentials, tokens, private keys, or customer data.
- Report vulnerabilities privately using the project's security policy.
- Do not publish an exploit before a fix is available.
- Review dependency and license changes.
- Be careful with CI workflows from forks; do not expose secrets.
- If a secret is exposed, revoke it first, then rotate and clean history.

## First-contribution checklist

- [ ] I chose a project I can run locally.
- [ ] I read the contribution guide and code of conduct.
- [ ] I confirmed the issue is open and the approach is welcome.
- [ ] I created a focused branch.
- [ ] I made one coherent change.
- [ ] I added or updated tests and documentation.
- [ ] I ran the project's checks.
- [ ] I opened a clear pull request.
- [ ] I responded to review without pressure.
- [ ] I recorded what I learned.

## DevSphere contribution paths

- Use [Collaboration](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/collaboration) to find projects and collaborators.
- Use [Programming](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/programming) for language, tooling, and architecture questions.
- Use [Questions & Help](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/questions-help) for a specific technical problem.
- Read [CONTRIBUTING.md](../CONTRIBUTING.md) before changing this repository.
- Read the [Open Source Resources](../resources/open-source.md) collection for verified platforms and references.

DevSphere does not guarantee that an external project will accept a contribution. Verify every opportunity and never pay to contribute to an open-source project.

---

**Related:** [Collaboration Guide](COLLABORATION_GUIDE.md) · [Discussion Guide](DISCUSSION_GUIDE.md) · [Open Source Resources](../resources/open-source.md) · [Learning Roadmaps](../resources/learning-roadmaps.md) · [Collaboration discussions](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/collaboration)
