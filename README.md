# Resume Web Project

Ushbu loyiha shaxsiy rezume (CV) veb-saytini Django asosida yaratish uchun mo‘ljallangan.

## 🚀 Loyiha holati

Asosiy funksiyalar tugallangan va loyiha ishga tayyor. Quyidagi jadvalda asosiy fayl va papkalarning holati keltirilgan:

| Fayl/Papka 
|------------
| `templates/` 
| `static/` 
| `core/`
| `main/`
| `media/projects/` 
| `statfiles/` 
| `.dockerignore` 
| `.env` 
| `.gitignore` 
| `Dockerfile` 
| `compose.yaml` 
| `compose.debug.yaml`
| `requirements.txt` 
| `Pipfile` / `Pipfile.lock` 
| `Huseyin_CV.docx` 
| `Resume_Huseyin.pdf`
| `db.sqlite3` 
| `manage.py` 

## 📁 Asosiy papkalar

- `core/` – asosiy dastur mantiqi
- `main/` – loyihaning asosiy sozlamalari
- `templates/` – HTML shablonlari
- `static/` – statik fayllar (CSS, JS, rasmlar)
- `media/projects/` – loyihalarga oid media fayllar

## 🐳 Docker orqali ishga tushirish

Loyiha Docker yordamida oson ishga tushiriladi:

```bash
docker-compose up
