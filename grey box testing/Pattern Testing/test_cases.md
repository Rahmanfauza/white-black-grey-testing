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

## 🚧 2. Test Case – Batasan & Input Aneh

| No | Skenario | Input | Hasil yang Diharapkan | Status | Screenshot |
|----|----------|-------|------------------------|--------|-----------|
| 2.1 | Judul kosong | `""` | Validasi muncul: “Judul wajib diisi” | ✅ | ![Screenshot 7](screenshots/2.%20Menguji%20Batasan/1.png) |
| 2.2 | Deskripsi kosong | (biarkan kosong) | Tetap tersimpan tanpa error | ✅ | ![Screenshot 8](screenshots/2.%20Menguji%20Batasan/2.png) |
| 2.3 | Input sangat panjang | >10.000 karakter di deskripsi | Tidak crash, data tersimpan atau ditolak sopan | ✅ | ![Screenshot 9](screenshots/2.%20Menguji%20Batasan/3.png) |
| 2.4 | Karakter aneh di judul | "!@#*🤯🎉" | Tidak error, tetap ditampilkan dengan aman | ✅ | ![Screenshot 10](screenshots/2.%20Menguji%20Batasan/4.png) |
| 2.5 | Input skrip (XSS attempt) | `<script>alert(1)</script>` | Teks ditampilkan sebagai string biasa, tidak dieksekusi | ✅ | ![Screenshot 11](screenshots/2.%20Menguji%20Batasan/5.png) |

---

## ⚙️ 3. Test Case – Performa dan Stabilitas

| No | Skenario | Langkah | Hasil yang Diharapkan | Status | Screenshot |
|----|----------|--------|------------------------|--------|-----------|
| 3.1 | Tambah banyak tugas | Tambah 100 tugas via form/manual | Aplikasi tetap responsif | ✅ | ![Screenshot 12](screenshots/3.%20Performa%20dan%20Stabilitas/1.png) |
| 3.2 | Operasi berulang | Tambah, edit, hapus secara berurutan 10x | Tidak freeze/crash | ✅ | ![Screenshot 13](screenshots/3.%20Performa%20dan%20Stabilitas/2.png) |
| 3.3 | Akses multitab | Login dari 2 tab | Tidak logout paksa, data konsisten | ✅ | ![Screenshot 14](screenshots/3.%20Performa%20dan%20Stabilitas/3.png) |

---
🎨 4. Test Case – Usability & Pengalaman Pengguna

| No | Skenario | Fokus | Hasil yang Diharapkan | Status | Screenshot |
|----|----------|-------|------------------------|--------|------------|
| 4.1 | Navigasi menu | Klik Dashboard, Tasks, Settings | ⚠️ Di halaman **Dashboard**, menu sisi kiri muncul dan navigasi mudah. Di halaman **Tasks**, menu kiri tidak muncul namun tersedia tombol kembali di bawah. Di halaman **Settings**, tidak ada tombol kembali ke Dashboard – hanya bisa klik icon profil. | ✅ | ![Screenshot 15](screenshots/4.%20Kegunaan%20UX/1-navigasi.png) |
| 4.2 | Feedback error | Input password salah di login | Pesan error muncul dengan warna yang jelas | ✅ | ![Screenshot 16](screenshots/4.%20Kegunaan%20UX/2-feedback.png) |
| 4.3 | Placeholder form | Formulir isian memiliki placeholder & label yang jelas | Placeholder dan label muncul di semua form | ✅ | ![Screenshot 17](screenshots/4.%20Kegunaan%20UX/3-tombol-interaktif.png) |
| 4.4 | Komponen interaktif | Cek semua tombol dan ikon berfungsi | ⚠️ Ditemukan beberapa tombol tidak berfungsi:<br>• Tombol lihat kata sandi (tidak aktif)<br>• Tombol forgot password (tidak merespons)<br>• Tombol reset tugas (tidak merespons)<br>• Tombol ganti warna tema di Settings (tidak aktif) | ❌ | ![Screenshot 18](screenshots/4.%20Kegunaan%20UX/4-ui-konsisten.png) |
| 4.5 | UI konsisten | Cek keseragaman font, warna, dan layout | Semua halaman menggunakan layout dan style konsisten | ✅ | ![Screenshot 19](screenshots/4.%20Kegunaan%20UX/5-responsif.png) |


---

## 📌 Catatan Umum:

- Semua pengujian dilakukan menggunakan **user: airin**.
- Aplikasi lolos uji untuk input ekstrem, edge cases, dan tetap stabil walau diuji berulang dan cepat.
- Pengujian dilakukan secara manual dengan browser Chrome pada resolusi layar laptop.

---

## 🏁 Kesimpulan Sementara

Pattern Testing menunjukkan bahwa aplikasi:
- ✅ Stabil dalam berbagai kondisi input
- ⚠ Perlu validasi lebih spesifik untuk input seperti HTML/script (walau tidak langsung berbahaya)

---

