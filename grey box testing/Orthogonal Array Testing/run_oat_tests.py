import requests
import pandas as pd

# Konfigurasi
BASE_URL = "http://127.0.0.1:5000"
LOGIN_URL = f"{BASE_URL}/login"
ADD_TASK_URL = f"{BASE_URL}/tasks/add"

USERNAME = "airin"
PASSWORD = "passwordairin"

# Baca CSV (pakai pemisah ;)
# Baca CSV
try:
    df = pd.read_csv("test_cases.csv", sep=";")
    print("✅ File test_cases.csv berhasil dibaca.")
    print("📄 Kolom yang terbaca oleh pandas:", df.columns.tolist())  # DEBUG!
except Exception as e:
    print("❌ Gagal membaca test_cases.csv:", e)
    exit()


# Session agar bisa simpan cookies (untuk login)
session = requests.Session()

# Step 1: Login dulu
login_data = {
    "username": USERNAME,
    "password": PASSWORD
}

login_response = session.post(LOGIN_URL, data=login_data)

if "dashboard" not in login_response.url:
    print("❌ Login gagal. Cek username/password.")
    exit()

print("\n✅ Login berhasil! Mulai menjalankan test case...\n")

# Step 2: Jalankan test case dari CSV
for idx, row in df.iterrows():
    title = str(row.get('judul', '')).strip()
    description = str(row.get('deskripsi', '')).strip()
    expected = str(row.get('ekspektasi', '')).lower().strip()

    # Data yang akan dikirim ke form
    payload = {
        "title": title,
        "description": description
    }

    response = session.post(ADD_TASK_URL, data=payload, allow_redirects=False)

    # Penilaian hasil
    if response.status_code == 302 and response.headers.get("Location", "").endswith("/dashboard"):
        result = "valid"
    else:
        result = "invalid"

    status = "✅ SESUAI" if result == expected else "❌ TIDAK SESUAI"

    print(f"[TC{idx+1}] Judul: {title[:15]:<15} | Ekspektasi: {expected:<7} | Hasil: {result:<7} → {status}")
