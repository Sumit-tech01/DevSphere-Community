# Challenge 001 — Responsive Developer Profile Card

**Level:** Beginner–Intermediate  
**Suggested timebox:** 4–8 hours  
**Focus areas:** Semantic HTML, CSS layout, responsive design, accessibility, visual hierarchy  
**Status:** Open  
**Submission category:** Project Showcase

---

## 1. Problem statement

Developer profiles are often the first thing a potential collaborator, recruiter, or client sees. A good profile card should communicate who someone is, what they build, and how to reach them — quickly, clearly, and on any screen size.

Your task is to build a **responsive developer profile card** for yourself or a clearly fictional developer. The card should feel like a polished component from a personal portfolio: intentional typography, strong hierarchy, accessible interactions, and a layout that works from a small phone to a wide desktop.

The card is a single component, not a full portfolio website. Focus on quality over quantity.

## 2. What you will practice

- Writing semantic HTML that describes content, not just appearance.
- Building a layout with modern CSS (Flexbox and/or Grid).
- Designing a responsive experience from 320px to 1440px and beyond.
- Meeting WCAG 2.2 AA accessibility requirements.
- Making deliberate choices about type, spacing, color, and contrast.
- Documenting your decisions and reflecting on trade-offs.

## 3. Core requirements

Your submission must include all of the following:

- [ ] **Semantic structure.** Use appropriate HTML elements such as `<main>`, `<article>`, `<header>`, `<h1>`, `<p>`, `<ul>`, and `<a>`. Do not build the card entirely from `<div>` elements.
- [ ] **Developer identity.** Display a profile image or avatar, full name, professional role, and a short bio (2–4 sentences).
- [ ] **Skills.** Show at least four technical skills or areas of focus in a list.
- [ ] **Location and availability.** Include a location or time zone and a short availability statement (for example, "Open to open-source collaboration").
- [ ] **Contact links.** Include at least three working links, such as GitHub, a portfolio, and a professional profile. Each link must have a clear accessible name.
- [ ] **Responsive layout.** The card must work at **320px**, **768px**, and **1440px** widths without horizontal scrolling or overlapping content.
- [ ] **Accessible markup.** Use descriptive `alt` text (or an appropriate empty `alt` for decorative images), visible focus styles, keyboard-operable links, and sufficient color contrast.
- [ ] **Visual design.** Use a deliberate type scale, consistent spacing, a clear hierarchy, and no more than one primary accent color plus neutrals.
- [ ] **Reduced motion.** Any animation must respect `prefers-reduced-motion`.
- [ ] **No private data.** Use your own information only if you are comfortable sharing it, or use clearly fictional data. Do not publish another person's personal information.
- [ ] **README.** Document how to run the project, include at least one screenshot, and explain one design or technical decision.
- [ ] **Original implementation.** You may follow tutorials and use design references, but the final code must be yours. Credit any assets or code you reuse.

### Suggested structure

```text
profile-card/
├── index.html
├── styles.css
├── script.js          # optional
├── assets/
│   └── avatar.webp
└── README.md
```

A build tool is not required. You may use React, Vue, Svelte, or another framework, but the same requirements apply.

## 4. Bonus features

These are optional and should not compromise the core requirements:

- [ ] **Theme toggle.** Support light and dark themes, remember the preference, and respect the system preference by default.
- [ ] **Initials fallback.** Generate an accessible avatar fallback from the person's initials if the image fails to load.
- [ ] **Copy email action.** Add a copy-to-clipboard button with visible confirmation and a fallback for browsers without clipboard support.
- [ ] **vCard download.** Provide a downloadable contact card with valid fields.
- [ ] **Print styles.** Make the card readable when printed.
- [ ] **Motion polish.** Add a subtle entrance or hover effect that is disabled under reduced motion.
- [ ] **Automated checks.** Run Lighthouse, axe, or another accessibility tool and document the results.
- [ ] **Deployment.** Publish the card with GitHub Pages and include the live link.
- [ ] **Internationalization.** Add a language toggle for two languages, with correct `lang` attributes.
- [ ] **Component tests.** Add tests for the theme toggle or copy action.

## 5. Example profile data

You may use this fictional example if you do not want to publish your own details:

```text
Name:        Maya Chen
Role:        Frontend Developer
Location:    Singapore (UTC+8)
Bio:         I build accessible, fast web interfaces and care about
             design systems that work for everyone.
Skills:      HTML, CSS, JavaScript, Accessibility, Design Systems
Links:       github.com/example, mayachen.example, linkedin.com/in/example
Availability: Open to open-source collaboration
```

All names, links, and details in the example are fictional. Replace them with your own information or another clearly fictional persona.

## 6. Deliverables

Submit:

1. A public repository containing the source code.
2. A live demo link, if available (GitHub Pages is free).
3. One or two screenshots showing desktop and mobile layouts.
4. A README with setup instructions and a short design rationale.
5. A reflection covering:
   - What you found difficult.
   - One trade-off you made.
   - What you would improve with more time.
   - How you checked accessibility.
6. A self-assessment using the rubric below.

## 7. Submission instructions

1. Build and test your card.
2. Push the code to your own public repository.
3. Open a **Project Showcase** discussion with this title:

   ```text
   [Challenge 001] Your Name — Developer Profile Card
   ```

4. Include the required links, screenshots, reflection, and rubric self-assessment.
5. Tag the post with `challenge-001` if the label is available.
6. Give specific, constructive feedback to at least one other submission.

**Do not open a pull request against the DevSphere repository with your solution.** Challenge solutions are shared in Discussions, not merged into this repository.

## 8. Evaluation rubric

| Criterion | Points | What reviewers look for |
| --- | ---: | --- |
| **Core requirements** | 40 | Every required element is present and working |
| **Responsive behavior** | 15 | No horizontal scroll at 320px, 768px, and 1440px; content remains readable and balanced |
| **Accessibility** | 15 | Semantic HTML, keyboard access, visible focus, contrast, alt text, reduced motion |
| **Visual design** | 10 | Hierarchy, spacing, typography, color discipline, and polish |
| **Code quality** | 10 | Readable structure, meaningful names, appropriate complexity, no dead code |
| **Communication** | 10 | README, screenshots, reflection, and self-assessment are clear and honest |
| **Total** | **100** | |

### Self-review bands

| Score | Interpretation |
| ---: | --- |
| 90–100 | Excellent: complete, accessible, polished, and clearly documented |
| 75–89 | Strong: all core requirements met with minor gaps |
| 60–74 | Complete: works, but needs accessibility, responsive, or documentation improvements |
| Below 60 | Revise: missing core requirements or significant usability issues |

These bands are for self-review and peer feedback, not a formal certification. Reviewers should explain their reasoning rather than only assigning a number.

## 9. Rules

- **Original work.** Write the implementation yourself. Credit tutorials, icons, fonts, and images.
- **Free tools only.** No paid APIs, paid templates, or paid hosting required.
- **Respect privacy.** Do not publish another person's personal data, contact details, or photograph without permission.
- **Accessibility is required.** A card that cannot be navigated with a keyboard is incomplete.
- **No plagiarism.** Do not copy another participant's submission.
- **Disclose AI assistance.** If you used AI tools for substantial code or design decisions, say so and ensure you can explain the result.
- **No vote manipulation.** Ask for feedback, not for artificial engagement.
- **Follow the Code of Conduct.** Be kind, specific, and constructive.

## 10. Hints

### Layout

- Start with a single-column card and add a two-column layout at a wider breakpoint only when the content benefits.
- Use `max-width`, `margin-inline: auto`, and fluid spacing with `clamp()` instead of fixed widths everywhere.
- Test at 320px first, then 768px, then 1440px.

### Typography

- Use a clear hierarchy: name, role, bio, section labels, links.
- Avoid more than two font families. System fonts are a valid, fast choice.
- Keep body text at a comfortable size and line length.

### Accessibility

- Use real links, not clickable `<div>` elements.
- Add `:focus-visible` styles with strong contrast.
- Check contrast with a tool; do not rely on appearance alone.
- Add `alt` text that describes the person's avatar meaningfully, or use `alt=""` if it is purely decorative and the name is adjacent.
- Respect `prefers-reduced-motion` for transitions and animations.
- Test with keyboard only and at 200% zoom.

### Code quality

- Use meaningful class names and group related CSS.
- Avoid unnecessary JavaScript; CSS can handle most of this challenge.
- Keep the README honest about what is finished and what is not.

## 11. Definition of done

- [ ] All core requirements are complete.
- [ ] The page works at 320px, 768px, and 1440px with no horizontal scrolling.
- [ ] Keyboard navigation reaches every interactive element.
- [ ] Focus states are visible.
- [ ] Text contrast meets WCAG AA.
- [ ] Images have appropriate alt text.
- [ ] Motion respects reduced-motion preferences.
- [ ] No private data or secrets are included.
- [ ] The README includes setup instructions and a screenshot.
- [ ] The submission is posted in Project Showcase with the correct title.
- [ ] The reflection explains at least one trade-off.

## 12. Resources

- [MDN — Learn Web Development](https://developer.mozilla.org/en-US/docs/Learn_web_development)
- [MDN — CSS Layout Cookbook](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook)
- [MDN — Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
- [W3C — WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [web.dev — Learn Performance](https://web.dev/learn/performance)
- [The A11Y Project](https://www.a11yproject.com/)
- [GitHub Pages](https://docs.github.com/en/pages)

## 13. What to avoid

- A card that only looks good at one screen width.
- Clickable `<div>` elements instead of semantic links.
- Invisible or missing focus styles.
- Low-contrast text or decorative text over busy images.
- Auto-playing animation or motion that ignores user preferences.
- A screenshot with no README or explanation.
- Copying a tutorial's code without understanding or attribution.
- Sharing someone else's photo, email, or location without consent.

---

**Questions?** Ask in **Questions & Help** or the **Hackathons & Challenges** discussion. **Finished?** Share it in **Project Showcase** with the title format above.

**Challenge version:** 1.0 · **Published:** 3 November 2026
