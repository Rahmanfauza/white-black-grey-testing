🧩 Pattern Testing (Exploratory Testing)

Pattern Testing adalah pendekatan pengujian yang menekankan eksplorasi, kreativitas, dan intuisi tester. Dalam pengujian ini, tester tidak hanya mengikuti skrip pengujian formal, tapi juga mencari celah-celah bug dari interaksi pengguna nyata secara **tidak terduga**.

---

🎯 Tujuan Pengujian

- Mengidentifikasi bug yang tidak tertangkap oleh pengujian formal
- Menguji aplikasi dari sisi **pengalaman pengguna (UX)**, **stabilitas sistem**, dan **ketahanan terhadap input aneh**
- Menilai konsistensi antarmuka dan kenyamanan saat digunakan oleh pengguna akhir

---

🧪 Tahapan & Skenario Pengujian

1. 🛠 Menguji Fungsional Dasar

| Langkah | Deskripsi |
|--------|-----------|
| 1 | Login dengan username dan password yang valid |
| 2 | Tambah tugas baru (judul & deskripsi) |
| 3 | Lihat daftar tugas pada halaman dashboard dan all tasks |
| 4 | Update status tugas (Pending → Completed/In Progress) |
| 5 | Hapus salah satu tugas |
| 6 | Logout, lalu login kembali untuk memastikan data tetap ada |

📸 [Screenshot Pengujian Fungsional Dasar](screenshots/1.%20Menguji%20Fungsional%20Dasar/1.png)

---

### 2. 🚧 Menguji Batasan & Skenario Tidak Terduga

| Skenario | Input | Ekspektasi |
|----------|-------|------------|
| Judul kosong | `""` | Validasi muncul: tidak bisa disimpan |
| Judul aneh | `"@@@###🤯"` | Tidak error, tampil normal |
| Deskripsi panjang | 10.000+ karakter | Tetap tersimpan atau ditolak dengan sopan |
| Input script | `<script>alert(1)</script>` | Ditampilkan sebagai teks biasa, tidak dijalankan |

📸 `screenshots/2.%20Menguji%20Batasan/1.png`

---

3. ⚙️ Menguji Performa & Stabilitas

| Uji | Langkah | Hasil Diharapkan |
|-----|--------|------------------|
| Tambah banyak tugas | Tambah 100 tugas berturut-turut | Aplikasi tetap stabil, tidak crash |
| Operasi berulang | Tambah, edit status, hapus tugas sebanyak 50 kali | Tidak ada error atau delay |
| Akses multitab | Login di 2 tab browser | Tidak logout paksa, data konsisten |

🔁 catatan untuk melakukan Otomatis Tambah 100 Data Tugas

Untuk melakukan pengujian performa penambahan data massal, saya menggunakan script berikut melalui **DevTools Console** di browser:

```javascript
for (let i = 1; i <= 100; i++) {
  fetch("/tasks/add", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded"
    },
    body: `title=Task+${i}&description=Deskripsi+${i}`
  });
}

📸 `screenshots/3.%20Performa%20dan%20Stabilitas/1.png`

---



4. 🎨 Menguji Kegunaan & UX

| Uji | Pertanyaan |
|-----|------------|
| Navigasi | Apakah menu Dashboard, Tasks, dan Settings mudah diakses dan tidak membingungkan? |
| Feedback | Apakah pesan error muncul saat input salah? (contoh: login gagal) |
| Komponen UI | Apakah tombol, icon, dan form responsif serta konsisten? |
| Tampilan Umum | Apakah desain antarmuka bersih, modern, dan nyaman digunakan? |

📸 `screenshots/4.%20Kegunaan%20UX/1.png`

---

✅ Kesimpulan

Pattern Testing berhasil menemukan beberapa temuan penting:

- ✅ Aplikasi stabil untuk berbagai kombinasi input
- ✅ Tidak crash saat digunakan secara intensif atau dalam jumlah besar
- ✅ Tampilan dan navigasi antarmuka cukup intuitif
- ⚠️ Tidak tersedia fitur untuk mengedit **judul dan deskripsi** tugas, hanya status yang bisa diubah
- ⚠️ Validasi form perlu ditingkatkan terutama untuk karakter input dan batasan panjang
- ⚠️ Halaman awal untuk melihat kata sandi tidak bisa di klik

---

💡 Rekomendasi Perbaikan

- Tambahkan validasi karakter dan batas panjang input (misal: max 255 karakter)
- Tambahkan pesan error yang lebih informatif di semua form (judul kosong, input tidak valid)
- Pertimbangkan menambahkan fitur edit judul dan deskripsi untuk fleksibilitas pengguna
- Gunakan alert/feedback yang lebih kontras saat aksi berhasil/gagal



