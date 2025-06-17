📋 Tabel Uji

| TC | Status  | Login | Data | Hasil yang Diharapkan             | Hasil Aktual                  | Sesuai? | Catatan |
|----|---------|-------|------|-----------------------------------|-------------------------------|---------|---------|
| 1  | pending | ✔️     | ✔️    | Tampil normal                     | Data tampil sesuai            | ✅      | Tampilan normal, data tampil sesuai status |
| 2  | selesai | ✔️     | ✔️    | Tampil dengan status selesai      | Data tampil dengan status "selesai" | ✅      | Status "selesai" tampil sesuai, tidak ada error |
| 3  | pending | ❌     | ✔️    | Redirect ke login                 | Dialihkan ke halaman login    | ✅      | Tidak bisa akses data, sistem langsung redirect |
| 4  | selesai | ❌     | ✔️    | Redirect ke login                 | Dialihkan ke halaman login    | ✅      | Mekanisme proteksi berjalan baik, user tidak bisa akses |
| 5  | pending | ✔️     | ❌    | Halaman valid, data kosong        | Halaman tampil tanpa error    | ✅      | UI menampilkan “no data” dengan benar |
| 6  | selesai | ✔️     | ❌    | Halaman valid, data kosong        | Halaman tampil tanpa error    | ✅      | Tampilan tetap stabil meskipun tidak ada task |
| 7  | pending | ❌     | ❌    | Redirect ke login                 | Dialihkan ke halaman login    | ✅      | Akses diblokir karena belum login dan tidak ada data |
| 8  | selesai | ❌     | ❌    | Redirect ke login                 | Dialihkan ke halaman login    | ✅      | Sistem aman dari akses tidak sah, langsung redirect |

📌 Keterangan Kolom
- **Status:** Status tugas yang dipilih
- **Login:** Kondisi apakah user sudah login
- **Data:** Apakah ada data task di database
- **Hasil yang Diharapkan:** Prediksi perilaku sistem
- **Hasil Aktual:** Berdasarkan pengujian manual
- **Sesuai?:** ✅ jika hasil sesuai ekspektasi
- **Catatan:** Tambahan info jika ada bug atau perilaku khusus
