# Maintenance mode (under construction gate)

**Status:** ON — the live homepage is preserved in `index-live.html`; visitors to `/` see the under-construction page.

## How this site is hosted

- **GitHub Pages** (custom domain: `aliceportfolio.com`, deploys from `main`)
- No Netlify (`netlify.toml` / `_redirects`), Vercel (`vercel.json`), Apache (`.htaccess`), or CI workflow found

GitHub Pages has no server-side rewrite rules, so the gate uses a **homepage swap** instead of a redirect file.

## What changed

| File | Role |
|------|------|
| `index-live.html` | **Added** — exact copy of the real homepage before maintenance |
| `index.html` | **Replaced** with the contents of `under-construction.html` (gate page) |
| `under-construction.html` | **Unchanged** — still available at `/under-construction.html` |
| Case studies, contact form, assets | **Unchanged** — still on disk and still reachable by direct URL |

### GitHub Pages limitation

This gates **`/` (the homepage) only**. These URLs still work if someone has the link or bookmark:

- `/sifted-case-study/`, `/contact-form/`, etc.
- Any case study HTML file path

To gate **every page**, say so and we can add a small temporary redirect script to each HTML file’s `<head>` (multi-page approach).

## Assets on the gate page

`under-construction.html` loads favicons from `/assets/...` and fonts from Google Fonts. Those paths are **not** affected by the homepage swap and should keep working.

## Turn maintenance mode OFF (restore live site)

One command from the repo root:

```bash
mv index-live.html index.html
```

Then commit and push to `main`. GitHub Pages will serve the real homepage again within a minute or two.

Or tell your agent:

> **Remove maintenance mode and restore the live site.**

That should run the same restore: move `index-live.html` back to `index.html`.

## Turn maintenance mode ON again later

```bash
cp index.html index-live.html
cp under-construction.html index.html
```

Then commit and push.

## Optional cleanup after restore

After turning maintenance off, you can delete `index-live.html` if you no longer need the backup copy in the repo (or keep it for the next maintenance window).
