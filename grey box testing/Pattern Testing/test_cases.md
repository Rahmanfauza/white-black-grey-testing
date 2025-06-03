🧩 Pattern Testing – Test Case Documentation

Dokumentasi ini berisi rangkaian pengujian eksploratif (Pattern Testing) yang dilakukan pada aplikasi **Task Manager**. Fokus utama pengujian ini adalah mengeksplorasi fungsi dari antarmuka, input tak biasa, validasi form, performa aplikasi, dan pengalaman pengguna (UX).

---

✅ 1. Test Case – Fungsional Dasar

| No | Skenario | Langkah | Hasil yang Diharapkan | Status |
|----|----------|--------|------------------------|--------|
| 1.1 | Login user | Input username & password yang benar | Halaman dashboard ditampilkan dengan notifikasi “Login berhasil” | ✅ |
| 1.2 | Logout user | Klik tombol logout | Redirect ke halaman login, pesan “Anda telah logout” muncul | ✅ |
| 1.3 | Tambah tugas | Klik "Add Task", isi judul dan deskripsi, submit | Tugas tampil di dashboard | ✅ |
| 1.4 | Lihat semua tugas | Klik menu "Tasks" | Semua tugas ditampilkan dengan status dan waktu | ✅ |
| 1.5 | Update status tugas | Klik tombol update status (Pending → Completed) | Status berubah dan tersimpan | ✅ |
| 1.6 | Hapus tugas | Klik tombol delete | Tugas hilang dari daftar | ✅ |

---

🚧 2. Test Case – Batasan & Input Aneh

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|------------------------|--------|
| 2.1 | Judul kosong | "" | Validasi muncul: “Judul wajib diisi” | ✅ |
| 2.2 | Deskripsi kosong | (biarkan kosong) | Tetap tersimpan tanpa error | ✅ |
| 2.3 | Input sangat panjang | >10.000 karakter di deskripsi | Tidak crash, data tersimpan atau ditolak sopan | ✅ |
| 2.4 | Karakter aneh di judul | "!@#*🤯🎉" | Tidak error, tetap ditampilkan dengan aman | ✅ |
| 2.5 | Input skrip (XSS attempt) | `<script>alert(1)</script>` | Teks ditampilkan sebagai string biasa, tidak dieksekusi | ✅ |

---

⚙️ 3. Test Case – Performa dan Stabilitas

| No | Skenario | Langkah | Hasil yang Diharapkan | Status |
|----|----------|--------|------------------------|--------|
| 3.1 | Tambah banyak tugas | Tambah 100 tugas via form/manual | Aplikasi tetap responsif | ✅ |
| 3.2 | Operasi berulang | Tambah, edit, hapus secara berurutan 10x | Tidak freeze/crash | ✅ |
| 3.3 | Akses multitab | Login dari 2 tab | Tidak logout paksa, data konsisten | ✅ |

---

🎨 4. Test Case – Usability & Pengalaman Pengguna

| No | Skenario | Fokus | Hasil yang Diharapkan | Status |
|----|----------|-------|------------------------|--------|
| 4.1 | Navigasi menu | Klik Dashboard, Tasks, Settings | Menu aktif sesuai yang diklik | ✅ |
| 4.2 | Feedback error | Input password salah di login | Pesan error muncul dengan warna yang jelas | ✅ |
| 4.3 | Placeholder form | Formulir isian memiliki placeholder & label yang jelas | Mudah dipahami user | ✅ |
| 4.4 | Komponen interaktif | Icon tombol lihat kata sandi dan detail dapat diklik | Fungsi berjalan sesuai aksi | ❌ |
| 4.5 | UI konsisten | Semua halaman pakai warna, font, dan gaya seragam | Tampilan enak dilihat, tidak membingungkan | ✅ |

---

📌 Catatan Umum:

- Semua pengujian dilakukan menggunakan **user: airin**.
- Aplikasi lolos uji untuk input ekstrem, edge cases, dan tetap stabil walau diuji berulang dan cepat.
- Pengujian dilakukan secara manual dengan browser Chrome pada resolusi layar laptop.

---

🏁 Kesimpulan Sementara

Pattern Testing menunjukkan bahwa aplikasi:
- ✅ Stabil dalam berbagai kondisi input
- ⚠ Perlu validasi lebih spesifik untuk input seperti HTML/script (walau tidak langsung berbahaya)

---

