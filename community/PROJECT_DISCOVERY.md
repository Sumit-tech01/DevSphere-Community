# DevSphere Project and Resource Discovery

DevSphere helps members find work worth learning from: open-source projects, developer tools, AI applications, web and mobile products, and trustworthy learning resources. This framework explains how to submit them, how they are verified, and how to avoid spam, copyright problems, and privacy harm.

> **Honest status:** DevSphere does not maintain a ranked directory of projects. There is no invented catalog, no paid placement, and no guarantee that a submission will be featured. This page defines the process so future discoveries are useful and trustworthy.

## What can be submitted

| Type | Examples | Best place to submit |
| --- | --- | --- |
| **Open-source project** | A library, CLI, self-hosted tool, or educational repository with a license | [Project Showcase](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/project-showcase) |
| **Developer tool** | An editor extension, testing utility, API client, or build tool | Project Showcase; use the resource process if it is primarily documentation |
| **AI application** | An LLM app, evaluation harness, agent, or ML demo with clear limits | Project Showcase, with safety and evaluation notes |
| **Web application** | A production or prototype web product | Project Showcase |
| **Mobile application** | An Android, iOS, Flutter, or React Native app | Project Showcase |
| **Learning resource** | A course, book, tutorial, roadmap, or reference | [Resource Submission](RESOURCE_SUBMISSION.md) or a pull request to [`resources/`](../resources/) |

If you are unsure, choose the closest category and explain the ambiguity in the post. Do not cross-post the same item to several categories.

## Where submissions happen

- **Projects and products:** [Project Showcase](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/project-showcase) using the [project showcase template](templates/PROJECT_SHOWCASE.md) or the [project discovery submission template](templates/PROJECT_DISCOVERY_SUBMISSION.md).
- **Learning resources:** the [resource submission process](RESOURCE_SUBMISSION.md), a feature request issue, or a pull request to the relevant file under [`resources/`](../resources/).
- **Collaboration requests:** [Collaboration](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/collaboration) using the [project proposal](templates/PROJECT_PROPOSAL.md), [find a teammate](templates/FIND_A_TEAMMATE.md), or [collaboration request](templates/COLLABORATION_REQUEST.md) template.
- **Questions about the process:** [General Discussion](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/general-discussion).

Do not open a pull request that only adds an affiliate link, a duplicate entry, or an unverified paid placement.

## Submission format

Every project submission should include:

| Field | What to provide |
| --- | --- |
| **Name** | The project's public name |
| **One-sentence description** | What it does and who it helps |
| **Repository** | Public URL, or an explanation of what can be verified if private |
| **Live demo or website** | A working link, or "not available" |
| **Category** | Open-source project, developer tool, AI app, web app, mobile app, or learning resource |
| **Stage** | Idea, prototype, MVP, live, maintained, or archived |
| **License** | The actual license, or "not open source" |
| **Problem** | The problem it solves and who experiences it |
| **What is new or useful** | The specific contribution, not marketing language |
| **Known limitations** | Honest boundaries and unresolved issues |
| **What you want** | Feedback, users, contributors, reviewers, or collaborators |
| **Affiliation** | Author, maintainer, employee, contractor, investor, affiliate, or unrelated |
| **Sponsorship or paid features** | Any paid plan, sponsorship, or commercial interest |
| **Verification date** | The date you last checked the links |

Use the [project discovery submission template](templates/PROJECT_DISCOVERY_SUBMISSION.md) for a complete version.

## Verification standards

A reviewer should be able to confirm the submission without asking for private access.

### Links

- Open every link in a private browser window.
- Confirm the page loads without a login wall, region lock, or broken redirect.
- Use the canonical URL, not a tracking or affiliate link.
- Prefer the official repository or documentation over a content farm.
- Check that the demo and repository refer to the same project.
- Record the date of the check.

### Repository and license

- Confirm the repository is public and the license is present.
- Do not describe a project as open source if it has no license or uses a restrictive license incorrectly.
- Check whether the README explains setup, usage, and limitations.
- Check recent activity only as context. An old but stable project can still be useful; a new project is not automatically better.
- Do not use stars, forks, or contributor counts as a quality score.

### Claims

- Verify users, revenue, downloads, awards, and partnerships before repeating them.
- If a number cannot be verified, omit it or label it as the submitter's estimate.
- Distinguish "live" from "coming soon" and "prototype" from "production."
- Do not present a demo as evidence of general capability.
- For AI projects, ask what was evaluated, what data was used, and what limitations remain.

### Safety

- Do not download or run unverified binaries.
- Do not open a project that requests passwords, seed phrases, tokens, or identity documents.
- Do not test a project with real customer data or production credentials.
- Report malware, phishing, or credential harvesting through the private route in the [Code of Conduct](../CODE_OF_CONDUCT.md).

## Review process

1. **Triage.** A maintainer checks the category, completeness, duplicate status, and basic safety.
2. **Verification.** Links, license, claims, and affiliations are checked.
3. **Editorial review.** The description is edited for clarity, accuracy, and length.
4. **Decision.** Accepted, needs changes, or declined with a reason.
5. **Publication.** The project or resource is shared in the appropriate discussion or collection.
6. **Maintenance.** Broken links and stale claims are corrected when reported or during periodic review.

There is no guaranteed review deadline. DevSphere is maintained by volunteers. A submission can be declined even when the project is good, for example if it duplicates existing coverage, is outside the community's scope, or cannot be verified safely.

## Review rubric

| Dimension | Weight | What reviewers check |
| --- | --- | --- |
| **Usefulness** | 30% | Solves a real problem for a defined audience |
| **Originality** | 20% | Adds something distinct; not a repost or near-duplicate |
| **Documentation** | 20% | Clear setup, usage, limitations, and license |
| **Safety and legality** | 20% | No malware, piracy, privacy harm, or misleading claims |
| **Verifiability** | 10% | Working links, identifiable authorship, honest evidence |

Safety and legality are pass/fail gates. A high score elsewhere does not override a safety problem.

## Spam prevention

DevSphere removes or restricts submissions that behave like spam:

- The same project posted repeatedly or across several categories.
- Link shorteners, affiliate links, referral codes, or tracking parameters.
- Mass mentions, unsolicited direct messages, or requests to move to a private group immediately.
- "Guaranteed job," "guaranteed income," or "guaranteed users" claims.
- Generic AI-generated posts with no connection to the project.
- Fake engagement, purchased stars, or coordinated upvoting.
- Requests for fees, bank details, identity documents, or credentials.
- Recruiting spam disguised as a project showcase.
- A new account whose first post is only a promotional link.

**Rate guidance:** one submission per project per 30 days is enough. Update the existing thread with a release note instead of creating a new post. If a project changes substantially, explain what changed and why a new post is useful.

**No engagement bait:** do not ask members to star, follow, upvote, or share a project as a condition of feedback. Ask for feedback on the work.

## Copyright and attribution

- Submit only work you created or have permission to share.
- Respect the project's license and attribution requirements.
- Do not paste proprietary code, leaked material, or paywalled content.
- Do not use screenshots, logos, or images without permission.
- Credit collaborators, third-party assets, datasets, and inspiration.
- Do not remove copyright notices or license headers.
- If you are unsure whether you can share something, link to the official page instead of copying it.

## Privacy and safety

- Do not include passwords, API keys, tokens, private keys, or customer data.
- Do not include home addresses, phone numbers, private email, identity documents, or private messages.
- Do not publish another person's information without consent.
- Do not share private repositories or internal dashboards.
- If a project is for a minor, use guardian consent and minimal personal details.
- Remove metadata from screenshots when it could reveal private information.
- Follow the [Code of Conduct](../CODE_OF_CONDUCT.md) and [Moderation Policy](MODERATION_POLICY.md).

## Affiliations and sponsorships

Disclose any relationship that could affect how a submission is read:

| Relationship | What to disclose |
| --- | --- |
| **Author or maintainer** | You built or maintain the project |
| **Employee or contractor** | You work for the organization behind it |
| **Investor or advisor** | You have a financial or advisory relationship |
| **Affiliate or referral** | You earn a commission or benefit from sign-ups |
| **Sponsored** | Someone paid for the project, post, or promotion |
| **Unrelated** | You have no relationship beyond using the project |

Paid tools and services are labeled. DevSphere does not accept affiliate links or paid placements presented as neutral recommendations. A paid product can be discussed when it is clearly labeled and genuinely useful alongside free alternatives.

## What is not accepted

- Pirated books, leaked courses, or bypassed paywalls.
- Malware, credential-stealing tools, or unverified binaries.
- Affiliate, referral, or commission links.
- Paid placements presented as neutral recommendations.
- "Guaranteed job," "guaranteed income," or get-rich-quick material.
- Scraped content with no rights.
- Link farms, auto-generated listicles, or content with no identifiable author.
- Duplicate URLs or near-duplicate pages.
- Discriminatory, harassing, or illegal material.
- Projects that require sensitive personal data before showing any useful function, unless the requirement is necessary and clearly disclosed.

## Corrections and removal

If a project or resource is broken, mislabeled, unsafe, or no longer accurate:

1. Open a [feature request](https://github.com/Sumit-tech01/DevSphere-Community/issues/new?template=feature_request.md) or reply in the original discussion with the correction.
2. Include the current status and evidence.
3. For a safety issue, use the private reporting route in the [Code of Conduct](../CODE_OF_CONDUCT.md).
4. A maintainer will verify and update or remove the entry.

Authors and maintainers can request removal of their project from a DevSphere collection. Removal does not imply misconduct.

## Current discovery index

**No project index is published yet.** DevSphere will not create placeholder projects or fictional entries. When real submissions are reviewed and consented to, they will be linked from the relevant category page or discussion.

## Related documents

- [Project discovery submission template](templates/PROJECT_DISCOVERY_SUBMISSION.md)
- [Project showcase template](templates/PROJECT_SHOWCASE.md)
- [Resource submission process](RESOURCE_SUBMISSION.md)
- [Developer Spotlight](DEVELOPER_SPOTLIGHT.md)
- [Community Initiatives](COMMUNITY_INITIATIVES.md)
- [Collaboration Guide](COLLABORATION_GUIDE.md)
- [Community Guidelines](COMMUNITY_GUIDELINES.md)
- [Moderation Policy](MODERATION_POLICY.md)
