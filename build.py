#!/usr/bin/env python3
"""
Blue Dreams Resort & Spa Bodrum — MICE Landing Page Builder
============================================================
Çalıştır:  python3 build.py
Çıktı:     bluedreams-landing-v2.html  (self-contained, offline çalışır)

Gereksinimler:
    pip3 install Pillow PyMuPDF  --break-system-packages

Klasör yapısı (bu script ile aynı dizin):
    build.py
    template.html
    images/
        MER02619.jpg
        MER02615.jpg
        MER02612.jpg
        MER02606.jpg
        MER02602.jpg
        MER02596.jpg
        MER01894.jpg
        CEM05142.jpg
        CEM05139.jpg
    assets/
        factsheet.pdf
"""

import base64
import json
import os
import sys
from pathlib import Path
from io import BytesIO

# ── Ayarlar ─────────────────────────────────────────────────────────────────
SCRIPT_DIR   = Path(__file__).parent
TEMPLATE     = SCRIPT_DIR / "template.html"
OUTPUT       = SCRIPT_DIR / "bluedreams-landing-v2.html"
IMAGES_DIR   = SCRIPT_DIR / "images"
PDF_PATH     = SCRIPT_DIR / "assets" / "factsheet.pdf"
MAX_WIDTH    = 1000   # piksel
IMG_QUALITY  = 68     # JPEG kalitesi

# Görsellerin hangi placeholder'a karşılık geldiği
IMAGE_MAP = {
    "salon_sea": "aerial_view.jpg", # Havadan resort + deniz manzarası (hero ilk slayt)
    "salon_a": "MER02619.jpg",    # İstanbul Salonu — hero
    "salon_b": "MER02615.jpg",    # İstanbul Salonu (galeri)
    "salon_c": "_MUR5722.jpg",    # Stockholm
    "salon_d": "_MUR5702.jpg",    # Turunç
    "salon_e": "_MUR5706.jpg",    # Salamis
    "salon_f": "MER02596.jpg",    # İstanbul Salonu (galeri)
    "salon_g": "MER01894.jpg",    # Açık alan
    "salon_h": "_MUR5712.jpg",    # Marmaris
    "salon_i": "_MUR5709.jpg",    # Belek
}
# ─────────────────────────────────────────────────────────────────────────────


def encode_image(path: Path) -> str:
    """Görseli yükle, yeniden boyutlandır ve base64'e çevir."""
    try:
        from PIL import Image
    except ImportError:
        sys.exit("❌  Pillow kurulu değil → pip3 install Pillow --break-system-packages")

    with Image.open(path) as img:
        img = img.convert("RGB")
        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / img.width
            img = img.resize((MAX_WIDTH, int(img.height * ratio)), Image.LANCZOS)
        buf = BytesIO()
        img.save(buf, format="JPEG", quality=IMG_QUALITY, optimize=True)
    return base64.b64encode(buf.getvalue()).decode()


def encode_pdf(path: Path) -> str:
    """PDF'yi base64'e çevir."""
    return base64.b64encode(path.read_bytes()).decode()


def main():
    print("🏗️  Blue Dreams Landing Page Builder")
    print("=" * 45)

    # Template kontrol
    if not TEMPLATE.exists():
        sys.exit(f"❌  template.html bulunamadı: {TEMPLATE}")

    template_html = TEMPLATE.read_text(encoding="utf-8")

    # Görselleri işle
    replacements = {}
    for key, filename in IMAGE_MAP.items():
        img_path = IMAGES_DIR / filename
        if not img_path.exists():
            print(f"⚠️   Görsel bulunamadı (atlanıyor): {img_path}")
            replacements[f"__{key.upper()}__"] = ""
            continue
        print(f"🖼️   İşleniyor: {filename}")
        replacements[f"__{key.upper()}__"] = encode_image(img_path)

    # PDF işle
    if PDF_PATH.exists():
        print(f"📄  PDF işleniyor: {PDF_PATH.name}")
        replacements["__PDF_B64__"] = encode_pdf(PDF_PATH)
    else:
        print(f"⚠️   PDF bulunamadı (broşür indirme devre dışı): {PDF_PATH}")
        replacements["__PDF_B64__"] = ""

    # Template'e yerleştir
    html = template_html
    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)

    # Çıktıyı yaz
    OUTPUT.write_text(html, encoding="utf-8")
    size_mb = OUTPUT.stat().st_size / (1024 * 1024)
    print(f"\n✅  Oluşturuldu: {OUTPUT.name}  ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
