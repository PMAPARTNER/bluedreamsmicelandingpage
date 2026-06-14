#!/bin/bash
# ============================================================
# Blue Dreams Resort — Deploy Script
# Kullanım: ./deploy.sh
# ============================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo ""
echo "🏗️  Landing page yeniden oluşturuluyor..."
python3 build.py

echo ""
echo "🚀  GitHub'a push ediliyor..."
git add bluedreams-landing-v2.html
git commit -m "Landing page güncellendi — $(date '+%Y-%m-%d %H:%M')"
git push origin main

echo ""
echo "✅  Tamamlandı!"
echo "📎  GitHub: https://github.com/PMAPARTNER/bluedreamsmicelandingpage"
echo "🌐  Live:   https://pmapartner.github.io/bluedreamsmicelandingpage/bluedreams-landing-v2.html"
