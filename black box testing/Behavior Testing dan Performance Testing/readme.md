# Pengujian Behavior Testing dan Performance testing 
## 1. Behavior Testing 
| No. | Skenario Uji                 | Input/Tindakan               | Ekspektasi                                                      | Screenshot                                        | Status  |
| --- | ---------------------------- | ---------------------------- | --------------------------------------------------------------- | ------------------------------------------------- | -------- |
| 1   | Registrasi User Baru         | Form diisi lengkap dan valid | User terdaftar, redirect ke login                               | ![Registrasi User Baru](screenshot/registrasi_user_baru.png)  | ✅ / ❌  |
| 2   | Registrasi Username Duplikat | Username sudah terdaftar     | Muncul error: "Username sudah digunakan"                        | ![Username Duplikat](screenshot/username_duplikat.png)        | ✅ / ❌  |
| 3   | Login Valid                  | Username & password benar    | Masuk ke dashboard                                              | ![Login Valid](screenshot/login_valid.png)                     | ✅ / ❌  |
| 4   | Login Invalid                | Username/password salah      | Muncul error: "Username atau password salah"                    | ![Login Invalid](screenshot/login_invalid.png)                 | ✅ / ❌  |
| 5   | Tambah Task                  | Isi form task dan submit     | Task muncul di dashboard, flash msg "Task berhasil ditambahkan" | ![Tambah Task](screenshot/tambah_task.png)                     | ✅ / ❌  |
| 6   | Akses Dashboard tanpa Login  | Buka /dashboard tanpa login  | Dialihkan ke halaman login                                      | ![Akses Tanpa Login](screenshot/akses_tanpa_login.png)         | ✅ / ❌  |

## 2. Performance Testing

