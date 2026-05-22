# Kemenhub HubUD — Scraper Lalu Lintas Angkutan Udara

## 📦 Instalasi

```bash
cd d:\xampp\htdocs\kemenhub-scraping
pip install -r requirements.txt
```

## 🚀 Cara Penggunaan

### 1. Single Bandara (CLI)

```bash
# Scrape UPG domestik dari Januari 2020 sampai bulan ini
python scraper.py --bandara UPG --category domestik --start 2020-01

# Scrape CGK internasional dengan rentang tertentu
python scraper.py --bandara CGK --category internasional --start 2023-01 --end 2024-12

# Semua opsi tersedia
python scraper.py --help
```

### 2. Multi-Bandara (Batch)

Edit file `scraper_batch.py`, ubah daftar bandara dan kategori, lalu jalankan:

```bash
python scraper_batch.py
```

## 📋 Parameter CLI

| Parameter | Singkat | Default | Keterangan |
|-----------|---------|---------|------------|
| `--bandara` | `-b` | `UPG` | Kode IATA bandara |
| `--category` | `-c` | `domestik` | `domestik` atau `internasional` |
| `--start` | `-s` | `2020-01` | Periode awal `YYYY-MM` |
| `--end` | `-e` | Bulan ini | Periode akhir `YYYY-MM` |
| `--output` | `-o` | Auto | Nama file output (tanpa ekstensi) |
| `--delay` | `-d` | `1.5` | Jeda antar request (detik) |
| `--no-resume` | | — | Mulai ulang dari awal (hapus progress) |

## 📊 Output

Program menghasilkan dua file:

| File | Format | Keterangan |
|------|--------|------------|
| `lalinud_UPG_domestik_2020-01_2026-05.csv` | CSV | UTF-8 BOM, siap untuk Excel |
| `lalinud_UPG_domestik_2020-01_2026-05.xlsx` | Excel | Dengan formatting tabel |

### Kolom Data

| Kolom | Keterangan |
|-------|------------|
| `Periode` | Format YYYY-MM |
| `Bandara` | Kode IATA |
| `Kategori` | Domestik / Internasional |
| `Pesawat_Datang` | Jumlah pergerakan pesawat datang |
| `Pesawat_Berangkat` | Jumlah pergerakan pesawat berangkat |
| `Penumpang_Datang` | Jumlah penumpang datang |
| `Penumpang_Berangkat` | Jumlah penumpang berangkat |
| `Penumpang Transit_Datang` | Penumpang transit datang |
| `Penumpang Transit_Berangkat` | Penumpang transit berangkat |
| `Kargo_Datang` | Kargo datang (kg) |
| `Kargo_Berangkat` | Kargo berangkat (kg) |
| `Bagasi_Datang` | Bagasi datang (kg) |
| `Bagasi_Berangkat` | Bagasi berangkat (kg) |
| `Pos_Datang` | Pos/mail datang (kg) |
| `Pos_Berangkat` | Pos/mail berangkat (kg) |

## ⚡ Fitur

- ✅ **Auto CSRF token** — diambil otomatis dari halaman awal
- ✅ **Resume** — lanjut dari progress terakhir jika terputus
- ✅ **Retry otomatis** — 3x percobaan jika request gagal
- ✅ **Rate limiting** — delay antar request agar tidak di-block
- ✅ **Logging** — log tersimpan di `scraper.log`
- ✅ **Export CSV & Excel** — dengan formatting otomatis

## 🏗️ Struktur File

```
kemenhub-scraping/
├── scraper.py              # Script utama (single bandara)
├── scraper_batch.py        # Script batch (multi-bandara)
├── requirements.txt        # Daftar dependensi Python
├── README.md               # Dokumentasi ini
├── scraper.log             # Log eksekusi (auto-generated)
└── output/                 # File hasil scraping (auto-generated)
    ├── lalinud_UPG_domestik_*.csv
    └── lalinud_UPG_domestik_*.xlsx
```
