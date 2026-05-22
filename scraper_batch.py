"""
=============================================================
 Scraper Multi-Bandara — Batch Mode
=============================================================
 Gunakan file ini untuk scraping banyak bandara sekaligus
 dalam satu eksekusi.
=============================================================
"""

from scraper import scrape
from datetime import date

# ─── Konfigurasi Batch ────────────────────────────────────────────────────────

# Daftar bandara yang ingin di-scrape (kode IATA)
BANDARA_LIST = [
    "UPG",  # Sultan Hasanuddin
    "CGK",  # Soekarno Hatta
    "SUB",  # Juanda
    "DPS",  # I Gusti Ngurah Rai
    "KNO",  # Kualanamu
]

# Kategori: "domestik" atau "internasional"
CATEGORIES = ["domestik", "internasional"]

# Rentang periode
START_PERIOD = "2020-01"
END_PERIOD   = date.today().strftime("%Y-%m")  # Bulan saat ini

# Jeda antar request (detik) — naikkan jika server sering error
DELAY = 2.0


# ─── Jalankan Scraping ────────────────────────────────────────────────────────

if __name__ == "__main__":
    results = {}

    for bandara in BANDARA_LIST:
        for category in CATEGORIES:
            print(f"\n{'='*60}")
            print(f"  Memproses: {bandara} — {category}")
            print(f"{'='*60}")

            try:
                df = scrape(
                    bandara  = bandara,
                    category = category,
                    start    = START_PERIOD,
                    end      = END_PERIOD,
                    delay    = DELAY,
                )
                if df is not None:
                    key = f"{bandara}_{category}"
                    results[key] = df
                    print(f"✅ Selesai: {bandara} {category} — {len(df)} baris data")
            except Exception as e:
                print(f"❌ Error pada {bandara} {category}: {e}")

    print(f"\n{'='*60}")
    print(f"  BATCH SELESAI — Total: {len(results)} kombinasi berhasil")
    print(f"{'='*60}")
