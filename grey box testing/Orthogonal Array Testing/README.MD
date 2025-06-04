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

| TC  | Judul   | Deskripsi   | Status      | Ekspektasi | Hasil Aktual | Sesuai? | Bukti (Screenshot)                      |
|-----|---------|-------------|-------------|------------|---------------|----------|------------------------------------------|
| TC1 | Kosong  | Kosong      | pending     | Invalid    | valid         | ❌        | ![](./screenshots/TC1.png)              |
| TC2 | Kosong  | Normal      | selesai     | Invalid    | valid         | ❌        | ![](./screenshots/TC2.png)              |
| TC3 | Kosong  | Panjang     | in progress | Invalid    | valid         | ❌        | ![](./screenshots/TC3.png)              |
| TC4 | Normal  | Kosong      | selesai     | Valid      | valid         | ❌        | ![](./screenshots/TC4.png)              |
| TC5 | Normal  | Normal      | in progress | Valid      | valid         | ❌        | ![](./screenshots/TC5.png)              |
| TC6 | Normal  | Panjang     | pending     | Valid      | valid         | ❌        | ![](./screenshots/TC6.png)              |
| TC7 | Panjang | Kosong      | in progress | Valid      | valid         | ❌        | ![](./screenshots/TC7.png)              |
| TC8 | Panjang | Normal      | pending     | Valid      | valid         | ❌        | ![](./screenshots/TC8.png)              |
| TC9 | Panjang | Panjang     | selesai     | Valid      | valid         | ❌        | ![](./screenshots/TC9.png)              |

---

🧠 Insight & Kesimpulan

- Dengan OAT, jumlah test case berhasil ditekan dari 27 → hanya 9 kombinasi tanpa kehilangan cakupan
- **Sistem menerima semua input** termasuk judul kosong, yang menunjukkan kurangnya validasi server-side
- Aplikasi tetap stabil meskipun menerima input dengan teks sangat panjang
- Pengujian otomatis melalui `run_oat_tests.py` sangat membantu mendeteksi inkonsistensi validasi

---
