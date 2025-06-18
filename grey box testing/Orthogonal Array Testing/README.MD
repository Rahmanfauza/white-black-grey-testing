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

🔍 Faktor dan Level yang Digunakan

| Faktor (Variabel)    | Level 1    | Level 2    | Level 3         |
|----------------------|------------|------------|------------------|
| Judul Task           | Kosong     | Normal     | Sangat Panjang   |
| Deskripsi Task       | Kosong     | Normal     | Sangat Panjang   |
| Status Task (manual) | pending    | selesai    | in progress      |

> Status dikontrol secara manual melalui POST request tambahan saat pengujian otomatis.

---

🧪 Kombinasi Pengujian: L9(3^3)

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

> ❗️ **Catatan:**  
> Berdasarkan hasil aktual dari script `run_oat_tests.py`, semua kombinasi menghasilkan `valid`. Hal ini menunjukkan bahwa:  
> - Validasi sistem mungkin belum membatasi input dengan ketat  
> - Endpoint `/tasks/add` menerima input apapun selama session login valid

---

💡 Logika Validasi Sistem

- **Judul kosong** → seharusnya ditolak (`invalid`)
- **Judul normal/panjang** → seharusnya diterima (`valid`)
- **Deskripsi kosong/panjang** → tidak berpengaruh pada validasi (`valid`)
- **Status** → tidak divalidasi karena tidak dimasukkan melalui form

---

⚙️ Implementasi Teknis

- File `test_cases.csv` berisi 9 kombinasi input berdasarkan Orthogonal Array L9(3^3)
- Script `run_oat_tests.py`:
  - Membaca kombinasi dari CSV
  - Login otomatis sebagai user `airin`
  - Mengirim data ke endpoint `/tasks/add` (POST request)
  - Menentukan valid/invalid berdasarkan redirect ke `/dashboard`
  - Membandingkan hasil aktual dengan kolom `ekspektasi`

---

📊 Hasil Uji Aktual – Disertai Bukti Screenshot

<img width="499" alt="Image" src="https://github.com/user-attachments/assets/a3e0b903-ce60-4401-8562-48d5699fdf65" />

<img width="499" alt="Image" src="https://github.com/user-attachments/assets/c3c45afe-83c3-425b-9622-6bb8d317c36e" />

<img width="603" alt="Image" src="https://github.com/user-attachments/assets/c8b2c24c-d874-45ab-932b-b76560b17701" />

<img width="575" alt="Image" src="https://github.com/user-attachments/assets/cd68e515-4339-4cc6-97c4-e17135ed4e41" />

---

🧠 Insight & Kesimpulan

- Dengan OAT, jumlah test case berhasil ditekan dari 27 → hanya 9 kombinasi tanpa kehilangan cakupan
- **Sistem menerima semua input** termasuk judul kosong, yang menunjukkan kurangnya validasi server-side
- Aplikasi tetap stabil meskipun menerima input dengan teks sangat panjang
- Pengujian otomatis melalui `run_oat_tests.py` sangat membantu mendeteksi inkonsistensi validasi

---
