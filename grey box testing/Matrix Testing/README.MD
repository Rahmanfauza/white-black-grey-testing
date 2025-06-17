📊 Matrix Testing  – Gray Box Testing

Matrix Testing dilakukan untuk menguji kombinasi dari kondisi login, ketersediaan data, dan status tugas (pending/selesai). Tujuan utama pengujian ini adalah untuk memastikan bahwa aplikasi dapat merespons dengan benar dalam berbagai skenario penggunaan, termasuk akses sah dan tidak sah.

🎯 Tujuan Pengujian
- Memastikan bahwa halaman task hanya bisa diakses oleh user yang telah login
- Menilai bagaimana aplikasi menangani kondisi data kosong
- Menguji tampilan status tugas (pending dan selesai) pada berbagai kondisi

---

🔍 Rangkuman Hasil

1. **Akses Login**
   - Sistem berhasil melindungi semua akses terhadap halaman task. Saat pengguna tidak login (baik ada maupun tidak ada data), aplikasi otomatis melakukan _redirect_ ke halaman login.
   - Hal ini terlihat konsisten di semua test case: TC3, TC4, TC7, dan TC8.

2. **Tampilan Data**
   - Saat pengguna login dan data tersedia (TC1 & TC2), aplikasi menampilkan data dengan status yang sesuai (pending atau selesai) tanpa error atau tampilan yang rusak.
   - Pada status “selesai”, indikator visual dan status berhasil ditampilkan dengan benar.

3. **Kondisi Tanpa Data**
   - Ketika user login namun database kosong (TC5 & TC6), aplikasi tetap menampilkan halaman yang valid dengan pesan bahwa tidak ada data yang tersedia.
   - Ini menunjukkan aplikasi telah menangani kondisi kosong secara _graceful_ tanpa menimbulkan error.

---

✅ Kesimpulan

Matrix Testing menunjukkan bahwa aplikasi telah memenuhi ekspektasi fungsional dasar terkait:
- Akses yang terproteksi
- Tampilan status tugas
- Penanganan data kosong

Tidak ditemukan _bug_ maupun _anomali_ pada pengujian ini. Semua skenario memberikan hasil yang sesuai dengan harapan, dan semua test case diberi label **✅ Sesuai**.

---

📎 Catatan Tambahan
- Sinkronisasi data antar tab belum real-time; perlu refresh manual
- Semua proteksi login bekerja sebagaimana mestinya
- Sistem mampu membedakan status tugas dan menampilkannya dengan benar
