#!/usr/bin/env bash
# Run once from this folder before going live:  bash fetch-images.sh
# Saves every image (old-site product photos + Unsplash photography) into ./images
# and rewrites all pages to use the local copies.
set -e
cd "$(dirname "$0")"
mkdir -p images/photos
while read -r url; do
  [ -z "$url" ] && continue
  rel="${url#https://trimlinemedicals.com/images/}"
  mkdir -p "images/$(dirname "$rel")"
  echo "↓ $rel"; curl -fsSL "$url" -o "images/$rel" || echo "  (missing on old site, skipped)"
done < image-list.txt
grep -oh 'https://images.unsplash.com/photo-[^"&)]*?auto=format&amp;fit=crop&amp;w=[0-9]*&amp;q=80\|https://images.unsplash.com/photo-[^"&)]*?auto=format&fit=crop&w=[0-9]*&q=80' *.html | sed 's/&amp;/\&/g' | sort -u | while read -r u; do
  id=$(echo "$u" | sed -E 's#.*photo-([^?]*)\?.*w=([0-9]+).*#\1-w\2#'); f="images/photos/$id.jpg"
  [ -f "$f" ] || { echo "↓ $f"; curl -fsSL "$u" -o "$f" || echo "  (failed)"; }
done
for f in *.html; do
  python3 - "$f" <<'PY'
import re,sys
p=sys.argv[1]; s=open(p).read()
s=s.replace("https://trimlinemedicals.com/images/","images/")
s=re.sub(r"https://images\.unsplash\.com/photo-([^?\"')]+)\?auto=format(?:&amp;|&)fit=crop(?:&amp;|&)w=(\d+)(?:&amp;|&)q=80", r"images/photos/\1-w\2.jpg", s)
open(p,"w").write(s)
PY
done
echo "Done — all images are now local."
