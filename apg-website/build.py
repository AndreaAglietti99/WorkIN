#!/usr/bin/env python3
"""
Build the single-file distributable (adlerpelzer-website.html)
by inlining script.js into index.html.

Usage:  python3 build.py
"""
import pathlib

root = pathlib.Path(__file__).parent
html = (root / "index.html").read_text(encoding="utf-8")
js   = (root / "script.js").read_text(encoding="utf-8")

if '<script src="script.js"></script>' not in html:
    raise SystemExit('Could not find the <script src="script.js"> tag in index.html')

out = html.replace('<script src="script.js"></script>', "<script>\n" + js + "\n</script>")
(root / "adlerpelzer-website.html").write_text(out, encoding="utf-8")
print(f"Built adlerpelzer-website.html  ({len(out)/1024:.1f} KB)")
