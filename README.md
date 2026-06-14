# Blue Dreams Resort & Spa Bodrum — MICE Landing Page

Toplantı & etkinlik salonları için Türkçe reklam landing page'i.

---

## Kurulum (ilk kez)

### 1. Repoyu klonla
```bash
git clone https://github.com/PMAPARTNER/bluedreamsmicelandingpage.git
cd bluedreamsmicelandingpage
```

### 2. Gerekli Python kütüphanelerini yükle
```bash
pip3 install Pillow PyMuPDF --break-system-packages
```

### 3. Görselleri ve PDF'i yerleştir
Görselleri `images/` klasörüne, PDF'i `assets/` klasörüne koy:

```
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
```

> Görseller Google Drive'dan alınır:  
> https://drive.google.com/drive/u/1/folders/1AS0vDacBXAFP2ieh1i-IGHBVY0DCOrS3

---

## Güncelleme & Deploy

Görsel veya içerik değişikliği yaptıktan sonra tek komutla deploy et:

```bash
./deploy.sh
```

Bu komut:
1. `build.py` ile HTML'i yeniden oluşturur (görseller base64 olarak gömülür)
2. `git commit` + `git push` ile GitHub'a yükler

---

## Sadece Build (push etmeden)

```bash
python3 build.py
```

Çıktı: `bluedreams-landing-v2.html`

---

## Dosya Yapısı

| Dosya | Açıklama |
|-------|----------|
| `build.py` | Görseller + PDF → HTML oluşturur |
| `deploy.sh` | Build + GitHub push |
| `template.html` | HTML şablonu (placeholder'lı) |
| `bluedreams-landing-v2.html` | Oluşturulan çıktı (açmak için tarayıcıya sürükle) |

---

## İletişim
**Blue Dreams Resort & Spa Bodrum**  
📞 +90 252 337 11 11  
✉️ sales@bluedreamsresort.com  
📍 Torba Mah. Heredot Bulvarı No:11 Bodrum, Muğla
