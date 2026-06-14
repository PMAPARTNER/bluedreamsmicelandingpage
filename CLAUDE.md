# Blue Dreams Resort & Spa Bodrum — MICE Landing Page

## Proje Özeti
Türkçe reklam amaçlı landing page. Mavi/lacivert tema, self-contained HTML (görseller ve PDF base64 olarak gömülü).

**Canlı URL:** https://pmapartner.github.io/bluedreamsmicelandingpage/bluedreams-landing-v2.html  
**Booking URL:** https://bluedreamsresort.com/tr/meetings  
**GitHub Repo:** https://github.com/PMAPARTNER/bluedreamsmicelandingpage

---

## Claude için: Deploy Talimatları

Kullanıcı "deploy et", "push et", "güncelle" dediğinde şu adımları izle:

### 1. Repo'yu /tmp'ye klonla (her seferinde)
```bash
TOKEN=$(cat ~/Downloads/.github_token)
rm -rf /tmp/bluedreams-repo
git clone https://PMAPARTNER:${TOKEN}@github.com/PMAPARTNER/bluedreamsmicelandingpage.git /tmp/bluedreams-repo
cd /tmp/bluedreams-repo
git config user.email "hanates4444@gmail.com"
git config user.name "PMAPARTNER"
git remote set-url origin https://PMAPARTNER:${TOKEN}@github.com/PMAPARTNER/bluedreamsmicelandingpage.git
```

### 2. HTML'i yeniden oluştur
```bash
cd /tmp/bluedreams-repo
# Görselleri ve PDF'i kopyala
cp ~/Downloads/images/* ./images/ 2>/dev/null || true
cp ~/Downloads/assets/* ./assets/ 2>/dev/null || true
# Build et
python3 build.py
```

### 3. Push et
```bash
cd /tmp/bluedreams-repo
git add bluedreams-landing-v2.html
git commit -m "Landing page güncellendi — $(date '+%Y-%m-%d %H:%M')"
git push origin main
```

**NOT:** Bash sandbox'ında internet erişimi VAR. Git push direkt çalışır. Chrome MCP'ye gerek yok.

---

## Klasör Yapısı

```
repo/
├── build.py            ← Build script (çalıştır: python3 build.py)
├── deploy.sh           ← Build + git push (çalıştır: ./deploy.sh)
├── template.html       ← HTML template (__SALON_A__ ... __PDF_B64__ placeholder'ları)
├── bluedreams-landing-v2.html  ← Oluşturulan çıktı (commit'lenen dosya)
├── images/             ← Görseller (Drive'dan indirilmiş)
│   ├── MER02619.jpg    → salon_a (İstanbul Salonu — hero)
│   ├── MER02615.jpg    → salon_b
│   ├── MER02612.jpg    → salon_c
│   ├── MER02606.jpg    → salon_d
│   ├── MER02602.jpg    → salon_e
│   ├── MER02596.jpg    → salon_f
│   ├── MER01894.jpg    → salon_g
│   ├── CEM05142.jpg    → salon_h
│   └── CEM05139.jpg    → salon_i
└── assets/
    └── factsheet.pdf   ← Broşür (indirme butonu için)
```

---

## Görsel Kaynağı
Google Drive: https://drive.google.com/drive/u/1/folders/1AS0vDacBXAFP2ieh1i-IGHBVY0DCOrS3

---

## Salon Bilgileri (PDF Factsheet'ten)

| Salon | Tiyatro | Banket | Boyutlar |
|-------|---------|--------|----------|
| İstanbul Salonu | 700 | 450 | 770 m², bölünebilir (Avrupa + Asya) |
| Turunç | 35 | 10 | 4.50 × 6.50 m |
| Salamis | 45 | 14 | 8.30 × 4.35 m |
| Belek | 20 | 10 | 4.40 × 4.40 m |
| Marmaris | 30 | 10 | 4.30 × 5.30 m |
| Stockholm | 20 | 10 | 4.30 × 4.40 m |

---

## İletişim Bilgileri
- Tel: +90 252 337 11 11
- E-posta: sales@bluedreamsresort.com
- Adres: Torba Mah. Heredot Bulvarı No:11 Bodrum, Muğla

---

## CSS Değişkenleri
```css
--navy: #0d1e2c;
--blue: #1a6fa8;
--cyan: #3ab4e6;
--light: #e8f4fb;
```
