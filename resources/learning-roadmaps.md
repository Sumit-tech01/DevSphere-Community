# DevSphere Learning Roadmaps

Structured, project-based paths for ten developer roles. Each roadmap gives you a sequence to follow, the concepts that matter, official resources, projects that prove your understanding, and milestones that help you decide what to learn next.

> **Honest expectation:** a roadmap is a map, not a guarantee. Progress depends on your starting point, available time, previous experience, and the opportunities you can access. Nobody becomes job-ready by completing a checklist alone. Build projects, ask for feedback, and verify claims against current job descriptions.

## How to use these roadmaps

1. **Pick one path.** You can change later; switching every week prevents depth.
2. **Follow the sequence, not the clock.** Move on when you can explain and apply a concept, not when a calendar says so.
3. **Build after every stage.** Each roadmap includes project ideas that combine the concepts you just learned.
4. **Use the resource collections for depth.** The [programming](programming.md), [web development](web-development.md), [AI and machine learning](artificial-intelligence.md), [app development](app-development.md), [developer tools](developer-tools.md), [open source](open-source.md), and [career development](career-development.md) collections contain the full curated lists.
5. **Write down evidence.** Keep a short project README, a demo, and notes about trade-offs. A portfolio is evidence of thinking, not a collection of screenshots.
6. **Ask in the matching discussion.** Each roadmap links to a live DevSphere category where you can ask questions or share progress.

## Shared foundations

Everyone benefits from these foundations, even when a role does not list them again:

| Foundation | Why it matters | Start with |
| --- | --- | --- |
| Git and GitHub | Version control and collaboration are part of every role | [Pro Git](https://git-scm.com/book/en/v2) and [GitHub Skills](https://skills.github.com/) |
| Command line | Most developer tools are used from a terminal | [The Missing Semester](https://missing.csail.mit.edu/) |
| HTTP and the web | APIs, debugging, and deployment depend on it | [MDN — HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) |
| Testing | Confidence to change code without breaking it | [Software Testing Fundamentals](https://martinfowler.com/testing/) |
| Technical writing | READMEs, issues, reviews, and documentation are part of the work | [GitHub — Basic writing and formatting](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) |
| Security basics | Every application has a trust boundary | [OWASP Top Ten](https://owasp.org/projects/top-ten) |

---

## Frontend Developer

**Focus:** accessible, responsive interfaces that work across browsers and devices.

### Learning sequence

| Stage | Concepts | Resources |
| --- | --- | --- |
| 1. Web foundations | Semantic HTML, CSS layout, responsive design, browser rendering | [MDN — Learn Web Development](https://developer.mozilla.org/en-US/docs/Learn_web_development), [web.dev — Learn](https://web.dev/learn/) |
| 2. JavaScript | Types, functions, scope, modules, events, asynchronous code, the DOM | [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide), [JavaScript.info](https://javascript.info/) |
| 3. TypeScript | Structural typing, narrowing, generics, configuration | [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) |
| 4. React | Components, props, state, effects, rendering, composition | [React — Learn](https://react.dev/learn) |
| 5. Next.js | Routing, layouts, rendering modes, data fetching, metadata | [Next.js — Learn](https://nextjs.org/learn), [Next.js documentation](https://nextjs.org/docs) |
| 6. Quality | Accessibility, performance, testing, error and loading states | [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [web.dev — Learn Performance](https://web.dev/learn/performance), [Testing Library](https://testing-library.com/docs/) |
| 7. Delivery | Build tooling, deployment, observability, rollback | [Vite guide](https://vite.dev/guide/), [GitHub Pages](https://docs.github.com/en/pages), [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) |

### Projects

- Build a responsive profile card or landing page using semantic HTML and modern CSS.
- Build a searchable dashboard that consumes a public API and handles loading, empty, error, and success states.
- Build a multi-page React or Next.js application with routing, forms, validation, and accessible components.
- Audit an existing site for keyboard access, contrast, focus visibility, responsive behavior, and Core Web Vitals, then document the fixes.

### Milestones

- [ ] I can build a responsive page without horizontal scrolling at 320px and 1440px.
- [ ] I can explain state, props, effects, and rendering without relying on memorized snippets.
- [ ] I can add TypeScript to a real project and remove unexplained `any` types.
- [ ] I can test a component's behavior and catch a regression before deploying.
- [ ] I can explain the accessibility and performance trade-offs in one of my projects.
- [ ] I have deployed at least one project and documented how to run it locally.

**Discuss:** [Web Development](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/web-development) · **Resources:** [Web development collection](web-development.md)

---

## Backend Developer

**Focus:** reliable APIs, data models, authentication boundaries, and services that are understandable to operate.

### Learning sequence

| Stage | Concepts | Resources |
| --- | --- | --- |
| 1. Language foundation | One backend language, data structures, error handling, package management | [Python tutorial](https://docs.python.org/3/tutorial/), [Node.js Learn](https://nodejs.org/learn), or [Dev.java — Learn](https://dev.java/learn/) |
| 2. HTTP and APIs | Methods, status codes, headers, idempotency, pagination, versioning | [MDN — HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP), [OpenAPI specification](https://spec.openapis.org/oas/latest.html) |
| 3. Web framework | Routing, validation, middleware, dependency injection, error responses | [Express](https://expressjs.com/), [Fastify](https://fastify.dev/docs/latest/), or [FastAPI](https://fastapi.tiangolo.com/) |
| 4. Databases | Relational modeling, SQL, indexes, transactions, migrations | [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html), [SQLBolt](https://sqlbolt.com/) |
| 5. Security | Authentication, authorization, input validation, secrets, rate limits | [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) |
| 6. Testing and operations | Unit and integration tests, containers, logs, health checks, configuration | [Docker — Get started](https://docs.docker.com/get-started/), [Node.js test runner](https://nodejs.org/api/test.html), [The Twelve-Factor App](https://12factor.net/) |
| 7. Design | Caching, queues, idempotency, failure modes, observability | [System Design Primer](https://github.com/donnemartin/system-design-primer) |

### Projects

- Build a REST API with validation, structured errors, pagination, and integration tests.
- Add a database with migrations, indexes, and a transaction that protects an invariant.
- Implement session or token authentication with clear authorization rules and audit logging.
- Add a background job, a retry policy, and a dead-letter path for failed work.
- Containerize the service and document configuration, health checks, and rollback.

### Milestones

- [ ] I can design a small schema and explain its relationships and indexes.
- [ ] I can write an API contract before implementing it.
- [ ] I can test success, validation failure, authorization failure, and server failure paths.
- [ ] I can explain how secrets are stored and rotated.
- [ ] I can debug a slow query or a failing request using evidence, not guesses.
- [ ] I can operate my service locally with one documented command.

**Discuss:** [Programming](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/programming) or [Web Development](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/web-development)

---

## Full-Stack Developer

**Focus:** connecting user experience, APIs, data, authentication, and deployment without losing maintainability.

### Learning sequence

| Stage | Concepts | Resources |
| --- | --- | --- |
| 1. Web fundamentals | HTML, CSS, JavaScript, HTTP, accessible forms | [MDN — Learn Web Development](https://developer.mozilla.org/en-US/docs/Learn_web_development) |
| 2. Frontend application | Components, state, routing, data fetching, error states | [React — Learn](https://react.dev/learn), [Next.js — Learn](https://nextjs.org/learn) |
| 3. Backend | Routes, validation, business logic, database access, tests | [Node.js Learn](https://nodejs.org/learn), [FastAPI](https://fastapi.tiangolo.com/) |
| 4. Data | Schema design, SQL, migrations, indexes, transactions | [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html), [SQLBolt](https://sqlbolt.com/) |
| 5. Identity and security | Sessions, OAuth concepts, authorization, CSRF, secrets | [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) |
| 6. Quality | TypeScript, testing, accessibility, performance budgets | [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html), [Testing Library](https://testing-library.com/docs/) |
| 7. Delivery | CI, deployment, environment configuration, logs, rollback | [GitHub Actions](https://docs.github.com/en/actions), [Docker — Get started](https://docs.docker.com/get-started/) |

### Projects

- Build a full-stack application with authentication, a relational database, and role-based permissions.
- Add server-side validation and client-side feedback for every form.
- Add an audit trail for a sensitive action and document who can see it.
- Write a deployment guide that another person can follow without asking you questions.
- Perform a security and accessibility review, then fix one issue in each area.

### Milestones

- [ ] I can trace a feature from a user interaction through the API to the database and back.
- [ ] I can explain where authorization is enforced and why the client is not trusted.
- [ ] I can write a migration without losing existing data.
- [ ] I can test the critical path and at least one failure path end to end.
- [ ] I can deploy a change and roll it back.
- [ ] I can explain the architecture of my project in five minutes.

**Discuss:** [Web Development](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/web-development)

---

## AI Engineer

**Focus:** building useful AI-powered applications with retrieval, tools, evaluation, safety, and cost awareness.

### Learning sequence

| Stage | Concepts | Resources |
| --- | --- | --- |
| 1. Python and data | Virtual environments, APIs, JSON, async requests, data inspection | [Python tutorial](https://docs.python.org/3/tutorial/), [pandas — Getting started](https://pandas.pydata.org/docs/getting_started/index.html) |
| 2. ML foundations | Supervised learning, validation, metrics, overfitting, baselines | [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course), [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html) |
| 3. LLM APIs | Messages, tokens, context windows, structured output, tool use | [OpenAI API documentation](https://developers.openai.com/api/docs), [Gemini API documentation](https://aistudio.google.com/docs), [Claude documentation](https://platform.claude.com/docs/en/home) |
| 4. Prompting and agents | Instructions, examples, decomposition, tool schemas, failure handling | [Prompt Engineering Guide](https://www.promptingguide.ai/), [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction) |
| 5. Retrieval | Chunking, embeddings, vector search, citations, access control | [LangChain overview](https://docs.langchain.com/oss/python/langchain/overview), [Sentence Transformers](https://sbert.net/), [Faiss](https://faiss.ai/) |
| 6. Evaluation | Gold sets, retrieval metrics, answer quality, regression tests | [Hugging Face Evaluate](https://huggingface.co/docs/evaluate/index) |
| 7. Production | Latency, cost, monitoring, privacy, human review, fallbacks | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), [MLflow](https://mlflow.org/docs/latest/index.html) |

### Projects

- Build a retrieval-augmented assistant over documents you have permission to use. Cite sources and refuse when evidence is missing.
- Create an evaluation set with at least 30 realistic questions. Compare two retrieval or prompting strategies.
- Build a tool-using assistant with explicit permissions, input validation, and a safe failure path.
- Add a cost and latency dashboard for every model call, including token usage and retries.
- Write a threat model covering prompt injection, data leakage, and unsafe tool use.

### Milestones

- [ ] I can explain why an LLM response is not evidence by itself.
- [ ] I can separate retrieval quality from answer quality in an evaluation.
- [ ] I can prevent a tool call from exceeding the user's authority.
- [ ] I can estimate the cost of a request before shipping it.
- [ ] I can document known failure cases and the fallback behavior.
- [ ] I have built one AI application that a non-author can run from the README.

**Discuss:** [AI & Machine Learning](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/ai-machine-learning) · **Resources:** [AI and machine learning collection](artificial-intelligence.md)

---

## Machine Learning Engineer

**Focus:** training, evaluating, packaging, and operating models with reproducible engineering practices.

### Learning sequence

| Stage | Concepts | Resources |
| --- | --- | --- |
| 1. Mathematics | Linear algebra, probability, optimization, notation | [Mathematics for Machine Learning](https://mml-book.github.io/), [MIT linear algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) |
| 2. Python and data | NumPy, pandas, visualization, reproducible notebooks | [NumPy beginner guide](https://numpy.org/doc/stable/user/absolute_beginners.html), [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) |
| 3. Classical ML | Baselines, cross-validation, leakage, metrics, error analysis | [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html), [StatLearning](https://www.statlearning.com/) |
| 4. Deep learning | Tensors, autograd, training loops, regularization, transfer learning | [PyTorch basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html), [Dive into Deep Learning](https://d2l.ai/) |
| 5. Experimentation | Tracking, data versioning, model comparison, reproducibility | [MLflow](https://mlflow.org/docs/latest/index.html), [DVC](https://doc.dvc.org) |
| 6. Deployment | Model serving, batching, latency, monitoring, drift, rollback | [Full Stack Deep Learning](https://fullstackdeeplearning.com/course/), [MLOps Guide](https://mlops-guide.github.io/) |
| 7. Responsible engineering | Privacy, bias, documentation, human oversight | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) |

### Projects

- Build a tabular ML pipeline with a baseline, validation strategy, error analysis, and model card.
- Train an image or text classifier with a reproducible training command and fixed seeds.
- Serve a model behind an API with input validation, batching, timeouts, and monitoring.
- Reproduce one published result or benchmark and document every difference.
- Compare two models on cost, latency, and failure modes, not only accuracy.

### Milestones

- [ ] I can explain the difference between training, validation, and test data.
- [ ] I can detect and fix data leakage in a pipeline.
- [ ] I can reproduce a training run from a clean environment.
- [ ] I can explain a model's limitations to a non-specialist.
- [ ] I can monitor a deployed model for drift and bad inputs.
- [ ] I can document data provenance and licensing constraints.

**Discuss:** [AI & Machine Learning](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/ai-machine-learning)

---

## Data Scientist

**Focus:** turning messy data into defensible analysis, models, and decisions.

### Learning sequence

| Stage | Concepts | Resources |
| --- | --- | --- |
| 1. Statistics | Distributions, sampling, uncertainty, hypothesis tests, causal caution | [Seeing Theory](https://seeing-theory.brown.edu/), [StatQuest](https://statquest.org/) |
| 2. Python for data | pandas, NumPy, cleaning, joins, missing data, reproducible analysis | [pandas documentation](https://pandas.pydata.org/docs/), [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) |
| 3. SQL | SELECT, joins, aggregation, window functions, query performance | [SQLBolt](https://sqlbolt.com/), [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html) |
| 4. Visualization | Chart choice, uncertainty, accessibility, misleading graphs | [seaborn](https://seaborn.pydata.org/), [Matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html) |
| 5. Modeling | Baselines, feature engineering, validation, metrics, error analysis | [scikit-learn](https://scikit-learn.org/stable/), [StatLearning](https://www.statlearning.com/) |
| 6. Experimentation | A/B tests, power, guardrail metrics, practical significance | [How Not to Run an A/B Test](https://www.evanmiller.org/how-not-to-run-an-ab-test.html), [Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml) |
| 7. Communication | Executive summaries, limitations, decision memos, reproducibility | [Google Technical Development Guide](https://www.google.com/about/careers/applications/buildyourfuture/resources/) |

### Projects

- Clean a messy public dataset and document every assumption, exclusion, and missing-value decision.
- Build a dashboard or report that answers one decision question and clearly shows uncertainty.
- Analyze an A/B test with a pre-registered metric, guardrails, and a practical-significance discussion.
- Build a predictive model and write a one-page decision memo for a non-technical stakeholder.
- Reproduce your analysis from raw data with a single documented command.

### Milestones

- [ ] I can explain a confidence interval without using jargon incorrectly.
- [ ] I can join and aggregate data in SQL without exporting everything to a spreadsheet.
- [ ] I can identify a misleading chart and fix it.
- [ ] I can separate correlation from a causal claim.
- [ ] I can explain model errors by segment rather than only reporting one score.
- [ ] I can present a recommendation with assumptions, risks, and next steps.

**Discuss:** [AI & Machine Learning](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/ai-machine-learning)

---

## Python Developer

**Focus:** readable, tested Python for automation, APIs, data work, and maintainable tools.

### Learning sequence

| Stage | Concepts | Resources |
| --- | --- | --- |
| 1. Language fundamentals | Types, control flow, functions, classes, exceptions, comprehensions | [The Python Tutorial](https://docs.python.org/3/tutorial/) |
| 2. Standard library | Paths, dates, JSON, collections, iterators, subprocess, logging | [Python standard library](https://docs.python.org/3/library/) |
| 3. Project structure | Virtual environments, packages, modules, configuration, entry points | [Python Packaging User Guide](https://packaging.python.org/en/latest/) |
| 4. Testing and quality | pytest, fixtures, mocking boundaries, type hints, linting | [pytest documentation](https://docs.pytest.org/en/stable/), [typing documentation](https://docs.python.org/3/library/typing.html) |
| 5. Application layer | CLI design, HTTP clients, API services, database access | [FastAPI](https://fastapi.tiangolo.com/), [HTTPX](https://www.python-httpx.org/) |
| 6. Data and automation | pandas, file processing, scheduling, error recovery | [pandas — Getting started](https://pandas.pydata.org/docs/getting_started/index.html) |
| 7. Delivery | Packaging, containers, CI, logging, observability | [Docker — Get started](https://docs.docker.com/get-started/), [GitHub Actions](https://docs.github.com/en/actions) |

### Projects

- Build a CLI that validates and transforms a CSV file, with helpful errors and tests.
- Build a small API with typed request models, validation, structured errors, and tests.
- Automate a repetitive local workflow with safe defaults, logging, and a dry-run mode.
- Package a reusable library with a README, tests, and a changelog.
- Add CI that runs tests and linting on every pull request.

### Milestones

- [ ] I can structure a project so imports work outside my editor.
- [ ] I can write tests for success, failure, and boundary cases.
- [ ] I can explain the difference between a package, a module, and a script.
- [ ] I can handle secrets and configuration without hard-coding them.
- [ ] I can profile a slow function before optimizing it.
- [ ] I can publish or share a tool with setup instructions another person can follow.

**Discuss:** [Programming](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/programming)

---

## Mobile App Developer

**Focus:** shipping a reliable mobile product with platform-appropriate interaction, performance, accessibility, and release practices.

### Learning sequence

| Stage | Concepts | Resources |
| --- | --- | --- |
| 1. Choose a path | Native Android, native iOS, Flutter, or React Native | [Android get started](https://developer.android.com/get-started), [Apple SwiftUI tutorials](https://developer.apple.com/tutorials/swiftui), [Flutter](https://docs.flutter.dev/), [React Native](https://reactnative.dev/docs/getting-started) |
| 2. Language and UI | Layout, navigation, state, lists, forms, theming, accessibility | [Dart documentation](https://dart.dev/docs), [React Native tutorial](https://reactnative.dev/docs/tutorial), [Expo tutorial](https://docs.expo.dev/tutorial/introduction/) |
| 3. Data and offline behavior | API calls, local storage, caching, sync, conflict handling | [Flutter learning pathway](https://docs.flutter.dev/learn/pathway), [Expo documentation](https://docs.expo.dev/) |
| 4. Platform quality | Permissions, notifications, deep links, battery, accessibility | [Android design](https://developer.android.com/design), [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) |
| 5. Testing | Unit tests, widget/component tests, device testing, crash reporting | [Flutter testing](https://docs.flutter.dev/testing), [Expo unit testing](https://docs.expo.dev/develop/unit-testing/) |
| 6. Release | Signing, versioning, store metadata, staged rollout, rollback | [Android publishing](https://developer.android.com/studio/publish), [App Store](https://developer.apple.com/app-store/) |

### Projects

- Build a habit tracker with local persistence, empty states, and accessible controls.
- Build an offline-first notes app that syncs when connectivity returns and handles conflicts.
- Build an app that consumes a public API, caches results, and explains failures to the user.
- Test on a small screen, a large screen, and with large text enabled.
- Prepare a release checklist and a privacy explanation for the data your app collects.

### Milestones

- [ ] I can explain the platform's navigation and lifecycle model.
- [ ] I can handle loading, empty, error, and offline states.
- [ ] I can ask for permissions only when needed and explain why.
- [ ] I can test the critical path on a real or emulated device.
- [ ] I can produce a signed build and follow store requirements.
- [ ] I can explain my app's data collection and retention behavior.

**Discuss:** [App Development](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/app-development) · **Resources:** [App development collection](app-development.md)

---

## DevOps Engineer

**Focus:** reproducible environments, safe delivery, and observable systems.

### Learning sequence

| Stage | Concepts | Resources |
| --- | --- | --- |
| 1. Linux and networking | Processes, permissions, filesystems, DNS, TCP/IP, SSH, logs | [The Missing Semester](https://missing.csail.mit.edu/), [Ubuntu tutorials](https://ubuntu.com/tutorials), [Bash manual](https://www.gnu.org/software/bash/manual/) |
| 2. Version control | Branching, review, tags, release notes, rollback | [Pro Git](https://git-scm.com/book/en/v2), [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow) |
| 3. Containers | Images, layers, volumes, networks, Compose, registries | [Docker — Get started](https://docs.docker.com/get-started/), [Docker Compose](https://docs.docker.com/compose/) |
| 4. Cloud fundamentals | Identity, networking, storage, compute, cost, least privilege | [AWS documentation](https://docs.aws.amazon.com/), [Azure documentation](https://learn.microsoft.com/en-us/azure/), [Google Cloud documentation](https://docs.cloud.google.com/docs) |
| 5. Infrastructure as code | Declarative resources, state, plans, drift, review | [Terraform documentation](https://developer.hashicorp.com/terraform/docs) |
| 6. CI/CD | Build, test, artifacts, environments, approvals, secrets | [GitHub Actions](https://docs.github.com/en/actions) |
| 7. Operations | Metrics, logs, traces, alerts, incident review, security | [OpenSSF Best Practices](https://www.bestpractices.dev/en), [OWASP Top Ten](https://owasp.org/projects/top-ten) |

### Projects

- Containerize an application with a minimal image, health check, and documented configuration.
- Build a CI pipeline that runs tests and linting, then publishes a build artifact.
- Write infrastructure as code for a small environment and review the plan before applying it.
- Create a runbook for a failed deployment, including detection, rollback, and communication.
- Add structured logs and one meaningful alert with a clear owner.

### Milestones

- [ ] I can explain what happens between `git push` and a deployed change.
- [ ] I can keep secrets out of source control and rotate a leaked credential.
- [ ] I can reproduce a service locally with one documented command.
- [ ] I can review an infrastructure plan and identify destructive changes.
- [ ] I can diagnose a failure from logs and metrics rather than guessing.
- [ ] I can write a rollback plan before shipping a risky change.

**Discuss:** [Programming](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/programming) · **Resources:** [Developer tools collection](developer-tools.md)

---

## Open-Source Contributor

**Focus:** making useful, respectful contributions and becoming a reliable collaborator.

### Learning sequence

| Stage | Concepts | Resources |
| --- | --- | --- |
| 1. Git and GitHub | Fork, clone, branch, commit, push, pull request, review | [Pro Git](https://git-scm.com/book/en/v2), [GitHub Skills](https://skills.github.com/) |
| 2. Project selection | License, activity, contribution guide, communication channels | [Open Source Guides — How to Contribute](https://opensource.guide/how-to-contribute/) |
| 3. First issue | Good-first-issue labels, scope, reproduction, acceptance criteria | [Good First Issue](https://goodfirstissue.dev/), [Up For Grabs](https://up-for-grabs.net/), [GitHub good-first-issue topic](https://github.com/topics/good-first-issue) |
| 4. Make the change | Small commits, tests, documentation, local verification | [GitHub — Contributing to a project](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project) |
| 5. Open the pull request | Clear title, context, linked issue, screenshots, test evidence | [GitHub — About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) |
| 6. Review and iterate | Respond to feedback, resolve threads, keep scope small | [GitHub — Reviewing changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests) |
| 7. Maintain | Triage, review, releases, security, contributor care | [Open Source Guides — Starting a Project](https://opensource.guide/starting-a-project/), [Maintaining Balance](https://opensource.guide/maintaining-balance-for-open-source-maintainers/) |

### Projects

- Make a documentation or typo fix in a project you use, following its contribution guide.
- Fix a small reproducible bug and add a regression test.
- Review another contributor's pull request with specific, kind questions.
- Improve a README so a new contributor can set up the project without help.
- Maintain a small repository with a license, contributing guide, issue template, and CI.

### Milestones

- [ ] I have read a project's contribution guide before opening a pull request.
- [ ] I can keep a pull request focused on one problem.
- [ ] I can explain my change and its trade-offs in the description.
- [ ] I can respond to review feedback without taking it personally.
- [ ] I understand the project's license and attribution requirements.
- [ ] I have helped someone else make their first contribution.

**Discuss:** [Collaboration](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/collaboration) · **Guides:** [Open-source guide](../community/OPEN_SOURCE_GUIDE.md), [Open-source resources](open-source.md)

---

## Choosing between similar paths

| If you enjoy... | Consider... |
| --- | --- |
| Interfaces, interaction, accessibility, visual systems | Frontend |
| APIs, data models, reliability, performance | Backend |
| Owning a feature end to end | Full-stack |
| LLM applications, retrieval, evaluation, product behavior | AI Engineer |
| Training models, experiments, deployment, reproducibility | ML Engineer |
| Statistics, analysis, decisions, communication | Data Scientist |
| Automation, tooling, readable scripts, APIs | Python Developer |
| Mobile interaction, offline behavior, release cycles | Mobile App Developer |
| Systems, automation, reliability, security | DevOps |
| Collaboration, documentation, community maintenance | Open-Source Contributor |

You do not need a new roadmap for every framework. Learn the underlying concepts, then read the framework's official documentation when you adopt it.

## What these roadmaps deliberately avoid

- Promising a job, salary, or timeframe.
- Requiring paid courses, certificates, or bootcamps.
- Treating one framework as a complete education.
- Measuring progress by the number of links collected.
- Recommending tools without explaining what problem they solve.
- Hiding the need for communication, testing, accessibility, and security.

---

**Related:** [Resource index](README.md) · [Programming](programming.md) · [Web development](web-development.md) · [AI and machine learning](artificial-intelligence.md) · [App development](app-development.md) · [Developer tools](developer-tools.md) · [Career development](career-development.md) · [Open source](open-source.md)
