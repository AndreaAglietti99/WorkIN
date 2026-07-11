# Adler Pelzer Group — Website (project context)

This is a modern restyling of **adlerpelzer.com**, a B2B automotive Tier-1 supplier
(acoustic & thermal components and systems). Single self-contained file, no backend,
no build framework. Editable source + a one-step build into a single HTML file.

## Files

- `index.html` — source markup + all CSS (in one `<style>`). References `script.js`.
- `script.js` — all JS: i18n dictionary (5 languages), interactions, renderers, router.
- `adlerpelzer-website.html` — **built single-file output** (index.html + script.js inlined). This is the deployable artifact.
- `build.py` — run `python3 build.py` to regenerate `adlerpelzer-website.html` after editing source.
- `world.geo.json` / `map_path.txt` — source data + generated SVG path for the world map (already inlined into index.html).

## How to work on it

1. Edit `index.html` and/or `script.js`.
2. Preview: open `index.html` directly, or `python3 -m http.server` then visit it (so `script.js` loads).
3. Build the single file: `python3 build.py`.
4. Deploy `adlerpelzer-website.html` anywhere (static host) — it has no dependencies except Google Fonts.
