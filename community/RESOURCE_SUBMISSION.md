# Resource Submission Process

DevSphere curates resources for developers at every stage. The collection is free to use, and inclusion is based on usefulness and verifiability, not payment, affiliation, or popularity.

This page covers **learning resources**. To submit an open-source project, developer tool, AI application, web app, or mobile app, use the [Project and Resource Discovery framework](PROJECT_DISCOVERY.md) and the [project discovery submission template](templates/PROJECT_DISCOVERY_SUBMISSION.md).

> **No paid placements.** DevSphere does not sell listings, accept affiliate links, or publish sponsored resources as neutral recommendations. A paid product can be included only when it is clearly labeled and genuinely useful alongside free alternatives.

## What belongs in the collection

| Category | Examples | Not a fit |
| --- | --- | --- |
| **Programming** | Official language docs, free books, practice platforms | Pirated books, scraped course dumps |
| **Web development** | MDN, framework docs, accessibility guidance | Link farms, SEO articles with no authorship |
| **AI & ML** | Papers, official model docs, free courses, evaluation guides | "Make money with AI" schemes, unverified benchmarks |
| **Developer tools** | Official tool documentation, open-source utilities | Cracked software, credential-stealing tools |
| **Career development** | Interview prep, resume guidance, verified programs | "Guaranteed job" services, paid referrals |
| **Open source** | Contribution guides, license references, issue discovery | Projects with no license presented as open source |
| **Roadmaps** | Structured learning paths with working links | Lists of affiliate courses |

## Quality criteria

Every submission is reviewed against these criteria:

| Criterion | Question | Pass example | Fail example |
| --- | --- | --- | --- |
| **Relevance** | Does it help a developer learn or build something real? | A framework's official tutorial | A generic productivity blog |
| **Authority** | Is the author or organization identifiable and credible? | Official documentation, recognized maintainers | Anonymous content with no sources |
| **Accuracy** | Are claims current and technically correct? | Versioned docs with clear scope | Outdated instructions presented as current |
| **Access** | Is the resource actually accessible? | Public page that loads without payment | Login wall, broken link, region lock |
| **Status** | Is free or paid status stated accurately? | "Free" for official docs; "Free + paid" with a pricing link | "Free" for a trial that expires |
| **Level** | Is the intended level clear? | Beginner, intermediate, advanced | No audience or prerequisites |
| **Maintenance** | Is the resource likely to stay useful? | Actively maintained docs or a stable archive | Abandoned project with broken setup |
| **Safety** | Does it avoid malware, scams, and privacy harm? | Reputable download source | Unverified binary, credential request |
| **Copyright** | Is it legal to link and describe? | Official page or open license | Pirated books, leaked courses |
| **Accessibility** | Is the page usable with a keyboard and screen reader? | Semantic docs, readable contrast | Image-only instructions |
| **Non-duplication** | Is it already covered by an existing entry? | A new, distinct official reference | A second link to the same homepage |

## Status labels

Use only these labels in resource tables:

| Label | Meaning | Evidence required |
| --- | --- | --- |
| **Free** | The linked resource is free to access | Official page loads without payment |
| **Free + paid** | A free plan or free core exists, and paid options are also offered | Official pricing or plan page |
| **Paid** | The resource requires payment | Official pricing page; clearly disclosed |
| **Docs free; usage billed** | Documentation is free, but using the service may cost money | Official pricing or billing page |
| **Free student resources** | Free resources with eligibility requirements | Official program page with eligibility |

Do not guess prices, free-tier limits, discounts, or eligibility. If a status cannot be verified, write "Verify current terms" and link the official page.

## Before submitting

1. **Search the collection.** Check [the resource index](../resources/README.md) and the relevant category page.
2. **Open the link in a private window.** Confirm it works without your login or a regional exception.
3. **Find the official source.** Prefer documentation, the maintainer's site, or the original paper.
4. **Check the date and version.** Note whether the resource is current, archived, or version-specific.
5. **Confirm the status.** Use one of the labels above and link the evidence.
6. **Check the license.** Do not submit pirated or leaked material.
7. **Remove tracking parameters.** Use a clean canonical URL.
8. **Write a useful description.** Explain who it helps and why, without marketing language.
9. **Disclose conflicts.** State if you are the author, maintainer, employee, or affiliate.
10. **Choose the right category.** Do not submit the same link to several categories.

## Submission paths

### Option A — Open an issue

Use the repository's [feature request issue template](https://github.com/Sumit-tech01/DevSphere-Community/issues/new?template=feature_request.md). Include the resource details from the template below. This is the best path for a suggestion that needs discussion or verification.

### Option B — Open a pull request

For a clear addition that follows the existing format:

1. Read [CONTRIBUTING.md](../CONTRIBUTING.md).
2. Edit the relevant file under [`resources/`](../resources/).
3. Add the resource in the correct table and alphabetical or logical position.
4. Include the name, official URL, description, category, level where appropriate, and status.
5. Update the resource index if you add a new collection.
6. Run the repository validation commands.
7. Open a pull request using the repository template.

Do not open a pull request that only adds an affiliate link, duplicate, or unverified paid placement.

## Review process

1. **Triage:** a maintainer checks the category, duplicate status, and link.
2. **Verification:** the URL, status, authority, and safety are checked.
3. **Editorial review:** the description is edited for clarity and honesty.
4. **Decision:** accepted, needs changes, or declined with a reason.
5. **Publication:** the resource is added to the appropriate page and index.
6. **Maintenance:** broken links and stale statuses are corrected when reported or during periodic review.

There is no guaranteed review deadline. DevSphere is maintained by volunteers. A submission can be declined even when the resource is good, for example if it duplicates existing coverage or does not fit the collection's scope.

## Review rubric

| Dimension | Weight | What reviewers check |
| --- | --- | --- |
| Usefulness | 30% | Solves a real learning or building need |
| Accuracy | 25% | Correct, current, and appropriately scoped |
| Authority | 20% | Official or credible source with identifiable authorship |
| Access and status | 15% | Works without hidden payment; status is accurate |
| Safety and legality | 10% | No malware, piracy, privacy harm, or misleading claims |

A score is not a substitute for judgment. Safety and legality are pass/fail gates.

## What we do not accept

- Affiliate, referral, or commission links.
- Paid placements presented as neutral recommendations.
- Pirated books, leaked courses, or bypassed paywalls.
- Scraped content with no rights.
- "Guaranteed job," "guaranteed income," or get-rich-quick material.
- Tools that request passwords, seed phrases, or unnecessary identity documents.
- Unverified binaries from unofficial sources.
- Link farms, auto-generated listicles, or content with no author.
- Duplicate URLs or near-duplicate pages.
- Discriminatory, harassing, or illegal material.
- Resources that require creating an account before showing any useful content, unless the resource is uniquely valuable and the requirement is disclosed.

## Corrections and removal

If a resource is broken, mislabeled, unsafe, or no longer free:

1. Open a [feature request](https://github.com/Sumit-tech01/DevSphere-Community/issues/new?template=feature_request.md) or a pull request with the correction.
2. Include the current status and evidence.
3. For a safety issue, report it through the private route in the [Code of Conduct](../CODE_OF_CONDUCT.md) if public details could cause harm.
4. A maintainer will verify and update or remove the entry.

Authors and maintainers can request removal of their resource. Removal does not imply misconduct.

## Resource submission template

Copy the template from [community/templates/RESOURCE_SUBMISSION.md](templates/RESOURCE_SUBMISSION.md), or use this short version:

```markdown
### Resource name

- **Official URL:**
- **Category:**
- **Description:**
- **Level:**
- **Status:** Free / Free + paid / Paid / Docs free; usage billed
- **Status evidence:**
- **Why it belongs:**
- **What it duplicates or replaces:**
- **Conflict of interest:**
- **I verified the link on:** YYYY-MM-DD
```

## Questions

Use [General Discussion](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/general-discussion) for questions about the process. Do not post private or sensitive information in a public thread.

---

**Related:** [Resource index](../resources/README.md) · [Project and Resource Discovery](PROJECT_DISCOVERY.md) · [Programming](../resources/programming.md) · [Web development](../resources/web-development.md) · [AI and machine learning](../resources/artificial-intelligence.md) · [Developer tools](../resources/developer-tools.md) · [Career development](../resources/career-development.md) · [Open source](../resources/open-source.md)
