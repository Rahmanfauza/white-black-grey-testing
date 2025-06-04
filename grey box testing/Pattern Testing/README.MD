# 🧩 Pattern Testing (Exploratory Testing)

Pattern Testing adalah pendekatan pengujian yang menekankan eksplorasi, kreativitas, dan intuisi tester. Dalam pengujian ini, tester tidak hanya mengikuti skrip pengujian formal, tapi juga mencari celah-celah bug dari interaksi pengguna nyata secara **tidak terduga**.

---

## 🎯 Tujuan Pengujian

- Mengidentifikasi bug yang tidak tertangkap oleh pengujian formal
- Menguji aplikasi dari sisi **pengalaman pengguna (UX)**, **stabilitas sistem**, dan **ketahanan terhadap input aneh**
- Menilai konsistensi antarmuka dan kenyamanan saat digunakan oleh pengguna akhir

---

## 🧪 Tahapan & Skenario Pengujian

### 1. 🛠 Menguji Fungsional Dasar

| Langkah | Deskripsi |
|--------|-----------|
| 1 | Login dengan username dan password yang valid |
| 2 | Tambah tugas baru (judul & deskripsi) |
| 3 | Lihat daftar tugas pada halaman dashboard dan all tasks |
| 4 | Update status tugas (Pending → Completed/In Progress) |
| 5 | Hapus salah satu tugas |
| 6 | Logout, lalu login kembali untuk memastikan data tetap ada |

| Screenshot | Deskripsi |
|------------|-----------|
| ![Fungsional Dasar](screenshots/1.%20Menguji%20Fungsional%20Dasar/1.png) | Pengujian fungsional dasar berhasil dilakukan |

---

### 2. 🚧 Menguji Batasan & Skenario Tidak Terduga

| Skenario | Input | Ekspektasi |
|----------|-------|------------|
| Judul kosong | `""` | Validasi muncul: tidak bisa disimpan |
| Judul aneh | `"@@@###🤯"` | Tidak error, tampil normal |
| Deskripsi panjang | 10.000+ karakter | Tetap tersimpan atau ditolak dengan sopan |
| Input script | `<script>alert(1)</script>` | Ditampilkan sebagai teks biasa, tidak dijalankan |

| Screenshot | Deskripsi |
|------------|-----------|
| ![Batasan](screenshots/2.%20Menguji%20Batasan/1.png) | Pengujian batasan dan input aneh berhasil dilakukan |

---

### 3. ⚙️ Menguji Performa & Stabilitas

| Uji | Langkah | Hasil Diharapkan |
|-----|--------|------------------|
| Tambah banyak tugas | Tambah 100 tugas berturut-turut | Aplikasi tetap stabil, tidak crash |
| Operasi berulang | Tambah, edit status, hapus tugas sebanyak 50 kali | Tidak ada error atau delay |
| Akses multitab | Login di 2 tab browser | Tidak logout paksa, data konsisten |

| Screenshot | Deskripsi |
|------------|-----------|
| ![Performa dan Stabilitas](screenshots/3.%20Performa%20dan%20Stabilitas/1.png) | Pengujian performa menambah tugas berhasil dilakukan |

---

🔁 **Hapus Berulang (Stress Test)**

Dilakukan kombinasi:
- Manual: 32 aksi edit & delete untuk verifikasi UI
- Script: 18 penghapusan tambahan dijalankan melalui DevTools Console

| Screenshot | Deskripsi |
|------------|-----------|
| ![Performa dan Stabilitas](screenshots/3.%20Performa%20dan%20Stabilitas/2.png) | Pengujian stress test (hapus berulang) berhasil dilakukan |

---

### 🔁 Akses Multitab – Hasil Pengujian

- ✅ Login berhasil di dua tab browser secara bersamaan
- ✅ Semua tindakan (tambah, hapus, edit) berjalan tanpa error
- ✅ Session tidak bentrok atau logout paksa
- ⚠️ Catatan: Saat membuat tugas di tab pertama, tab kedua **harus di-refresh** manual agar data terbaru muncul. Ini wajar karena aplikasi belum mendukung sinkronisasi real-time (misalnya via WebSocket/AJAX).

| Screenshot | Deskripsi |
|------------|-----------|
| ![Akses Multitab](screenshots/3.%20Performa%20dan%20Stabilitas/3.png) | Pengujian akses multitab berhasil dilakukan |

---

### 4. 🎨 Menguji Kegunaan & UX

Uji ini dilakukan untuk menilai apakah aplikasi dapat digunakan dengan nyaman oleh pengguna, tanpa membingungkan dan tetap konsisten secara tampilan.

| Uji                | Pertanyaan                                                      | Hasil Observasi                                               |
|--------------------|------------------------------------------------------------------|---------------------------------------------------------------|
| Navigasi           | Apakah menu Dashboard, Tasks, dan Settings mudah diakses dan tidak membingungkan? | ⚠️ Menu di **Dashboard** muncul dan mudah diakses. Di **Tasks**, menu kiri tidak tampil, namun tersedia tombol kembali di bagian bawah. Di **Settings**, tidak ada tombol eksplisit untuk kembali ke Dashboard; pengguna harus klik icon profil di kanan atas. |
| Feedback           | Apakah pesan error muncul saat input salah? (contoh: login gagal) | ✅ Flash message muncul dengan warna berbeda dan jelas |
| Komponen UI        | Apakah tombol, icon, dan form responsif serta konsisten?        | ⚠️ Beberapa komponen interaktif tidak berfungsi dengan baik: (1) tombol untuk melihat kata sandi tidak aktif, (2) tombol reset tugas tidak bekerja, (3) tombol warna tema tidak aktif, (4) tombol "Forgot Password" tidak memberikan respon |
| Tampilan Umum      | Apakah desain antarmuka bersih, modern, dan nyaman digunakan?    | ✅ Layout bersih, font konsisten, nyaman digunakan |
| Responsif          | Apakah tampilan tetap bagus di layar kecil / saat window dikecilkan? | ✅ UI tetap dapat digunakan, meskipun belum 100% mobile-optimized |

| Screenshot | Deskripsi |
|------------|-----------|
| ![Navigasi](screenshots/4.%20Kegunaan%20UX/1-navigasi.png) | Pengujian navigasi menu di Dashboard dan Tasks |
| ![Feedback](screenshots/4.%20Kegunaan%20UX/2-feedback.png) | Pengujian feedback error |
| ![Tombol Interaktif](screenshots/4.%20Kegunaan%20UX/3-tombol-interaktif.png) | Pengujian tombol interaktif yang tidak berfungsi |
| ![UI Konsisten](screenshots/4.%20Kegunaan%20UX/4-ui-konsisten.png) | Pengujian konsistensi UI |
| ![Responsif](screenshots/4.%20Kegunaan%20UX/5-responsif.png) | Pengujian responsifitas UI |

---

## ✅ Kesimpulan

Pattern Testing berhasil menemukan beberapa temuan penting:

- ✅ Aplikasi stabil untuk berbagai kombinasi input
- ✅ Tidak crash saat digunakan secara intensif atau dalam jumlah besar
- ✅ Tampilan dan navigasi antarmuka cukup intuitif
- ⚠️ Tidak tersedia fitur untuk mengedit **judul dan deskripsi** tugas, hanya status yang bisa diubah
- ⚠️ Validasi form perlu ditingkatkan terutama untuk karakter input dan batasan panjang
- ⚠️ Beberapa komponen interaktif seperti tombol lihat password, reset tugas, dan pengaturan warna belum berfungsi

---

## 💡 Rekomendasi Perbaikan

- Tambahkan validasi karakter dan batas panjang input (misal: max 255 karakter)
- Tambahkan pesan error yang lebih informatif di semua form (judul kosong, input tidak valid)
- Pertimbangkan menambahkan fitur edit judul dan deskripsi untuk fleksibilitas pengguna
- Perbaiki fungsionalitas tombol-tombol interaktif yang tidak bekerja (lihat password, reset, forgot password)
- Gunakan alert/feedback yang lebih kontras dan konsisten saat aksi berhasil/gagal
