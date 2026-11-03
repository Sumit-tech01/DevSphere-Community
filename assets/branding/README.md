# DevSphere Brand Guidelines

The DevSphere identity is built around a simple idea: **many connected points forming one sphere.** It represents a global community of developers who learn, build, and grow together.

This directory contains the source assets for the DevSphere community. The SVG files are the source of truth; PNG exports are provided for platforms that do not render SVG.

> **Brand usage:** The DevSphere name, logo, and visual identity are community identity assets. The repository's [MIT License](../../LICENSE) covers documentation, templates, and code. Do not use the brand to impersonate DevSphere, imply endorsement, or mislead people about your relationship with the community.

---

## Asset index

| File | Format | Dimensions | Purpose |
| --- | --- | --- | --- |
| [`logo.svg`](logo.svg) | SVG | 840 × 280 | Primary horizontal logo with dark brand card |
| [`logo.png`](logo.png) | PNG | 840 × 280 | Raster version of the primary logo |
| [`logo-mark.svg`](logo-mark.svg) | SVG | 512 × 512 | Transparent logo mark for avatars and layouts |
| [`logo-mark.png`](logo-mark.png) | PNG | 512 × 512 | Raster logo mark |
| [`banner.svg`](banner.svg) | SVG | 1280 × 400 | Repository and README banner |
| [`banner.png`](banner.png) | PNG | 1280 × 400 | Raster banner |
| [`social-preview.svg`](social-preview.svg) | SVG | 1280 × 640 | GitHub social preview source |
| [`social-preview.png`](social-preview.png) | PNG | 1280 × 640 | Upload this to GitHub's social preview setting |
| [`favicon.svg`](favicon.svg) | SVG | 64 × 64 | Favicon-style app icon source |
| [`favicon.png`](favicon.png) | PNG | 512 × 512 | High-resolution favicon export |
| [`favicon-32.png`](favicon-32.png) | PNG | 32 × 32 | Small favicon export |

## Logo concept

The mark combines three ideas:

1. **A digital sphere** — a connected, global community rather than a single place.
2. **Orbital rings and nodes** — exchange, collaboration, and ideas moving between people.
3. **A subtle letter D** — a recognizable DevSphere signature integrated into the sphere rather than placed on top of it.

The wordmark uses a geometric sans-serif with generous letter spacing. The gradient moves from cyan through electric blue to violet, representing curiosity, engineering, and creativity.

## Color palette

| Token | Hex | Use |
| --- | --- | --- |
| **Midnight Navy** | `#0B1020` | Primary background, logo card, dark surfaces |
| **Electric Blue** | `#2563EB` | Primary actions, links, emphasis |
| **Cyan** | `#22D3EE` | Highlights, nodes, energy, focus accents |
| **Violet** | `#8B5CF6` | Creative accent, community, gradient end |
| **Cloud White** | `#F8FAFC` | Primary text and light surfaces |
| **Slate 400** | `#94A3B8` | Secondary text on dark surfaces |
| **Slate 500** | `#64748B` | Tertiary text and metadata |

**Gradient:** Cyan → Electric Blue → Violet. Use it for accents and the logo. Do not use it as a background for long body text.

**Contrast:** Body text on Midnight Navy should use Cloud White or Slate 400 at sufficient size. Verify contrast with a WCAG checker before publishing new assets. Do not place cyan text on white for body copy.

## Typography

- **Primary:** Inter, with `-apple-system`, `Segoe UI`, `Helvetica Neue`, Arial, and `sans-serif` fallbacks.
- **Style:** Geometric, modern, highly legible.
- **Wordmark:** Bold weight, wide tracking.
- **Body:** Regular or medium weight; avoid very light weights on dark backgrounds.
- **Fallback:** If Inter is unavailable, a clean geometric sans-serif is acceptable. Do not substitute a decorative or script font.

The repository does not bundle font files. Use the system fallback stack defined in the SVG or install Inter from [Google Fonts](https://fonts.google.com/specimen/Inter) if you need a local copy.

## Clear space and minimum size

- **Clear space:** Keep at least the height of the letter **D** clear on all sides of the logo.
- **Minimum logo width:** 320 px for the horizontal logo; 48 px for the mark.
- **Favicon:** Use the dedicated favicon asset at 16–64 px rather than shrinking the full logo.
- **Background:** The primary horizontal logo includes its own Midnight Navy card and works on light and dark pages. Use the transparent mark on dark surfaces.
- **Do not** place the transparent mark on a busy photograph without a contrast layer.

## Usage rules

**Do:**

- Use the provided SVG or PNG files without modification.
- Preserve the aspect ratio.
- Use the full logo when space allows and the mark when it does not.
- Add descriptive alt text: "DevSphere logo" or "DevSphere community logo".
- Use the palette consistently across community materials.
- Ask before using the brand for an event, product, or sponsorship claim.

**Do not:**

- Recolor, distort, rotate, or add effects to the logo.
- Crop the sphere or wordmark.
- Place the logo on a low-contrast background.
- Use the logo to imply official endorsement, partnership, or sponsorship.
- Combine the logo with another organization's mark without permission.
- Use the brand for scam, harassment, or misleading content.
- Present the logo as your own trademark.

## GitHub social preview

GitHub does not expose a public REST endpoint for uploading a repository social preview. An administrator must set it manually:

1. Open **Repository Settings → General**.
2. Scroll to **Social preview**.
3. Click **Edit** and upload [`social-preview.png`](social-preview.png).
4. Save and verify the preview in a private browser window or a link preview tool.

Recommended specifications:

- **Size:** 1280 × 640 px (2:1 ratio).
- **Format:** PNG or JPG, ideally under 1 MB.
- **Safe area:** Keep the logo and headline away from the outer 64 px; some surfaces crop the image.
- **Text:** Large enough to read on a phone.

## Regenerating PNG assets

The SVG files are the source of truth. If you update an SVG, regenerate the matching PNG with a tool you trust, such as:

```bash
# Example with CairoSVG (install separately; not a repository dependency)
python3 -m pip install cairosvg
python3 -c "import cairosvg; cairosvg.svg2png(url='assets/branding/social-preview.svg', write_to='assets/branding/social-preview.png', output_width=1280)"
```

Verify the exported PNG visually before committing it. Do not commit temporary files or install dependencies into the repository.

## Brand voice

DevSphere sounds:

- **Clear** — plain language, concrete examples, no jargon for its own sake.
- **Warm** — welcoming to beginners, never condescending.
- **Honest** — no inflated claims, fake statistics, or hype.
- **Curious** — interested in how things work and why.
- **Professional** — respectful of people's time, privacy, and craft.

**Tagline:** Connect. Code. Collaborate. Create.

**Short description:** A global developer community for learning, open source, AI, and building together.

## Questions

For brand usage questions, open a **General Discussion** post or contact the founder through [@Sumit-tech01](https://github.com/Sumit-tech01). Do not use the brand in a way that could confuse people about official DevSphere activity.

---

**Related:** [README](../../README.md) · [Community Guidelines](../../community/COMMUNITY_GUIDELINES.md) · [Contributing](../../CONTRIBUTING.md) · [License](../../LICENSE)
