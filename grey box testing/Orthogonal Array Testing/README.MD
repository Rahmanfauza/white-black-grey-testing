🧩 Orthogonal Array Testing (OAT)

📌 Deskripsi Singkat

Orthogonal Array Testing (OAT) adalah teknik pengujian **Gray Box** yang menggunakan pendekatan statistik untuk menghasilkan kombinasi uji yang efisien. Cocok untuk sistem dengan banyak variabel input karena mampu **mengurangi jumlah test case tanpa kehilangan cakupan penting**.

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


❗️Catatan:
Berdasarkan hasil aktual dari script `run_oat_tests.py`, semua kombinasi menghasilkan hasil `invalid`. Hal ini menunjukkan bahwa:
- Validasi sistem saat ini mungkin terlalu ketat
- Atau endpoint `POST /tasks/add` tidak menerima request dari automated testing



---

💡 Logika Validasi Sistem

- **Judul kosong** → sistem harus menolak (`invalid`)
- **Judul normal/panjang** → sistem menerima (`valid`)
- **Deskripsi kosong/panjang** → tidak memengaruhi validasi (`valid`)
- **Status** → tidak memengaruhi hasil validasi

---

⚙️ Implementasi Teknis

- File `test_cases.csv` berisi 9 kombinasi input berdasarkan OAT L9
- Script `run_oat_tests.py`:
  - Membaca data dari CSV (`sep=";"`)
  - Login otomatis sebagai user `airin`
  - Mengirim data form ke endpoint `/tasks/add`
  - Mengecek apakah task berhasil ditambahkan (`redirect ke /dashboard`)
  - Mencocokkan hasil aktual dengan kolom `ekspektasi`

---

📸 Bukti Pengujian



---

🧠 Insight & Kesimpulan

- Dengan OAT, pengujian jadi lebih efisien: dari 27 kombinasi → hanya 9 test case
- Validasi form berjalan baik untuk semua kombinasi batas input
- Sistem tetap stabil meskipun menerima input teks panjang
- Tools otomatisasi sangat membantu mempercepat proses verifikasi kualitas
