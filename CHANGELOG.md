# Changelog

All notable changes to the DevSphere community repository are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project follows [Semantic Versioning](https://semver.org/) for community infrastructure releases.

## [Unreleased]

### Added

- A complete Developer Spotlight and Community Recognition framework with objectives, eligibility, selection criteria, invitation and interview stages, permission rules, publishing guidance, corrections, removal, and a 13-question FAQ.
- `community/templates/DEVELOPER_SPOTLIGHT_TEMPLATE.md` with the full 17-section interview and permission form, optional-question guidance, and a maintainer checklist.
- `community/templates/DEVELOPER_NOMINATION_TEMPLATE.md` supporting self-nominations, nominations with permission, open-source contributors, students, independent builders, innovative project creators, and community helpers.
- `community/COMMUNITY_INITIATIVES.md` documenting Developer Spotlight (weekly slot), Project Review Friday (weekly), Builder of the Month (monthly), and Community Collaboration (ongoing), including schedules, discussion formats, moderation rules, accessibility, and privacy.
- `community/BUILDERS_OF_THE_MONTH.md` with the monthly recognition process, consent rules, recognition format, and an archive that starts with no invented recipients.
- `community/templates/PROJECT_REVIEW_TEMPLATE.md` with a submission form, reviewer response format, host checklist, and privacy checks for Project Review Friday.
- Five ready-to-publish recognition discussion drafts under `community/discussions/recognition/`, with titles, full Markdown bodies, existing discussion categories, suggested schedules, labels, and a manual publishing checklist.
- `community/launch/` with the first campaign's community announcement, founder introduction, first Spotlight invitation round, first Project Review Friday session, LinkedIn announcement, and publishing-order checklist.
- `community/PROJECT_DISCOVERY.md` and `community/templates/PROJECT_DISCOVERY_SUBMISSION.md` for open-source projects, developer tools, AI applications, web apps, mobile apps, and learning resources, including link verification, spam prevention, copyright, privacy, and affiliation disclosure.
- A consent-first private outreach policy and reusable invitation template under `community/outreach/`, with candidate-specific drafts kept out of the published repository so no one is named before accepting.
- A `🌟 Developer Spotlight` section in the root README with the program introduction, recognition criteria, nomination instructions, participation guidelines, and links to the handbook, templates, and discussion categories.

### Changed

- Renamed the "Best Open-Source Contribution" category to "Open-Source Contribution" so recognition does not imply a ranking.
- Reconciled the weekly activity calendar with Project Review Friday and added Builder of the Month and Community Collaboration to the monthly/ongoing rhythm.
- Added recognition labels (`spotlight`, `nomination`, `recognition`, `project-review`, `builder-of-the-month`) to the documented label set.
- Connected the resource index, resource submission process, template index, discussion index, launch playbook, and community roadmap to the new recognition and discovery documents.
- Added the Builders of the Month archive, Project Review template, and campaign launch kit to the README's recognition resources and the community activity guides.
- Updated repository validation to require the new files, check recognition draft metadata and categories, validate discussion category URLs, and verify template completeness.

### Planned

- Additional coding challenges with community-reviewed solutions.
- Expanded accessibility guidance for contributor-facing documents.
- Community-led activity reports when recurring formats have real participation.
- Verified developer spotlights when nominations and consent exist.
- Discussion category refinements based on community feedback.

## [2.0.0] - 2026-11-03

### Added

- A rebuilt 20-section README in the required order: hero, introduction, join, benefits, resource hub, roadmaps, AI/ML, web/app, tools/APIs, open source, showcase, collaborators, challenges, opportunities, events, spotlight, discussions, contribution, founder, and join CTA.
- `resources/learning-roadmaps.md` with ten role-based roadmaps: Frontend, Backend, Full-Stack, AI Engineer, ML Engineer, Data Scientist, Python Developer, Mobile App Developer, DevOps Engineer, and Open-Source Contributor.
- `resources/app-development.md` covering Android, iOS, Flutter, React Native, Expo, testing, accessibility, and release practices.
- `resources/developer-tools.md` covering Git, GitHub, editors, containers, API testing, design, Linux, cloud platforms, and open-source utilities.
- `resources/career-development.md` covering portfolios, resumes, interviews, data structures and algorithms, internships, open source as evidence, and job-search safety.
- `community/COLLABORATION_GUIDE.md` with paid, unpaid, voluntary, equity, and open-source collaboration models.
- `community/OPEN_SOURCE_GUIDE.md` with the contribution workflow, review expectations, maintainership, and security guidance.
- `community/DEVELOPER_SPOTLIGHT.md` with evidence-based categories, consent requirements, and a transparent review process.
- `community/COMMUNITY_ACTIVITIES.md` with weekly and monthly formats that run only when hosted.
- `community/RESOURCE_SUBMISSION.md` with quality criteria, status definitions, review rules, and correction handling.
- `community/GROWTH_STRATEGY.md` with a phased first-100-member plan, LinkedIn and GitHub promotion guidance, university and open-source outreach, onboarding, retention, and quality metrics.
- `community/templates/` with reusable formats for project proposals, finding teammates, collaboration requests, code review, project showcases, resource submissions, spotlight nominations, and community activities.

### Changed

- Expanded `resources/README.md` into a complete resource index with access labels, selection criteria, verification notes, and a submission route.
- Added Go and Rust learning paths to `resources/programming.md`.
- Added databases, SQL, OpenAPI, and app-development cross-links to `resources/web-development.md`.
- Added AI application development, current provider documentation, and clearer evaluation guidance to `resources/artificial-intelligence.md`.
- Connected `resources/open-source.md` to the DevSphere open-source and collaboration guides.
- Updated repository validation to require the new resource collections, community guides, and templates.
- Reconciled community status documents with the verified live Discussions state: 12 clean categories, 12/12 emoji metadata, and launch posts #1–#3 correctly categorized and pinned.
- Updated the community roadmap to record the completed foundation work and the remaining optional launch tasks.

### Fixed

- Replaced stale or redirected external links with current canonical URLs.
- Removed the stale duplicate Papers with Code entry after the site merged into Hugging Face Papers.
- Removed outdated claims that 16 categories, embedded emoji names, legacy categories, or incomplete pinning were still present.

### Security

- Kept paid, unpaid, and voluntary opportunity labels mandatory in collaboration and career content.
- Documented safety rules for credentials, private data, application fees, and suspicious opportunity posts.
- Preserved private reporting routes for Code of Conduct and security issues.

## [1.0.0] - 2026-11-03

### Added

- Complete DevSphere visual identity: logo, logo mark, banner, social preview, favicon, PNG exports, and brand guidelines.
- Professional repository README with mission, vision, objectives, community navigation, founder introduction, and getting-started guidance.
- Community documentation: guidelines, discussion guide, discussion setup playbook, moderation policy, member roles, and six-month roadmap.
- Contribution, code of conduct, security, and support policies.
- Twelve ready-to-publish discussion posts with category, format, and label recommendations.
- Curated learning resources for programming, web development, AI and machine learning, and open source.
- Coding challenge system with a reusable template and Challenge 001: Responsive Developer Profile Card.
- GitHub issue templates for bug reports, feature requests, project showcases, and general contributions, plus a pull request template.
- Repository validation workflow for Markdown linting, relative links, SVG syntax, and workflow YAML.
- Local validation script and Markdown lint configuration.

### Changed

- Expanded the initial README into a complete community guide.
- Standardized community links, naming, and brand terminology.

### Security

- Added a responsible disclosure policy with private reporting guidance.
- Added contribution rules that prohibit committing credentials or private data.

## Versioning notes

- **Major** releases introduce a comprehensive public documentation redesign or structural changes to the community's policies, discussion architecture, or brand identity.
- **Minor** releases add community programs, resource collections, challenges, or documentation sections.
- **Patch** releases fix links, typos, formatting, and small documentation errors.
