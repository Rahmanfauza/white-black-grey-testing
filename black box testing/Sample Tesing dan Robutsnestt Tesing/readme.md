# Pengujian Comparison Testing dan Decision Table Testing
## 1. Sample Testing
Sample Testing adalah pendekatan pengujian di mana hanya sebagian (sampel) dari fungsionalitas, data, atau skenario yang mungkin dari suatu aplikasi yang diuji, bukan keseluruhan. Tujuannya adalah untuk mendapatkan indikasi kualitas atau kinerja sistem secara keseluruhan dengan usaha pengujian yang terbatas.



## 1. Sample Testing

| Test Case | Langkah-langkah | Expected Result | Status |
|-----------|----------------|-----------------|--------|
| Registrasi & Login Valid | 1. Register user baru<br>2. Login dengan user tersebut | Registrasi sukses, login sukses, redirect ke dashboard |  |
| CRUD Tugas | 1. Buat tugas<br>2. Lihat detail<br>3. Update status<br>4. Hapus tugas | Setiap operasi sukses dengan feedback sesuai |  |
| View All Tasks | 1. Buat beberapa tugas<br>2. Buka halaman All Tasks | Semua tugas tampil urut kronologis |  |
| Manajemen Session | 1. Login<br>2. Logout<br>3. Akses dashboard | Redirect ke login saat akses tanpa otentikasi |  |

---

## 2. Robustness Testing

| Modul/Fitur | Test Case | Input | Expected Output | Status |
|-------------|----------|-------|-----------------|--------|
| **Login** | Input kosong | Username="", Password="" | Error message, tidak login |  |
|  | SQL Injection | Username="admin' --", Password="anything" | Error message, tidak login |  |
|  | Input panjang | Username=5000 chars, Password=5000 chars | Error message, tidak login |  |
| **Registrasi** | Email tidak valid | Email="notanemail" | Error message, registrasi gagal |  |
|  | Username sudah ada | Username="existinguser" | Error "Username sudah digunakan" |  |
| **Tugas** | Judul kosong | Title="", Description="desc" | Error message, tugas tidak dibuat |  |
|  | XSS Injection | Title="<script>alert('xss')</script>" | Script tags di-escape di output |  |
|  | Status tidak valid | Status="invalid_status" | Error message atau tidak ada perubahan |  |

---
## Test Data Samples

### Data Valid
| Modul | Field | Contoh Input |
|-------|-------|--------------|
| Registrasi | Username | "johndoe" |
|  | Email | "john@example.com" |
|  | Password | "SecurePass123!" |
| Tugas | Title | "Complete project docs" |
|  | Description | "Finish API docs by Friday" |

### Data Tidak Valid
| Modul | Field | Contoh Input | Expected Error |
|-------|-------|--------------|----------------|
| Registrasi | Username | "admin" (sudah ada) | "Username sudah digunakan" |
|  | Email | "invalid-email" | "Email tidak valid" |
|  | Password | "" | "Password tidak boleh kosong" |
| Tugas | Title | "" | "Judul tidak boleh kosong" |

---
