# Laporan Pengujian: Comparison Testing & Decision Table Testing

## 1. Comparison Testing

Comparison Testing, sering juga disebut Back-to-Back Testing atau Comparative Testing, adalah jenis pengujian perangkat lunak di mana output atau perilaku dari aplikasi yang sedang diuji (AUT - Application Under Test) dibandingkan dengan output atau perilaku dari aplikasi referensi atau versi sebelumnya dari aplikasi yang sama.
**Tujuan**: Membandingkan perubahan fungsionalitas antara versi lama (`v1.0`) dan versi baru (`v2.0`) untuk fitur Register, Login, dan Add Task.

** Status:**
*   **Konsisten (✅)**: Perilaku sama antar versi atau perubahan sesuai yang diharapkan/disengaja.
*   **Berubah (⚠️)**: Perilaku berbeda antar versi, seringkali karena validasi atau fungsionalitas baru di `v2.0`.
*   **Regresi (❌)**: Perilaku di `v2.0` tidak sesuai harapan atau terjadi penurunan fungsionalitas (tidak ditemukan dalam data asli).

### 1.1. Fitur: Registrasi
**Perubahan Utama**: Batas panjang username dan password di `v2.0` (maksimal 12 karakter).

| ID             | Deskripsi Input (`username`, `email`, `password`) | Hasil v1.0 (Lama)      | Hasil v2.0 (Baru)                      | Status | Screenshot | Catatan                      |
|----------------|---------------------------------------------------|------------------------|----------------------------------------|--------|------------|------------------------------|
| TC-COMP-REG-001| Input valid standar                               | Registrasi Sukses      | Registrasi Sukses                      | ✅     |            | Perilaku konsisten           |
| TC-COMP-REG-002| Input dengan panjang > 12 karakter                | Registrasi Sukses      | Error: "Username/password max 12 kar." | ⚠️     | ![Image](https://github.com/user-attachments/assets/ac836606-cfc2-4ecb-af55-a02dfaeb170d)           | Validasi baru di v2.0        |

### 1.2. Fitur: Login
**Perubahan Utama**: Batas panjang input di `v2.0` (maksimal 12 karakter) dan pesan error.

| ID             | Deskripsi Input (`username`, `password`) | Hasil v1.0 (Lama) | Hasil v2.0 (Baru)                | Status | Screenshot | Catatan                      |
|----------------|------------------------------------------|-------------------|----------------------------------|--------|------------|------------------------------|
| TC-COMP-LOG-001| Input dengan panjang > 12 karakter       | Login Sukses      | Error: "Input max 12 karakter"   | ⚠️     | ![Image](https://github.com/user-attachments/assets/95a16132-6824-4759-a854-aac9e3a61cf7)           | Validasi baru di v2.0        |
| TC-COMP-LOG-002| Input valid standar                      | Login Sukses      | Login Sukses                     | ✅     |            | Tidak terpengaruh perubahan  |

### 1.3. Fitur: Tambah Tugas (Add Task)
*(Tidak ada perbandingan spesifik di data asli, diasumsikan tidak ada perubahan signifikan)*

| ID             | Deskripsi Input (`title`, `description`) | Hasil v1.0 (Lama) | Hasil v2.0 (Baru) | Status | Screenshot | Catatan                      |
|----------------|------------------------------------------|-------------------|-------------------|--------|------------|------------------------------|
| TC-COMP-ADD-001| Input valid standar                      | Task Ditambahkan  | Task Ditambahkan  | ✅     |            | Perilaku konsisten (asumsi)|

## 2. Decision Table Testing

Decision Table Testing adalah teknik desain test case black-box yang digunakan untuk menguji sistem dengan logika kondisional yang kompleks. Teknik ini membantu memastikan bahwa semua kombinasi kondisi input yang relevan dan aturan bisnis terkait telah dipertimbangkan.

### 2.1. Fitur: Registrasi
**Aturan:**
*   Username, email, password tidak boleh kosong.
*   Username dan email harus unik.
*   (Format email tidak divalidasi secara ketat dalam kode asli).

| ID            | Kondisi: Username Valid | Kondisi: Email Valid | Kondisi: Password Valid | Kondisi: Unik (User & Email) | Aksi: Expected Result           | Aksi: Actual Result (Observasi)         | Screenshot                                                                                           |
|---------------|-------------------------|----------------------|-------------------------|------------------------------|----------------------------------|-----------------------------------------|--------------------------------------------------------------------------------------------------------|
| TC-DEC-REG-001| True                    | True                 | True                    | True                         | Registrasi berhasil             | Registrasi berhasil                     | <img src="https://github.com/user-attachments/assets/dc63909f-bbb8-4256-b57c-a9b265c54885" width="250"/> |
| TC-DEC-REG-002| True                    | True                 | True                    | False                        | Error: Username/email duplikat  | Registrasi ditolak, pesan error muncul  | <img src="https://github.com/user-attachments/assets/d11b3836-0169-434e-ba35-7160ba7e5ca3" width="250"/> |
| TC-DEC-REG-003| False (Kosong)          | True                 | True                    | True                         | Error: Username kosong          | Registrasi tidak diproses               | <img src="https://github.com/user-attachments/assets/897d222c-64a2-49f1-a66d-4cd3006022fc" width="250"/> |
| TC-DEC-REG-004| True                    | False (Kosong/Invalid)| True                   | True                         | Error: Email kosong/invalid     | Registrasi tidak diproses               | <img src="https://github.com/user-attachments/assets/c4d9bdfb-c2aa-48ba-9cc2-50bb52fd2d1c" width="250"/> |
| TC-DEC-REG-005| True                    | True                 | False (Kosong)          | True                         | Error: Password kosong          | Registrasi tidak diproses               | <img src="https://github.com/user-attachments/assets/7406b1c8-759d-427b-98db-093d8831e634" width="250"/> |

### 2.2. Fitur: Login
**Aturan:**
*   Username dan password tidak boleh kosong.
*   Username harus terdaftar.
*   Password harus cocok.

| ID            | Kondisi: Username Kosong | Kondisi: Password Kosong | Kondisi: Username Terdaftar | Kondisi: Password Cocok | Aksi: Expected Result       | Aksi: Actual Result (Observasi)         | Screenshot                                                                                           |
|---------------|--------------------------|--------------------------|-----------------------------|-------------------------|-----------------------------|-----------------------------------------|--------------------------------------------------------------------------------------------------------|
| TC-DEC-LOG-001| False                    | False                    | True                        | True                    | Login berhasil              | Login berhasil                          | <img src="https://github.com/user-attachments/assets/b776e382-4e6a-4348-b428-29b912bb41f6" width="250"/> |
| TC-DEC-LOG-002| True                     | False                    | -                           | -                       | Error: Username kosong      | Login gagal, pesan error username       | <img src="https://github.com/user-attachments/assets/5afba048-e589-43a6-87ac-8d93644917d9" width="250"/> |
| TC-DEC-LOG-003| False                    | True                     | -                           | -                       | Error: Password kosong      | Login gagal, pesan error password       | <img src="https://github.com/user-attachments/assets/93572b99-0eb2-4d20-8f06-735b6ff29dba" width="250"/> |
| TC-DEC-LOG-004| False                    | False                    | False                       | -                       | Error: Username tidak ada   | Login gagal, pesan user tidak ditemukan | <img src="https://github.com/user-attachments/assets/93572b99-0eb2-4d20-8f06-735b6ff29dba" width="250"/> |
| TC-DEC-LOG-005| False                    | False                    | True                        | False                   | Error: Password salah       | Login gagal, pesan password salah       | <img src="https://github.com/user-attachments/assets/93572b99-0eb2-4d20-8f06-735b6ff29dba" width="250"/> |


### 2.3. Fitur: Tambah Tugas (Add Task)
**Aturan:**
*   Pengguna harus login (memiliki sesi aktif).
*   Title tidak boleh kosong.
*   Description boleh kosong.

| ID            | Kondisi: Login (Session Ada) | Kondisi: Title Kosong | Kondisi: Description Kosong | Aksi: Expected Result      | Aksi: Actual Result (Observasi)         | Screenshot                                                                                           |
|---------------|------------------------------|-----------------------|-----------------------------|----------------------------|-----------------------------------------|--------------------------------------------------------------------------------------------------------|
| TC-DEC-ADD-001| True                         | False                 | False                       | Task berhasil ditambahkan  | Task berhasil ditambahkan               | <img src="https://github.com/user-attachments/assets/f8786506-3ef7-4f53-91dc-3784a8b31c3f" width="250"/> |
| TC-DEC-ADD-002| True                         | True                  | False                       | Error: Title kosong        | Task tidak ditambahkan, error muncul    | <img src="https://github.com/user-attachments/assets/30d514c2-5ab0-4f10-8af2-afc2b504f1a0" width="250"/> |
| TC-DEC-ADD-003| False                        | False                 | False                       | Redirect ke halaman login  | Redirect ke login (akses ditolak)       |                                                                                 |
| TC-DEC-ADD-004| True                         | False                 | True                        | Task berhasil ditambahkan  | Task berhasil ditambahkan               | <img src="https://github.com/user-attachments/assets/6f3662dc-1155-415e-96cb-5d23ebfcd57d" width="250"/> |

