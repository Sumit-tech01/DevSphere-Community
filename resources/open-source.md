# Open Source Resources

A free guide to Git, GitHub, licensing, first contributions, project maintenance, and healthy open-source communities. For the step-by-step workflow and communication advice, read the [DevSphere Open-Source Guide](../community/OPEN_SOURCE_GUIDE.md); this page is the curated reference collection.

> Start with one small contribution. You do not need to be an expert to be useful. See the [resource index](README.md) for selection criteria.

## Git and GitHub fundamentals

| Resource | Level | Notes |
| --- | --- | --- |
| [Pro Git](https://git-scm.com/book/en/v2) | Beginner–Advanced | The complete free Git book |
| [Git Reference](https://git-scm.com/docs) | All | Official command reference |
| [GitHub — Get Started](https://docs.github.com/en/get-started) | Beginner | Accounts, repositories, and workflow basics |
| [GitHub — Using Git](https://docs.github.com/en/get-started/using-git) | Beginner | Common Git operations in GitHub |
| [GitHub Skills](https://skills.github.com/) | Beginner | Interactive, hands-on GitHub courses |
| [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow) | Beginner | Branch-based collaboration model |
| [Oh My Git!](https://ohmygit.org/) | Beginner | Open-source game for learning Git |
| [Learn Git Branching](https://learngitbranching.js.org/) | Beginner–Intermediate | Visual, interactive branching practice |

**Practice idea:** Create a repository, make a branch, open a pull request against your own `main`, request changes, and merge. Then repeat with a real project.

## GitHub collaboration features

| Feature | Official guide |
| --- | --- |
| Issues | [About issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) |
| Pull requests | [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) |
| Code review | [Reviewing changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests) |
| Discussions | [About discussions](https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/about-discussions) |
| Projects | [About Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) |
| Actions | [GitHub Actions documentation](https://docs.github.com/en/actions) |
| Pages | [GitHub Pages documentation](https://docs.github.com/en/pages) |
| Security advisories | [About repository security advisories](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories) |

## Making your first contribution

| Resource | Why it helps |
| --- | --- |
| [Open Source Guides — How to Contribute](https://opensource.guide/how-to-contribute/) | The complete first-contribution path |
| [GitHub — Contributing to a project](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project) | Fork, clone, branch, and pull request |
| [First Contributions](https://firstcontributions.github.io/) | A safe practice repository |
| [Good First Issue](https://goodfirstissue.dev/) | Curated beginner-friendly issues |
| [Up For Grabs](https://up-for-grabs.net/) | Projects welcoming new contributors |
| [GitHub — Good first issue topic](https://github.com/topics/good-first-issue) | Browse labeled issues |
| [GitHub — Help wanted topic](https://github.com/topics/help-wanted) | Find projects that need help |

### A healthy first contribution

1. **Read the contribution guide.** It explains setup, tests, and communication norms.
2. **Start with documentation, tests, or a small bug.** Avoid redesigning the architecture in your first pull request.
3. **Comment on the issue before starting.** Confirm that the work is still needed and that your approach is welcome.
4. **Keep the change focused.** One problem per pull request.
5. **Run the project's checks.** Include the results in your pull request.
6. **Respond to review.** Review is a conversation about the code, not a judgment of you.
7. **Be patient.** Maintainers are often volunteers.

## Licensing

| Resource | Why it matters |
| --- | --- |
| [Choose a License](https://choosealicense.com/) | Plain-language comparison of common licenses |
| [Open Source Initiative — Licenses](https://opensource.org/licenses) | License list and definitions |
| [SPDX License List](https://spdx.org/licenses/) | Standard license identifiers |
| [GNU License List](https://www.gnu.org/licenses/license-list.html) | Free-license evaluation from the FSF |
| [Creative Commons — Choose a License](https://creativecommons.org/chooser/) | Licenses for non-code content |

**Key ideas:**

- A license tells others what they may do with your work.
- Public code without a license is not automatically open source.
- Changing a license affects the community's trust and legal rights.
- Dependencies have licenses too; check compatibility before distributing.
- Attribution requirements must be preserved.

## Starting and maintaining a project

| Resource | Why it helps |
| --- | --- |
| [Open Source Guides — Starting a Project](https://opensource.guide/starting-a-project/) | From idea to public repository |
| [Open Source Guides — Maintaining Balance](https://opensource.guide/maintaining-balance-for-open-source-maintainers/) | Sustainable maintainership |
| [GitHub — Setting up a project](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions) | README, license, contributing guide, and templates |
| [GitHub — Adding a code of conduct](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project) | Community expectations |
| [GitHub — Issue and pull request templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests) | Better reports and reviews |
| [Contributor Covenant](https://www.contributor-covenant.org/) | Widely adopted code of conduct |
| [Semantic Versioning](https://semver.org/) | Version numbers with meaning |
| [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) | Human-readable release notes |

### A minimal healthy repository

- `README.md` — what it does, how to install, how to use
- `LICENSE` — clear legal terms
- `CONTRIBUTING.md` — how to set up and contribute
- `CODE_OF_CONDUCT.md` — expected behavior
- `SECURITY.md` — private vulnerability reporting
- Issue and pull request templates
- CI checks for tests, linting, and builds
- Release notes and a changelog

## Security for open source

| Resource | Why it matters |
| --- | --- |
| [GitHub — Code Security](https://docs.github.com/en/code-security) | Dependabot, secret scanning, and code scanning |
| [GitHub — Security hardening for Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions) | Protect workflows and credentials |
| [OpenSSF — Best Practices](https://www.bestpractices.dev/en) | Secure software development guidance |
| [OWASP — Top Ten](https://owasp.org/projects/top-ten) | Common application security risks |
| [CWE Top 25](https://cwe.mitre.org/top25/) | Common software weaknesses |

**Never commit secrets.** If a credential is exposed, revoke it immediately, then remove it from history and rotate related credentials. Deleting the file alone is not enough.

## Community and governance

| Resource | Why it matters |
| --- | --- |
| [Open Source Guides](https://opensource.guide/) | A library of community leadership guides |
| [GitHub — Building communities](https://docs.github.com/en/communities) | Discussions, contributors, and moderation |
| [GitHub — Discussions quickstart](https://docs.github.com/en/discussions/quickstart) | Set up community conversations |
| [Open Source Guides — Leadership and Governance](https://opensource.guide/leadership-and-governance/) | Different project and governance models |
| [CHAOSS](https://www.chaoss.community/) | Community health metrics and practices |
| [GitHub — Community health files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file) | Default templates across repositories |

## Suggested learning sequence

1. **Learn Git basics:** status, add, commit, branch, merge, and log.
2. **Practice on your own repository.** Open a pull request and review it.
3. **Read a real project's contribution guide.** Notice how it communicates expectations.
4. **Make one small contribution.** Documentation, tests, or a focused bug fix.
5. **Learn licensing basics.** Understand what you are agreeing to.
6. **Contribute consistently.** Build relationships, not only commit counts.
7. **Maintain something small.** A resource list, a utility, or a community project.
8. **Learn security and release practices.** Protect users as your project grows.

## Avoid

- Opening a pull request before reading the contribution guide.
- Submitting mass, low-quality changes to many projects.
- Removing attribution or license notices.
- Pressuring maintainers for free labor or immediate reviews.
- Publishing a vulnerability before a fix is available.
- Measuring contribution only by commit count.
- Treating "open source" as "free labor."

---

**Related:** [Open-Source Guide](../community/OPEN_SOURCE_GUIDE.md) · [Collaboration Guide](../community/COLLABORATION_GUIDE.md) · [Learning Roadmaps](learning-roadmaps.md) · [Programming](programming.md) · [Web Development](web-development.md) · [AI & Machine Learning](artificial-intelligence.md) · [Contributing to DevSphere](../CONTRIBUTING.md) · [Collaboration discussions](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/collaboration)
