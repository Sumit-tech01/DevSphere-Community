# Developer Tools & APIs

A practical toolkit for writing code, collaborating, testing APIs, working with containers, and operating software. The focus is on tools with official documentation you can learn from without buying a course.

> **Status labels:** **Free** means the linked documentation or core tool is free to access. **Free + paid** means a free plan or core exists and optional paid plans are also offered. **Docs free; usage billed** means the documentation is free but the service itself may charge for usage. Verify current terms on the official page before relying on a free tier.

## Start with the essentials

| Tool | What it helps you do | Status | Start here |
| --- | --- | --- | --- |
| **Git** | Track changes and work safely across branches | Free | [Pro Git](https://git-scm.com/book/en/v2), [Git reference](https://git-scm.com/docs) |
| **GitHub** | Host repositories, review code, and collaborate | Free + paid | [GitHub documentation](https://docs.github.com/en), [GitHub Skills](https://skills.github.com/) |
| **VS Code** | Edit, debug, and extend your development workflow | Free | [VS Code documentation](https://code.visualstudio.com/docs) |
| **Terminal** | Run tools, automate tasks, and inspect systems | Free | [The Missing Semester](https://missing.csail.mit.edu/) |
| **Docker** | Build reproducible containers and development environments | Free + paid | [Docker — Get started](https://docs.docker.com/get-started/) |
| **Postman** | Explore, test, and document HTTP APIs | Free + paid | [Postman learning center](https://learning.postman.com/docs/getting-started/overview/) |
| **Figma** | Design interfaces and collaborate on product flows | Free + paid | [Figma help center](https://help.figma.com/hc/en-us) |
| **OpenAPI** | Describe HTTP APIs in a machine-readable contract | Free | [OpenAPI specification](https://spec.openapis.org/oas/latest.html) |

## Git and GitHub

Git is the version-control system; GitHub is a hosting and collaboration platform built around it. Learn Git locally before relying on a graphical client.

| Resource | Level | Notes |
| --- | --- | --- |
| [Pro Git](https://git-scm.com/book/en/v2) | Beginner–Advanced | The complete free Git book |
| [Git reference](https://git-scm.com/docs) | All | Official command documentation |
| [GitHub documentation](https://docs.github.com/en) | All | Official platform documentation |
| [GitHub Skills](https://skills.github.com/) | Beginner | Interactive courses that run in a repository |
| [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow) | Beginner | A lightweight branch-and-pull-request workflow |
| [GitHub CLI manual](https://cli.github.com/manual/) | Intermediate | Use GitHub from the terminal |
| [GitHub CLI documentation](https://docs.github.com/en/get-started/using-github/github-cli) | Intermediate | Authentication, repositories, issues, and pull requests |
| [Conventional Commits](https://www.conventionalcommits.org/) | Intermediate | An optional commit-message convention |
| [Learn Git Branching](https://learngitbranching.js.org/) | Beginner–Intermediate | Visual, interactive branching practice |
| [Oh My Git!](https://ohmygit.org/) | Beginner | An open-source game for learning Git |

**Practice:** create a repository, make a branch, commit a small change, open a pull request against your own `main`, request changes, and merge. Repeat until the workflow feels ordinary.

For a deeper open-source workflow, see the [open-source collection](open-source.md) and the [DevSphere open-source guide](../community/OPEN_SOURCE_GUIDE.md).

## Editors and local development

| Resource | Why it helps |
| --- | --- |
| [VS Code documentation](https://code.visualstudio.com/docs) | Setup, editing, debugging, terminals, and extensions |
| [VS Code FAQ](https://code.visualstudio.com/docs/supporting/faq) | Common installation and configuration questions |
| [The Missing Semester](https://missing.csail.mit.edu/) | Shell, scripting, editors, version control, and debugging |
| [GitHub Pages](https://pages.github.com/) | Publish a static portfolio or project site; free for public repositories |
| [GitHub Actions](https://docs.github.com/en/actions) | Automate tests, builds, and validation |
| [Markdown Guide](https://www.markdownguide.org/) | Write readable README files and documentation |
| [GitHub writing and formatting](https://docs.github.com/en/get-started/writing-on-github) | GitHub-flavored Markdown and collaboration features |

**Workflow idea:** keep one repository with a `README.md`, a reproducible setup command, a test command, and a CI workflow. This is more valuable than a long list of editor extensions.

## Containers

| Resource | Level | Notes |
| --- | --- | --- |
| [Docker — Get started](https://docs.docker.com/get-started/) | Beginner | Images, containers, and the core workflow |
| [Docker Compose](https://docs.docker.com/compose/) | Intermediate | Multi-service local environments |
| [Docker documentation](https://docs.docker.com/) | All | Official reference and guides |
| [Docker pricing](https://www.docker.com/pricing/) | All | Compare free and paid product terms |

**Practice:** containerize a small API and a database with Compose. Add a health check, a named volume, and a documented command that works from a clean checkout.

Do not use containers to hide setup problems. Write down the configuration, ports, environment variables, and data volumes.

## API testing and design

| Resource | Level | Notes |
| --- | --- | --- |
| [Postman learning center](https://learning.postman.com/docs/getting-started/overview/) | Beginner | Requests, collections, environments, and tests |
| [Postman pricing](https://www.postman.com/pricing/) | All | Compare free and paid plans |
| [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) | Beginner–Intermediate | Methods, headers, status codes, caching |
| [OpenAPI specification](https://spec.openapis.org/oas/latest.html) | Intermediate | Contract-first API design |
| [HTTPie CLI documentation](https://httpie.io/docs/cli) | Beginner | A readable command-line HTTP client |
| [curl documentation](https://curl.se/docs/) | Beginner–Advanced | The widely available transfer tool |
| [jq manual](https://jqlang.org/manual/) | Intermediate | Query and transform JSON in the terminal |

**Practice:** describe a small API in OpenAPI, implement it, test success and failure responses, and save a reusable request collection. Never commit real tokens or production credentials.

## Design and product collaboration

| Resource | Level | Notes |
| --- | --- | --- |
| [Figma help center](https://help.figma.com/hc/en-us) | Beginner | Files, frames, components, prototyping, and collaboration |
| [Figma pricing](https://www.figma.com/pricing/) | All | Compare free and paid plans |
| [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) | Intermediate | Platform interaction and visual guidance |
| [Android design](https://developer.android.com/design) | Intermediate | Android design and material guidance |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | All | Accessibility requirements for web interfaces |
| [Inclusive Components](https://inclusive-components.design/) | Intermediate | Accessible UI patterns |

Designers and developers collaborate better with shared constraints. Document breakpoints, states, empty cases, error messages, keyboard behavior, and content limits before implementation.

## Linux and the command line

| Resource | Level | Notes |
| --- | --- | --- |
| [The Missing Semester](https://missing.csail.mit.edu/) | Beginner | Practical shell and tooling skills |
| [Ubuntu tutorials](https://ubuntu.com/tutorials) | Beginner | Common Linux setup and server tasks |
| [The Linux Command Line](https://linuxcommand.org/tlcl.php) | Beginner–Intermediate | A free book for command-line fundamentals |
| [Bash manual](https://www.gnu.org/software/bash/manual/) | Intermediate | Official shell reference |
| [Linux kernel documentation](https://www.kernel.org/doc/html/latest/) | Advanced | Kernel and subsystem documentation |

**Practice:** learn `pwd`, `ls`, `cd`, `cp`, `mv`, `rm`, `grep`, `find`, `sed`, `awk`, `xargs`, `chmod`, `ps`, `top`, `df`, `curl`, and `ssh`. Understand a command before copying it from the internet.

## Cloud platforms

Cloud documentation is free; the services you create may not be. Always check the provider's current pricing, free-tier limits, and region availability before deploying.

| Platform | Start here | What to learn first |
| --- | --- | --- |
| **Amazon Web Services** | [AWS documentation](https://docs.aws.amazon.com/) | IAM, regions, networking, storage, compute, billing |
| **Microsoft Azure** | [Azure documentation](https://learn.microsoft.com/en-us/azure/) | Subscriptions, identity, resource groups, networking, cost |
| **Google Cloud** | [Google Cloud documentation](https://docs.cloud.google.com/docs) | Projects, IAM, networking, storage, compute, budgets |

**Safety checklist before creating a resource:**

- [ ] I know which account and project will be billed.
- [ ] I understand the region and data-residency implications.
- [ ] I have a budget or alert, if available.
- [ ] I know how to delete the resource.
- [ ] I have not committed credentials or service-account keys.
- [ ] I have checked whether a local or free alternative is sufficient.

## Open-source utilities

| Tool | Use | Resource |
| --- | --- | --- |
| **GitHub CLI** | Repositories, issues, pull requests, and Actions from the terminal | [Manual](https://cli.github.com/manual/) |
| **curl** | HTTP requests and API debugging | [Documentation](https://curl.se/docs/) |
| **jq** | JSON filtering and transformation | [Manual](https://jqlang.org/manual/) |
| **ripgrep** | Fast code and text search | [Repository](https://github.com/BurntSushi/ripgrep) |
| **HTTPie** | Human-friendly HTTP requests | [Documentation](https://httpie.io/docs/cli) |
| **GitHub Actions** | CI, validation, and release automation | [Documentation](https://docs.github.com/en/actions) |

## A sensible starter toolkit

1. **Editor:** VS Code, with only the extensions you can explain.
2. **Terminal:** a shell you understand and a prompt that shows the current directory and Git branch.
3. **Version control:** Git locally, GitHub remotely, and a signed-in GitHub CLI for repetitive work.
4. **Runtime manager:** the official version manager for your language, so projects can pin versions.
5. **Containers:** Docker only when the project needs reproducible services or deployment parity.
6. **API client:** Postman or HTTPie, plus `curl` for sharing reproducible requests.
7. **Documentation:** a README that explains setup, tests, architecture, and known limitations.
8. **CI:** one workflow that runs the checks you actually trust.

## Avoid

- Installing tools because a video thumbnail told you to.
- Copying shell commands without understanding destructive flags.
- Committing `.env` files, tokens, private keys, or cloud credentials.
- Treating a free trial as a permanent free service.
- Using a container image you have not inspected or trusted.
- Adding an extension that can read your entire workspace without checking its permissions.
- Assuming a tool is secure because it is popular.

---

**Related:** [Programming](programming.md) · [Web development](web-development.md) · [Open source](open-source.md) · [AI and machine learning](artificial-intelligence.md) · [Programming discussions](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/programming)
