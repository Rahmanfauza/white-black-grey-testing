🧪 Regression Testing – Task Manager App

Dokumen ini merangkum hasil pengujian regresi untuk memastikan bahwa perubahan pada sistem `created_at` tidak merusak fitur-fitur utama dalam aplikasi Task Manager.

---

📋 Rekap Hasil Pengujian

Berikut merupakan rekap hasil pengujian regresi secara ringkas dalam bentuk tabel:

| No | Test Case              | Status | Hasil yang Diharapkan                                                                 | Catatan                                                                 | Screenshot |
|----|------------------------|--------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------|------------|
| 1  | Login                  | ✅     | Redirect ke `/dashboard`, flash `"Login berhasil!"`                                   | Sesuai, hanya saja database agak lambat merekam input                  | ![Login](screenshots/login_success.png) |
| 2  | Register               | ✅     | Redirect ke `/login`, flash `"Registrasi berhasil"`                                   | Sesuai                                                                 | ![Register](screenshots/register_success.png) |
| 3  | Tambah Tugas           | ✅     | Data masuk DB, `created_at` format ISO, waktu tampil rapi                             | Sesuai, database lambat dalam menyimpan input                          | ![Tambah](screenshots/add_task_created_at.png) |
| 4  | Lihat Daftar Tugas     | ✅     | Tugas muncul dan tersortir dari terbaru                                                | Sesuai                                                                 | ![Dashboard](screenshots/dashboard_sorted.png) |
| 5  | Detail Tugas           | ✅     | Semua data tampil lengkap, format waktu rapi                                           | Sesuai                                                                 | ![Detail](screenshots/detail_task.png) |
| 6  | Update Status Tugas    | ✅     | Status berubah di DB, flash message muncul                                             | Sesuai, tapi sempat gagal akses DB                                     | ![Update](screenshots/update_status.png) |
| 7  | Hapus Tugas            | ✅     | Tugas terhapus dari DB dan dashboard                                                   | Sudah sesuai                                                           | ![Delete](screenshots/delete_task.png) |
| 8  | Logout                 | ❌     | Redirect ke `/login`, session terhapus                                                 | Nama user masih muncul setelah logout                                  | ![Logout](screenshots/logout_failed.png) |
