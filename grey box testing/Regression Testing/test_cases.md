# 🧪 Regression Testing – Task Manager App

Dokumen ini merangkum hasil pengujian regresi untuk memastikan bahwa perubahan pada sistem `created_at` tidak merusak fitur-fitur utama dalam aplikasi Task Manager.

---

## 📋 Rekap Hasil Pengujian

Berikut merupakan rekap hasil pengujian regresi secara ringkas dalam bentuk tabel:

| No | Test Case              | Status | Hasil yang Diharapkan                                                                 | Catatan                                                                 | Screenshot |
|----|------------------------|--------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------|------------|
| 1  | Login                  | ✅     | Redirect ke `/dashboard`, flash `"Login berhasil!"`                                   | Sesuai, hanya saja database agak lambat merekam input                  | <img src="https://github.com/user-attachments/assets/8ee18fc3-cae2-465b-b856-b9d75bf49bad" width="300"/> <img src="https://github.com/user-attachments/assets/b3dd46a3-c263-4dcb-b381-7f80070b5b35" width="300"/> |
| 2  | Register               | ✅     | Redirect ke `/login`, flash `"Registrasi berhasil"`                                   | Sesuai                                                                 | <img src="https://github.com/user-attachments/assets/d6c02c5a-aac9-4d1b-bb7c-cba12d8cb19d" width="300"/> |
| 3  | Tambah Tugas           | ✅     | Data masuk DB, `created_at` format ISO, waktu tampil rapi                             | Sesuai, database lambat dalam menyimpan input                          | <img src="https://github.com/user-attachments/assets/177708a2-6a33-443e-9d18-c6dd797b98c8" width="300"/> |
| 4  | Lihat Daftar Tugas     | ✅     | Tugas muncul dan tersortir dari terbaru                                                | Sesuai                                                                 | <img src="https://github.com/user-attachments/assets/2db75c4c-663b-4da6-95d4-66da9a782c69" width="300"/> |
| 5  | Detail Tugas           | ✅     | Semua data tampil lengkap, format waktu rapi                                           | Sesuai                                                                 | <img src="https://github.com/user-attachments/assets/52eeac38-b6ea-49b9-8a8e-a0350eca90ec" width="300"/> |
| 6  | Update Status Tugas    | ✅     | Status berubah di DB, flash message muncul                                             | Sesuai, tapi sempat gagal akses DB                                     | <img src="https://github.com/user-attachments/assets/12559d35-8794-4556-a8fe-b48af7f93c2d" width="300"/> |
| 7  | Hapus Tugas            | ✅     | Tugas terhapus dari DB dan dashboard                                                   | Sudah sesuai                                                           | <img src="https://github.com/user-attachments/assets/fe2e9654-fee9-40b5-8ba3-f7d7cd026dee" width="300"/> |
| 8  | Logout                 | ❌     | Redirect ke `/login`, session terhapus                                                 | Nama user masih muncul setelah logout                                  | <img src="https://github.com/user-attachments/assets/0bdfb4b6-7f99-4235-8fb6-094986e02013" width="300"/> |
