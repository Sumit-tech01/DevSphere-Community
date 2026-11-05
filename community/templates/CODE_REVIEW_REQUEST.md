# Code Review Request Template

Use this template in [Questions & Help](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/questions-help) or [Collaboration](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/collaboration) when you want focused feedback on a change.

> A review request is not a demand for free labor. Keep the diff small, state what you need, and respect the reviewer's time.

## Title

`[Project] — review [change] for [correctness / security / performance / accessibility]`

## Pull request or diff

- **Link:** [pull request, commit, or diff]
- **Issue:** [linked issue]
- **Size:** [files and lines changed]
- **Status:** [draft or ready for review]

## What this change does

[Two or three sentences. Explain the before and after behavior, not only the files changed.]

## Why this approach

[What alternatives did you consider? What trade-off did you choose?]

## Review focus

Prioritize the areas where you need the most help:

- [ ] Correctness
- [ ] Security and authorization
- [ ] Performance
- [ ] Accessibility
- [ ] Test coverage
- [ ] Naming and readability
- [ ] Architecture
- [ ] Documentation

**Specific question:** [for example, "Is the cursor signature verified before the database query?"]

## How to verify

```text
[install, run, and test commands]
```

**Tests I ran:** [commands and results]

**Manual checks:** [steps and outcome]

**Screenshots or recordings:** [links, if the change is visual]

## Known limitations

- [limitation]
- [follow-up work not included]
- [uncertainty the reviewer should know]

## Deadline

- **Needed by:** [date or "no deadline"]
- **Flexible:** [yes/no]
- **If the timeline is tight:** [what can be merged or deferred]

If there is no real deadline, say so. Artificial urgency discourages review.

## Reviewer guidance

- Point out blocking issues separately from preferences.
- Explain the reasoning when possible.
- Suggest a test or smaller alternative.
- Do not rewrite the branch without asking.

## Pre-review checklist

- [ ] The pull request description explains the change.
- [ ] The diff is limited to one problem.
- [ ] Tests pass locally.
- [ ] New behavior has tests or a documented manual check.
- [ ] Documentation is updated when needed.
- [ ] No secrets, personal data, or debug output are included.
- [ ] The review focus is specific.

---

**Related:** [Collaboration Guide](../COLLABORATION_GUIDE.md) · [Open-Source Guide](../OPEN_SOURCE_GUIDE.md) · [Collaboration request](COLLABORATION_REQUEST.md)
