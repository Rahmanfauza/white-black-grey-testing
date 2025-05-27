🧩 Pattern Testing (Exploratory Testing)

Pattern Testing adalah pendekatan pengujian yang menekankan eksplorasi, kreativitas, dan intuisi tester. Dalam pengujian ini, tester tidak hanya mengikuti skrip pengujian formal, tapi juga mencari celah-celah bug dari interaksi pengguna nyata secara **tidak terduga**.

🎯 Tujuan Pengujian
- Mengidentifikasi bug yang tidak tertangkap oleh pengujian formal
- Menguji aplikasi dari sisi **pengalaman pengguna**, **stabilitas**, dan **ketahanan terhadap input aneh**

---

🧪 Tahapan & Skenario Pengujian

1. 🛠 Menguji Fungsional Dasar
| Langkah | Deskripsi |
|--------|-----------|
| 1 | Buka aplikasi dan login sebagai user |
| 2 | Tambah tugas baru (judul, deskripsi) |
| 3 | Edit tugas yang sudah ada |
| 4 | Hapus tugas |
| 5 | Logout dan login kembali untuk cek persistensi data |

📸 `screenshots/functional_test.png`

---

2. 🚧 Menguji Batasan & Skenario Tidak Terduga
| Skenario | Input | Ekspektasi |
|----------|-------|------------|
| Judul kosong | "" | Tidak boleh disimpan |
| Judul aneh | "@@@###" | Ditolak atau disimpan tanpa error |
| Deskripsi panjang | 10.000 karakter | Tetap tersimpan, tidak crash |
| Tahun tidak valid (di register) | "abc" | Validasi muncul |

📸 `screenshots/boundary_case.png`

---

3. ⚙️ Menguji Performa & Stabilitas
| Uji | Langkah | Hasil Diharapkan |
|-----|--------|------------------|
| Tambah 100+ tugas | Loop tambah data | Aplikasi tetap responsif |
| Edit & hapus berulang | 50x | Tidak crash |
| Akses bersamaan (multitab) | Login dari 2 tab | Tidak bentrok session |

📸 `screenshots/performance_test.png`

---

4. 🎨 Menguji Kegunaan & UX
| Uji | Pertanyaan |
|-----|------------|
| Antarmuka | Apakah mudah digunakan? |
| Navigasi | Apakah tombol dan menu jelas? |
| Feedback | Apakah error message muncul dengan tepat? |

📸 `screenshots/usability_feedback.png`

---

✅ Kesimpulan

Pattern Testing berhasil menemukan beberapa celah:
- Validasi input yang bisa ditingkatkan
- Aplikasi tetap stabil dengan banyak data
- UX cukup baik, tapi bisa lebih jelas untuk error handling

---
💡 Rekomendasi Perbaikan
- Tambahkan validasi karakter pada input
- Limit jumlah karakter maksimal
- Tambahkan pesan error eksplisit pada semua form


