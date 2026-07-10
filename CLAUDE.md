# acmOS marketing site (ams-site)

Context for AI sessions / reviewers. This is the PUBLIC marketing site for acmOS
(the accommodation management system for major events — product repo: acm-app, private).

## Setup
- Static site, **GitHub Pages** from this repo (public), branch `main`, root.
- No build step, no framework, no dependencies: `index.html` (single file, inline CSS/JS),
  `video.html` (self-playing product film), `img/*.png` (real product screenshots).
- Publish flow: commit → push → Pages rebuilds in ~1 min. Cache-bust iframe/video with `?v=N`.

## Brand & positioning (decided, don't drift)
- Name: **acmOS** — "the accommodation operating system for major events". Wordmark acm + gradient OS.
- Logo: dark rounded square, gradient spark ✦ + amber dot (inline SVG + data-URI favicon).
- Design language: dark-first "aurora UI" (Linear/Vercel style): #070b17 bg, blue→violet
  gradients (#5b7cfa→#a78bfa), amber accents (#ffb454), glass cards, grid pattern in hero.
  Fonts: Sora (display) + Inter (body) via Google Fonts.
- Copy rules (research-backed): H1 < 8 words; pain before product; simple language;
  specificity over adjectives; AI positioned as "explainable, not a black box" —
  NEVER overclaim AI (the engine is a deterministic, auditable allocator).
- Audience: organising committees & event owners. Credibility anchor: built by Olympic
  Winter Games accommodation operations (founding team quote section).

## Key constraints (intentional)
- **No email address anywhere** (anti-spam + professionalism). Contact section is a
  placeholder until a Web3Forms key or a domain email exists. Do not re-add mailto.
- "Open the demo environment" points to a Replit DEV URL that sleeps when the owner's
  workspace is closed — known limitation, accepted for now (upgrade path: Render $7/mo).
- The film (`video.html`): embedded in #engine as a YouTube-style iframe with poster+play
  (click = user gesture = audio allowed; NEVER autoplay with sound). Music is synthesized
  in-page via WebAudio (no copyrighted assets). Narration via speechSynthesis (optional).
- Fairness depiction: bars must be ORGANISATIONS (A/B/C of the same group), not client
  groups — fairness balances companies; groups are separated by inventory blocks.
- Screenshots in img/ come from the product's `npm run shots` pipeline; don't hand-edit.

## Review focus (if you're here to audit)
1. Conversion: hero clarity (5-second test), CTA paths (all lead to #contact), mobile layout.
2. Copy: claims vs product truth (see acm-app/CLAUDE.md) — nothing the demo can't show.
3. Performance/a11y: single-file weight, font loading, contrast on dark theme, alt texts.
4. film timing/sync in video.html (CUES array) and behaviour inside the iframe embed.
