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

<img width="600" alt="Hasil TC1–TC3" src="https://github.com/user-attachments/assets/1c62ca63-2594-47e1-8e9c-37d77744984e" />

<img width="600" alt="Hasil TC4–TC6" src="https://github.com/user-attachments/assets/1cf5e715-1c41-4cbb-8095-347cfc4acbff" />

<img width="600" alt="Hasil TC7–TC9" src="https://github.com/user-attachments/assets/051e0dc7-c11b-41a3-9718-247b6bd69423" />

---

🧠 Insight & Kesimpulan

Hasil pengujian menggunakan metode Orthogonal Array Testing (OAT) mengungkap beberapa temuan penting yang sangat relevan terhadap asumsi awal validasi sistem:

- **Tiga kombinasi awal (TC1–TC3)** yang mengandung *judul kosong* seharusnya ditolak sesuai ekspektasi (`invalid`). Namun, berdasarkan hasil aktual, sistem **menerima input tersebut dan menyimpannya ke dalam task list**. Ini menunjukkan bahwa validasi field `judul` **belum diterapkan secara server-side**.
- Kombinasi lain dengan judul "normal" atau "sangat panjang" diproses dan ditampilkan dengan benar di dashboard aplikasi. Semua data tersimpan dalam kondisi stabil tanpa crash, **membuktikan bahwa aplikasi dapat menangani input besar dan variatif dengan baik**.
- Status task seperti `pending`, `completed`, dan `in-progress` berhasil disimulasikan dengan benar melalui parameter manual, dan tampil sesuai di UI.
- Pendekatan OAT berhasil **meringkas jumlah pengujian dari 27 menjadi hanya 9 kombinasi** dengan tetap mencakup seluruh variasi penting antar variabel.
- Script `run_oat_tests.py` berjalan lancar untuk otomatisasi uji, dengan hasil akurat dan bermanfaat untuk mendeteksi *mismatch* antara ekspektasi dan realita.

✅ Ringkasan:
- Validasi server-side belum membatasi input kosong pada field penting (judul).
- Semua kombinasi diterima sistem, meskipun tidak seluruhnya semestinya valid.
- Aplikasi stabil dan tangguh menangani input besar serta pengujian intensif.
- Metode OAT terbukti efektif untuk efisiensi pengujian dan mendukung QA otomatis.

---


