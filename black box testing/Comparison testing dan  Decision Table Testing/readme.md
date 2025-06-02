# Laporan Pengujian: Comparison Testing & Decision Table Testing

Berikut adalah format ulang dari hasil pengujian Comparison Testing dan Decision Table Testing yang Anda berikan, dirapikan agar lebih terstruktur dan konsisten, termasuk penambahan kolom Screenshot dan standarisasi ID kasus uji.

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
| TC-COMP-REG-002| Input dengan panjang > 12 karakter                | Registrasi Sukses      | Error: "Username/password max 12 kar." | ⚠️     |            | Validasi baru di v2.0        |

### 1.2. Fitur: Login
**Perubahan Utama**: Batas panjang input di `v2.0` (maksimal 12 karakter) dan pesan error.

| ID             | Deskripsi Input (`username`, `password`) | Hasil v1.0 (Lama) | Hasil v2.0 (Baru)                | Status | Screenshot | Catatan                      |
|----------------|------------------------------------------|-------------------|----------------------------------|--------|------------|------------------------------|
| TC-COMP-LOG-001| Input dengan panjang > 12 karakter       | Login Sukses      | Error: "Input max 12 karakter"   | ⚠️     |            | Validasi baru di v2.0        |
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

| ID            | Kondisi: Username Valid | Kondisi: Email Valid | Kondisi: Password Valid | Kondisi: Unik (User & Email) | Aksi: Expected Result         | Aksi: Actual Result (Observasi)         | Screenshot |
|---------------|-------------------------|----------------------|-------------------------|------------------------------|-------------------------------|-----------------------------------------|------------|
| TC-DEC-REG-001| True                    | True                 | True                    | True                         | Registrasi berhasil           | Registrasi berhasil                     |            |
| TC-DEC-REG-002| True                    | True                 | True                    | False                        | Error: Username/email duplikat| Registrasi ditolak, pesan error muncul  |            |
| TC-DEC-REG-003| False (Kosong)          | True                 | True                    | True                         | Error: Username kosong        | Registrasi tidak diproses               |            |
| TC-DEC-REG-004| True                    | False (Kosong/Invalid)| True                    | True                         | Error: Email kosong/invalid   | Registrasi tidak diproses               |            |
| TC-DEC-REG-005| True                    | True                 | False (Kosong)          | True                         | Error: Password kosong        | Registrasi tidak diproses               |            |

### 2.2. Fitur: Login
**Aturan:**
*   Username dan password tidak boleh kosong.
*   Username harus terdaftar.
*   Password harus cocok.

| ID            | Kondisi: Username Kosong | Kondisi: Password Kosong | Kondisi: Username Terdaftar | Kondisi: Password Cocok | Aksi: Expected Result     | Aksi: Actual Result (Observasi)         | Screenshot |
|---------------|--------------------------|--------------------------|-----------------------------|-------------------------|---------------------------|-----------------------------------------|------------|
| TC-DEC-LOG-001| False                    | False                    | True                        | True                    | Login berhasil            | Login berhasil                          |            |
| TC-DEC-LOG-002| True                     | False                    | -                           | -                       | Error: Username kosong    | Login gagal, pesan error username       |            |
| TC-DEC-LOG-003| False                    | True                     | -                           | -                       | Error: Password kosong    | Login gagal, pesan error password       |            |
| TC-DEC-LOG-004| False                    | False                    | False                       | -                       | Error: Username tidak ada | Login gagal, pesan user tidak ditemukan |            |
| TC-DEC-LOG-005| False                    | False                    | True                        | False                   | Error: Password salah     | Login gagal, pesan password salah       |            |

### 2.3. Fitur: Tambah Tugas (Add Task)
**Aturan:**
*   Pengguna harus login (memiliki sesi aktif).
*   Title tidak boleh kosong.
*   Description boleh kosong.

| ID            | Kondisi: Login (Session Ada) | Kondisi: Title Kosong | Kondisi: Description Kosong | Aksi: Expected Result      | Aksi: Actual Result (Observasi)         | Screenshot |
|---------------|------------------------------|-----------------------|-----------------------------|----------------------------|-----------------------------------------|------------|
| TC-DEC-ADD-001| True                         | False                 | False                       | Task ditambahkan           | Task ditambahkan                        |            |
| TC-DEC-ADD-002| True                         | True                  | False                       | Error: Title kosong        | Task tidak disimpan, flash error muncul |            |
| TC-DEC-ADD-003| False                        | False                 | False                       | Redirect ke login          | Diarahkan ke halaman login              |            |
| TC-DEC-ADD-004| True                         | False                 | True                        | Task ditambahkan           | Task ditambahkan                        |            |
