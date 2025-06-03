# Pengujian Comparison Testing dan Decision Table Testing
## 1. Sample Testing
Sample Testing adalah pendekatan pengujian di mana hanya sebagian (sampel) dari fungsionalitas, data, atau skenario yang mungkin dari suatu aplikasi yang diuji, bukan keseluruhan. Tujuannya adalah untuk mendapatkan indikasi kualitas atau kinerja sistem secara keseluruhan dengan usaha pengujian yang terbatas.

| No. | Fitur               | Data Masukan                                                       | Output yang Diharapkan                                  | Status (✔️/❌) | Tangkapan Layar                                                                                      |
|-----|---------------------|--------------------------------------------------------------------|----------------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------|
| 1   | Registrasi Pengguna | username: `testuser`, email: `test@mail.com`, password: `Test123!` | Pengguna berhasil terdaftar, diarahkan ke halaman login | ✔️             | <img src="https://github.com/user-attachments/assets/abf112d3-60d5-41e4-b9e6-224e25d4760e" width="250"/> |
| 2   | Login Pengguna      | username: `testuser`, password: `Test123!`                         | Pengguna berhasil login, diarahkan ke dashboard         | ✔️             | <img src="https://github.com/user-attachments/assets/2afa4397-1c73-4704-8973-fa0ff9e24435" width="250"/> |
| 3   | Tambah Tugas        | judul: `Beli Belanjaan`, deskripsi: `Telur, susu`                  | Tugas muncul di dashboard dengan data yang sesuai       | ✔️             | <img src="https://github.com/user-attachments/assets/961c293f-07de-4925-985a-34e2dbf6e11a" width="250"/> |
| 4   | Lihat Detail Tugas  | Klik tugas `Beli Belanjaan`                                        | Halaman detail tugas menampilkan informasi yang benar   | ✔️             | <img src="https://github.com/user-attachments/assets/e742dbd7-2662-4c91-9a39-a70327ffe8cc" width="250"/> |
| 5   | Perbarui Status     | Ubah status menjadi `selesai`                                      | Status diperbarui, pesan sukses ditampilkan             | ✔️             | <img src="https://github.com/user-attachments/assets/12132cda-b880-435f-8a2d-7a8e2a91aee5" width="250"/> |
| 6   | Hapus Tugas         | Klik hapus pada `Beli Belanjaan`                                   | Tugas dihapus, pesan sukses ditampilkan                 | ✔️             | <img src="https://github.com/user-attachments/assets/52d3d8e1-8a8a-4436-8552-30cf00debcb9" width="250"/> |
| 7   | Logout              | -                                                                  | Pengguna berhasil logout, diarahkan ke halaman login    | ✔️             | <img src="https://github.com/user-attachments/assets/df74ec54-2eb2-47da-9f5d-2ce5af8862b8" width="250"/> |


## 2. Robustness Testing
Robustness Testing adalah jenis pengujian fungsional yang bertujuan untuk memverifikasi seberapa baik sistem perangkat lunak dapat menangani kondisi input yang tidak valid, kondisi lingkungan yang tidak terduga, atau situasi stres lainnya tanpa mengalami kegagalan (crash) atau perilaku yang tidak benar.

| No. | Feature            | Input Data                                                         | Expected Output                                         | Status (✔️/❌) | Screenshot                          |
| --- | ------------------ | ------------------------------------------------------------------ | ------------------------------------------------------- | ------------- | ---------------------------------------------- |
| 1   | User Registration  | username: \`\`, email: `test@mail.com`, password: `Test123!`       | Registration fails with error message                   |               | (screenshot/registration\_empty\_username.png) |
| 2   | User Registration  | username: `longusername...` (1000 chars)                           | Application handles gracefully, limit enforced          |               | (screenshot/registration\_long\_username.png)  |
| 3   | User Registration  | username: `testuser`, email: `invalid-email`, password: `Test123!` | Registration fails, error message shown                 |               | (screenshot/registration\_invalid\_email.png)  |
| 4   | Add Task           | title: `@#$%^&*()_+`, description: `123`                           | Task is added, special characters accepted or sanitized |               | (screenshot/add\_task\_special\_chars.png)     |
| 5   | Add Task           | title: (empty), description: `123`                                 | Task creation fails, error message shown                |               | (screenshot/add\_task\_empty\_title.png)       |
| 6   | Update Task Status | status: `completed<script>alert(1)</script>`                       | Input sanitized, XSS not executed                       |               | (screenshot/xss\_attempt.png)                  |
| 7   | SQL Injection Test | username: `' OR '1'='1`, password: `abc`                           | Login fails, SQL injection prevented                    |               | (screenshot/sql\_injection\_attempt.png)       |
| 8   | Large Input Test   | description: 10,000 characters                                     | Application remains stable, data stored or truncated    |               | (screenshot/large\_input\_test.png)            |
