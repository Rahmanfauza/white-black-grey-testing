# 🧩 Pattern Testing – Test Case Documentation

Dokumentasi ini berisi rangkaian pengujian eksploratif (Pattern Testing) yang dilakukan pada aplikasi **Task Manager**. Fokus utama pengujian ini adalah mengeksplorasi fungsi dari antarmuka, input tak biasa, validasi form, performa aplikasi, dan pengalaman pengguna (UX).

---

## ✅ 1. Test Case – Fungsional Dasar

| No | Skenario | Langkah | Hasil yang Diharapkan | Status | Screenshot |
|----|----------|--------|------------------------|--------|-----------|
| 1.1 | Login user | Input username & password yang benar | Halaman dashboard ditampilkan dengan notifikasi “Login berhasil” | ✅ | ![Screenshot 1](screenshots/1.%20Menguji%20Fungsional%20Dasar/1.png) |
| 1.2 | Logout user | Klik tombol logout | Redirect ke halaman login, pesan “Anda telah logout” muncul | ✅ | ![Screenshot 2](screenshots/1.%20Menguji%20Fungsional%20Dasar/2.png) |
| 1.3 | Tambah tugas | Klik "Add Task", isi judul dan deskripsi, submit | Tugas tampil di dashboard | ✅ | ![Screenshot 3](screenshots/1.%20Menguji%20Fungsional%20Dasar/3.png) |
| 1.4 | Lihat semua tugas | Klik menu "Tasks" | Semua tugas ditampilkan dengan status dan waktu | ✅ | ![Screenshot 4](screenshots/1.%20Menguji%20Fungsional%20Dasar/4.png) |
| 1.5 | Update status tugas | Klik tombol update status (Pending → Completed) | Status berubah dan tersimpan | ✅ | ![Screenshot 5](screenshots/1.%20Menguji%20Fungsional%20Dasar/5.png) |
| 1.6 | Hapus tugas | Klik tombol delete | Tugas hilang dari daftar | ✅ | ![Screenshot 6](screenshots/1.%20Menguji%20Fungsional%20Dasar/6.png) |

---

🚧 2. Test Case – Batasan & Input Aneh

| No  | Skenario                   | Input                     | Hasil yang Diharapkan                             | Status | Screenshot |
|-----|----------------------------|---------------------------|---------------------------------------------------|--------|------------|
| 2.1 | Judul dan Deskripsi kosong | *(biarkan kosong)*        | Tetap tersimpan tanpa error                       | ✅     | <img width="400" alt="2.1" src="https://github.com/user-attachments/assets/170067f5-4c16-4c8f-8daa-242d16246676" /> |
| 2.2 | Input sangat panjang       | >10.000 karakter di deskripsi | Tidak crash, data tersimpan atau ditolak sopan | ✅     | <img width="400" alt="2.2" src="https://github.com/user-attachments/assets/ef4f8595-4a2f-4533-84d9-a3653c137fc1" /> |
| 2.3 | Karakter aneh di judul     | "!@#*🤯🎉"                | Tidak error, tetap ditampilkan dengan aman         | ✅     | <img width="400" alt="2.3" src="https://github.com/user-attachments/assets/6e9a9bcb-0b43-4300-91b4-16268012315a" /> |


---

⚙️ 3. Test Case – Performa dan Stabilitas

| No  | Skenario          | Langkah                                  | Hasil yang Diharapkan                        | Status | Screenshot |
|-----|-------------------|------------------------------------------|----------------------------------------------|--------|------------|
| 3.1 | Tambah banyak tugas | Tambah 100 tugas via form/manual        | Aplikasi tetap responsif                     | ✅     | <img width="400" alt="3.1" src="https://github.com/user-attachments/assets/17d398c3-8a8d-4115-a6a2-bf6039cc024d" /> |
| 3.2 | Operasi berulang  | Tambah, edit, hapus secara berurutan 10x | Tidak freeze/crash                           | ✅     | <img width="400" alt="3.2" src="https://github.com/user-attachments/assets/d06a4b06-c1bd-4eb5-878b-e6870ffb2712" /> |
| 3.3 | Akses multitab    | Login dari 2 tab                         | Tidak logout paksa, data konsisten           | ✅     | <img width="400" alt="3.3" src="https://github.com/user-attachments/assets/f37b7b00-e212-4b13-8208-f17fd27f233c" /> |


---
🎨 4. Test Case – Usability & Pengalaman Pengguna

| No  | Skenario            | Fokus                                   | Hasil yang Diharapkan                                                                                                                                                 | Status | Screenshot |
|-----|---------------------|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------------|
| 4.1 | Navigasi menu       | Klik Dashboard, Tasks, Settings          | ⚠️ Di halaman **Dashboard**, menu sisi kiri muncul dan navigasi mudah. Di halaman **Tasks**, menu kiri tidak muncul namun tersedia tombol kembali di bawah. Di halaman **Settings**, tidak ada tombol kembali ke Dashboard – hanya bisa klik icon profil. | ✅     | <img width="400" src="https://github.com/user-attachments/assets/784250f4-a454-4597-b20b-3f1fd2d247cd" /> <img width="400" src="https://github.com/user-attachments/assets/c75296c5-fa36-407c-9ace-3df7bb18885e" /> <img width="400" src="https://github.com/user-attachments/assets/922ebb84-308b-4cb8-938c-9e49323a5f62" /> |
| 4.2 | Feedback error      | Input password salah di login            | Pesan error muncul dengan warna yang jelas                                                                                                                             | ✅     | <img width="400" src="https://github.com/user-attachments/assets/f18703cc-da53-4828-8fab-bda764231ee9" /> <img width="400" src="https://github.com/user-attachments/assets/58dbe9e9-50fd-4915-8ea5-39699af2f12d" /> |
| 4.3 | Placeholder form    | Formulir isian memiliki placeholder & label | Placeholder dan label muncul di semua form                                                                                                                            | ✅     | <img width="200" src="https://github.com/user-attachments/assets/cba5d8cf-f3cc-45b4-bbd5-e9b418605e9a" /> <img width="200" src="https://github.com/user-attachments/assets/45dc4f11-1684-4a31-8852-43a57c449d97" /> <img width="200" src="https://github.com/user-attachments/assets/f81ff1ef-4047-4c46-85e8-190652eff094" /> <img width="200" src="https://github.com/user-attachments/assets/5bbf3750-1fdb-49f9-b851-e985fdad1739" /> |
| 4.4 | Komponen interaktif | Cek semua tombol dan ikon berfungsi      | ⚠️ Ditemukan beberapa tombol tidak berfungsi:<br>• Tombol lihat kata sandi (tidak aktif)<br>• Tombol forgot password (tidak merespons)<br>• Tombol reset tugas (tidak merespons)<br>• Tombol ganti warna tema di Settings (tidak aktif) | ❌     | <img width="400" src="https://github.com/user-attachments/assets/328d28d6-02e3-4dae-9e00-6f2379a9ac32" /> |
| 4.5 | UI konsisten        | Cek keseragaman font, warna, dan layout | Semua halaman menggunakan layout dan style konsisten                                                                                                                  | ✅     | <img width="400" src="https://github.com/user-attachments/assets/316b4598-e61a-427d-8118-20772f126b81" /> |


---

📌 Catatan Umum:

- Semua pengujian dilakukan menggunakan **user: airin**.
- Aplikasi lolos uji untuk input ekstrem, edge cases, dan tetap stabil walau diuji berulang dan cepat.
- Pengujian dilakukan secara manual dan sebagian menggunakan console skrip otomatis dengan browser Chrome pada resolusi layar laptop.

---

## 🏁 Kesimpulan Sementara

Pattern Testing menunjukkan bahwa aplikasi:
- ✅ Stabil dalam berbagai kondisi input
- ⚠ Perlu validasi lebih spesifik untuk input seperti HTML/script (walau tidak langsung berbahaya)

---

