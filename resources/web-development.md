# Web Development Resources

A practical, free path through modern web development: fundamentals first, then frameworks, databases, APIs, testing, accessibility, performance, and deployment. For a staged sequence, see the [frontend](learning-roadmaps.md#frontend-developer), [backend](learning-roadmaps.md#backend-developer), and [full-stack](learning-roadmaps.md#full-stack-developer) roadmaps.

> All core resources are free to access. Optional certificates or paid hosting are not required. See the [resource index](README.md) for selection criteria.

## Start here

| Resource | Why it helps |
| --- | --- |
| [MDN — Learn Web Development](https://developer.mozilla.org/en-US/docs/Learn_web_development) | Structured curriculum from the web's reference documentation |
| [web.dev — Learn](https://web.dev/learn/) | Short, practical courses from Google's web team |
| [The Odin Project](https://www.theodinproject.com/) | Free, project-based full-stack curriculum |
| [freeCodeCamp — Responsive Web Design](https://www.freecodecamp.org/learn/2022/responsive-web-design) | Hands-on HTML and CSS practice |
| [HTML Living Standard](https://html.spec.whatwg.org/) | The authoritative HTML specification |
| [W3C Web Accessibility Initiative](https://www.w3.org/WAI/) | Accessibility standards and guidance |

## HTML and CSS

| Resource | Level | Notes |
| --- | --- | --- |
| [MDN HTML Guide](https://developer.mozilla.org/en-US/docs/Web/HTML) | Beginner | Elements, attributes, and semantics |
| [MDN CSS Guide](https://developer.mozilla.org/en-US/docs/Web/CSS) | Beginner | Layout, typography, color, and responsive design |
| [web.dev — Learn CSS](https://web.dev/learn/css) | Beginner–Intermediate | Modern CSS in focused modules |
| [CSS-Tricks — Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) | Beginner | Visual guide to Flexbox |
| [CSS-Tricks — Grid Guide](https://css-tricks.com/complete-guide-css-grid-layout/) | Beginner | Visual guide to CSS Grid |
| [Every Layout](https://every-layout.dev/) | Intermediate | Layout patterns that adapt to content |
| [Modern CSS Solutions](https://moderncss.dev/) | Intermediate | Replacement patterns for older CSS techniques |

**Practice idea:** Build a responsive profile card using semantic HTML, CSS Grid or Flexbox, and a layout that works at 320px and 1440px without horizontal scrolling.

## JavaScript for the web

| Resource | Level | Notes |
| --- | --- | --- |
| [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) | Beginner | Language fundamentals in a web context |
| [MDN DOM Introduction](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) | Beginner | Interacting with the page |
| [MDN Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) | Intermediate | HTTP requests from the browser |
| [JavaScript.info](https://javascript.info/) | Beginner–Advanced | Community textbook with exercises |
| [web.dev — Learn JavaScript](https://web.dev/learn/javascript) | Beginner–Intermediate | Modern JavaScript concepts |

## React

| Resource | Level | Notes |
| --- | --- | --- |
| [React — Learn](https://react.dev/learn) | Beginner | Official, interactive introduction |
| [React — Reference](https://react.dev/reference/react) | All | Hooks and API reference |
| [React — Thinking in React](https://react.dev/learn/thinking-in-react) | Beginner | Component and state design |
| [React — Community](https://react.dev/community) | All | Official community resources |
| [React Router](https://reactrouter.com/) | Intermediate | Routing for React applications |
| [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Intermediate | Server-state management |

**Practice idea:** Build a small searchable list with loading, empty, error, and success states. Keep components small and derive state instead of duplicating it.

## Next.js

| Resource | Level | Notes |
| --- | --- | --- |
| [Next.js Documentation](https://nextjs.org/docs) | Beginner–Advanced | Official framework documentation |
| [Next.js Learn](https://nextjs.org/learn) | Beginner | Project-based official course |
| [Next.js — App Router](https://nextjs.org/docs/app) | Intermediate | Routing, layouts, and rendering |
| [Next.js — Data Fetching](https://nextjs.org/docs/app/getting-started/fetching-data) | Intermediate | Server and client data patterns |
| [Next.js — Deployment](https://nextjs.org/docs/app/getting-started/deploying) | Intermediate | Deployment options and considerations |

**Practice idea:** Build a small content site with static pages, one dynamic route, metadata, and an accessible navigation menu.

## Node.js and backend

| Resource | Level | Notes |
| --- | --- | --- |
| [Node.js — Learn](https://nodejs.org/learn) | Beginner | Official Node.js learning path |
| [Node.js API Documentation](https://nodejs.org/api/) | All | Runtime and standard library reference |
| [Express.js Guide](https://expressjs.com/en/guide/routing/) | Beginner | Minimal Node.js web framework |
| [Fastify Documentation](https://fastify.dev/docs/latest/) | Intermediate | Performance-focused Node.js framework |
| [MDN — HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) | Beginner–Intermediate | Methods, status codes, headers, and caching |
| [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) | Intermediate | Describe an HTTP API as a reviewable contract |
| [Databases and SQL](#databases-and-sql) | Beginner–Intermediate | Relational and document database foundations |
| [Prisma Documentation](https://www.prisma.io/docs) | Intermediate | Type-safe database access for Node.js and TypeScript |

**Practice idea:** Build a small REST API with validation, pagination, structured errors, and tests. Describe it in OpenAPI before implementing it. Do not expose stack traces in production responses.

## Databases and SQL

| Resource | Level | Notes |
| --- | --- | --- |
| [SQLBolt](https://sqlbolt.com/) | Beginner | Interactive SQL lessons in the browser |
| [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html) | Beginner | Official relational database tutorial and SQL path |
| [SQLite Documentation](https://www.sqlite.org/docs.html) | Beginner–Advanced | Embedded database documentation and SQL reference |
| [MongoDB Documentation](https://www.mongodb.com/docs/) | Intermediate | Document database concepts, queries, and operations |

**Practice idea:** Model the same small feature in a relational database and a document database. Write down which constraints, joins, transactions, and migration path each choice makes easier or harder.

## TypeScript in web projects

| Resource | Level | Notes |
| --- | --- | --- |
| [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) | Beginner–Advanced | Official language guide |
| [React — TypeScript](https://react.dev/learn/typescript) | Intermediate | Official React TypeScript guidance |
| [Next.js — TypeScript](https://nextjs.org/docs/app/api-reference/config/typescript) | Intermediate | TypeScript configuration in Next.js |
| [Total TypeScript — Beginners Tutorial](https://www.totaltypescript.com/tutorials/beginners-typescript) | Beginner | Free interactive tutorial |

## Accessibility

Accessibility is part of quality, not an optional feature.

| Resource | Why it matters |
| --- | --- |
| [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/) | The standard for web content accessibility |
| [W3C WAI — Tutorials](https://www.w3.org/WAI/tutorials/) | Practical guidance for common patterns |
| [MDN — Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility) | Accessible HTML, ARIA, and testing |
| [WebAIM — WCAG Checklist](https://webaim.org/standards/wcag/checklist) | A practical checklist for audits |
| [The A11Y Project](https://www.a11yproject.com/) | Community-driven accessibility resources |
| [Inclusive Components](https://inclusive-components.design/) | Accessible UI pattern design |

**Minimum checks:** keyboard navigation, visible focus, semantic headings, form labels, color contrast, alt text, reduced motion, and zoom at 200%.

## Performance

| Resource | Why it matters |
| --- | --- |
| [web.dev — Learn Performance](https://web.dev/learn/performance) | Core performance concepts and metrics |
| [Core Web Vitals](https://web.dev/articles/vitals) | User-centered performance metrics |
| [MDN — Web Performance](https://developer.mozilla.org/en-US/docs/Web/Performance) | Performance fundamentals |
| [PageSpeed Insights](https://pagespeed.web.dev/) | Measure real-world and lab performance |
| [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) | Automated audits for performance and accessibility |

## Testing

| Resource | Level | Notes |
| --- | --- | --- |
| [Vitest Guide](https://vitest.dev/guide/) | Intermediate | Fast unit testing for Vite projects |
| [Jest Documentation](https://jestjs.io/docs/getting-started) | Intermediate | Widely used JavaScript test runner |
| [Testing Library](https://testing-library.com/docs/) | Intermediate | Test behavior, not implementation details |
| [Playwright](https://playwright.dev/docs/intro) | Intermediate | End-to-end browser testing |
| [Cypress](https://docs.cypress.io/app/get-started/why-cypress) | Intermediate | Browser testing and debugging |

## Security

| Resource | Why it matters |
| --- | --- |
| [OWASP Top Ten](https://owasp.org/projects/top-ten) | Common web application security risks |
| [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) | Practical defenses for common features |
| [MDN — Web Security](https://developer.mozilla.org/en-US/docs/Web/Security) | Browser security fundamentals |
| [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) | Reducing injection risk |
| [GitHub — Secret Scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning) | Prevent credential leaks |

## Deployment and developer experience

| Resource | Why it matters |
| --- | --- |
| [GitHub Pages](https://docs.github.com/en/pages) | Free static site hosting |
| [GitHub Actions](https://docs.github.com/en/actions) | Free CI/CD for public repositories |
| [Docker — Get Started](https://docs.docker.com/get-started/) | Reproducible development environments |
| [Vite](https://vite.dev/guide/) | Fast frontend tooling |
| [ESLint](https://eslint.org/docs/latest/) | Static analysis for JavaScript and TypeScript |
| [Prettier](https://prettier.io/docs/) | Consistent formatting |

## Suggested learning sequence

1. **HTML semantics and CSS layout.** Build static pages before adding a framework.
2. **JavaScript fundamentals and the DOM.** Make a page interactive without a framework.
3. **HTTP, APIs, and forms.** Understand requests, responses, validation, and errors.
4. **One framework.** Learn React or another framework deeply enough to explain its rendering model.
5. **TypeScript.** Add types to a real project, not only exercises.
6. **Testing and accessibility.** Make quality visible in your workflow.
7. **Backend and database.** Build an API with validation, authentication boundaries, and tests.
8. **Deployment and observability.** Ship something, measure it, and learn from failures.

## Mobile and cross-platform

Web skills transfer to mobile, but mobile has different layout, lifecycle, permission, offline, and release constraints. See the [app development collection](app-development.md) and the [Mobile App Developer roadmap](learning-roadmaps.md#mobile-app-developer) when you want to build for Android, iOS, Flutter, React Native, or Expo.

## Avoid

- Learning five frameworks before building one complete project.
- Copying UI code without understanding accessibility.
- Ignoring error, loading, and empty states.
- Storing secrets in client-side code.
- Deploying without checking responsive behavior and keyboard access.
- Trusting tutorials that are more than a major version behind.

---

**Related:** [Learning Roadmaps](learning-roadmaps.md) · [Programming](programming.md) · [App Development](app-development.md) · [AI & Machine Learning](artificial-intelligence.md) · [Developer Tools](developer-tools.md) · [Open Source](open-source.md) · [Web Development discussions](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/web-development)
