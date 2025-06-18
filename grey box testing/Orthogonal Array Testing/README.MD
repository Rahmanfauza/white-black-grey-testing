🧩 Orthogonal Array Testing (OAT)

📌 Deskripsi Singkat

Orthogonal Array Testing (OAT) adalah teknik pengujian **Gray Box** yang menggunakan pendekatan statistik untuk menghasilkan kombinasi uji yang efisien. Teknik ini sangat cocok digunakan saat terdapat banyak variabel input, karena mampu **mengurangi jumlah test case secara signifikan tanpa mengorbankan cakupan pengujian**.

---

🛠 Aplikasi yang Diuji

- **Nama Aplikasi:** Task Manager Web App  
- **Teknologi:** Flask, SQLite  
- **Fitur yang Diuji:** Form penambahan task (`/tasks/add`)  
- **Tujuan Pengujian:** Memverifikasi apakah sistem menangani berbagai kombinasi input task dengan benar dan sesuai validasi

---

🔍 Faktor dan Level Pengujian

| Faktor (Variabel)    | Level 1    | Level 2    | Level 3         |
|----------------------|------------|------------|------------------|
| Judul Task           | Kosong     | Normal     | Sangat Panjang   |
| Deskripsi Task       | Kosong     | Normal     | Sangat Panjang   |
| Status Task (manual) | pending    | selesai    | in progress      |

> Status dikontrol secara manual melalui parameter POST saat pengujian otomatis.

---

🧪 Kombinasi Pengujian – L9(3³)

| Test Case | Judul   | Deskripsi   | Status      | Ekspektasi                      |
|-----------|---------|-------------|-------------|----------------------------------|
| TC1       | Kosong  | Kosong      | pending     | Invalid (judul kosong)           |
| TC2       | Kosong  | Normal      | selesai     | Invalid                          |
| TC3       | Kosong  | Panjang     | in progress | Invalid                          |
| TC4       | Normal  | Kosong      | selesai     | Valid                            |
| TC5       | Normal  | Normal      | in progress | Valid                            |
| TC6       | Normal  | Panjang     | pending     | Valid                            |
| TC7       | Panjang | Kosong      | in progress | Valid                            |
| TC8       | Panjang | Normal      | pending     | Valid                            |
| TC9       | Panjang | Panjang     | selesai     | Valid                            |

---

💡 Logika Validasi Sistem

- **Judul kosong** → seharusnya ditolak (`invalid`)
- **Judul normal/panjang** → seharusnya diterima (`valid`)
- **Deskripsi kosong/panjang** → tidak berpengaruh terhadap validasi
- **Status** → tidak divalidasi karena tidak dikirim melalui form

---

⚙️ Implementasi Teknis

- File `test_cases.csv` memuat 9 kombinasi input berdasarkan Orthogonal Array L9(3³)
- Script `run_oat_tests.py`:
  - Membaca kombinasi dari CSV
  - Login otomatis sebagai user `airin`
  - Mengirimkan data ke endpoint `/tasks/add` melalui POST
  - Menentukan apakah input berhasil diproses (berdasarkan redirect ke `/dashboard`)
  - Membandingkan hasil aktual dengan nilai `ekspektasi` dari CSV

---

📊 Hasil Uji Aktual – Disertai Bukti Screenshot

<img width="600" alt="TC1–TC2" src="https://github.com/user-attachments/assets/a3e0b903-ce60-4401-8562-48d5699fdf65" />
<img width="600" alt="TC3–TC4" src="https://github.com/user-attachments/assets/c3c45afe-83c3-425b-9622-6bb8d317c36e" />
<img width="600" alt="TC5–TC6" src="https://github.com/user-attachments/assets/c8b2c24c-d874-45ab-932b-b76560b17701" />
<img width="600" alt="TC7–TC9" src="https://github.com/user-attachments/assets/cd68e515-4339-4cc6-97c4-e17135ed4e41" />

---

🧠 Insight & Kesimpulan

- Dari 9 test case yang diuji, sistem **menganggap semua input valid**, termasuk kombinasi dengan **judul kosong** (TC1–TC3) yang **seharusnya invalid**.
- Hasil ini menunjukkan bahwa validasi pada field *judul* **belum diterapkan dengan ketat** di sisi server.
- Semua data berhasil disimpan dan muncul di halaman task list, menandakan bahwa **endpoint `/tasks/add` menerima semua input** selama user dalam sesi login.
- Aplikasi tetap **stabil dan tidak mengalami crash**, bahkan saat menerima input deskripsi yang sangat panjang.
- Pendekatan OAT memungkinkan **pengujian efisien** dengan hanya 9 kombinasi, tanpa kehilangan cakupan variasi logis.
- Script `run_oat_tests.py` sangat membantu proses pengujian karena dapat **mendeteksi ketidaksesuaian antara ekspektasi dan realita** dengan cepat dan otomatis.

---
