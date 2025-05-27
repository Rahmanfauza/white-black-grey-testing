# Comparison Testing Report

## **Fitur yang Diuji**: Register, Login, dan Add Task  
**Tujuan**: Membandingkan perubahan fungsionalitas antara versi lama (`v1.0`) dan versi baru (`v2.0`).

---

### **1. Fitur Register**
#### **Perubahan**: Batas panjang username dan password (12 karakter)  
| **Test ID** | **Input** (`username`, `email`, `password`)       | **Versi Lama (`v1.0`)**       | **Versi Baru (`v2.0`)**        | **Status** | **Catatan**                  |
|-------------|--------------------------------------------------|-------------------------------|--------------------------------|------------|------------------------------|
| CT-R1       | `("userbaru", "baru@mail.com", "pass123")`       | Bisa >12 karakter            | Dibatasi 12 karakter           | ✅         | Perubahan fungsionalitas     |
| CT-R2       | `("userbaru1234567", "valid@mail.com", "pass1234567890")` | Diterima | Error: "Username/password max 12 karakter" | ⚠️ | Validasi baru |

---

### **2. Fitur Login**
#### **Perubahan**: Batas panjang input dan pesan error  
| **Test ID** | **Input** (`username`, `password`) | **Versi Lama (`v1.0`)**       | **Versi Baru (`v2.0`)**        | **Status** | **Catatan**                  |
|-------------|------------------------------------|-------------------------------|--------------------------------|------------|------------------------------|
| CT-L1       | `("user1234567", "pass1234567890")` | Diterima                     | Error: "Input max 12 karakter" | ⚠️       | Validasi baru di `v2.0`      |
| CT-L2       | `("user1", "pass1")`               | Sukses                        | Sukses                         | ✅         | Tidak terpengaruh perubahan  |

---


### **Legenda Status**  
- ✅ **Consistent**: Perilaku sama atau perubahan disengaja.  
- ⚠️ **Changed**: Perilaku berubah karena validasi baru.  

---

# 📋 Decision Table Testing – Aplikasi Manajemen Tugas (Flask)

- Register
- Login
- Add Task

---
## ✅ Fitur 1: Register

### Aturan
- Username, email, dan password tidak boleh kosong.
- Email dan username harus unik.
- (Catatan: format email **tidak divalidasi** di kode.)

### Tabel

| TC  | Username Valid | Email Valid | Password Valid | Unik (Username & Email) | Expected Result               | Actual Result                       |
|-----|----------------|-------------|----------------|--------------------------|-------------------------------|--------------------------------------------------|
| TC1 | ✔️              | ✔️           | ✔️              | ✔️                        | ✅ Registrasi berhasil         | ❌ Tidak ada                                       |
| TC2 | ✔️              | ✔️           | ✔️              | ❌                        | ❌ Username/email duplikat    | ✅ Registrasi ditolak dengan pesan kesalahan     |
| TC3 | ❌              | ✔️           | ✔️              | ✔️                        | ❌ Username kosong             | ✅ Registrasi tidak diproses                     |
| TC4 | ✔️              | ❌           | ✔️              | ✔️                        | ❌ Email kosong/invalid        | ✅ Registrasi tidak diproses                     |
| TC5 | ✔️              | ✔️           | ❌              | ✔️                        | ❌ Password kosong             | ✅ Registrasi tidak diproses                     |

---

## ✅ Fitur 2: Login

### Aturan 
- Username dan password tidak boleh kosong.
- Username harus terdaftar.
- Password harus cocok.

### Tabel 

| TC  | Username Kosong | Password Kosong | Username Terdaftar | Password Cocok | Expected Result        | Actual Result                 |
|-----|------------------|------------------|---------------------|----------------|-------------------------|------------------------------------------------|
| TC1 | ❌               | ❌               | ✔️                  | ✔️              | ✅ Login berhasil       | ❌ Tidak ada                                    |
| TC2 | ✔️               | ❌               | -                   | -              | ❌ Username kosong      | ✅ Login gagal dengan pesan error              |
| TC3 | ❌               | ✔️               | -                   | -              | ❌ Password kosong      | ✅ Login gagal dengan pesan error              |
| TC4 | ❌               | ❌               | ❌                  | -              | ❌ Username tidak ada   | ✅ Login gagal dengan pesan: user tidak ditemukan |
| TC5 | ❌               | ❌               | ✔️                  | ❌              | ❌ Password salah       | ✅ Login gagal dengan pesan: password salah    |

---

## ✅ Fitur 3: Add Task

### Aturan
- Pengguna harus login.
- Title tidak boleh kosong.
- Description boleh kosong.

### Tabel 

| TC  | Login (Session Ada) | Title Kosong | Description Kosong | Expected Result               | Actual Result                |
|-----|----------------------|---------------|---------------------|-------------------------------|----------------------------------------------|
| TC1 | ✔️                   | ❌            | ❌                  | ✅ Task ditambahkan           | ❌ Tidak ada                                   |
| TC2 | ✔️                   | ✔️            | ❌                  | ❌ Gagal – Title kosong        | ✅ Task tidak disimpan, flash error muncul     |
| TC3 | ❌                   | ❌            | ❌                  | 🔁 Redirect ke login          | ✅ Tidak ada akses, diarahkan ke halaman login |
| TC4 | ✔️                   | ❌            | ✔️                  | ✅ Task ditambahkan           | ❌ Tidak ada                                   |

---
