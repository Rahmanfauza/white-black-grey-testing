# Boundary Value Analysis (BVA) dan Equivalence Partitioning (EP)

## 📌 Pendahuluan
Dokumen ini mencakup skenario pengujian berbasis Black Box untuk aplikasi manajemen tugas berbasis Flask. Dua pendekatan digunakan:
- **Equivalence Partitioning (EP)**
- **Boundary Value Analysis (BVA)**

Fokus pengujian pada:
- Register
- Login
- Menambahkan Tugas (Task)
- Update Status Tugas

---

## 1. 🔐 Form Registrasi

### 🎯 Equivalence Partitioning (EP)

| No | Input                         | Kelas Ekivalen         | Hasil yang Diharapkan             | 📸 Screenshot |
|----|-------------------------------|-------------------------|------------------------------------|---------------|
| 1  | username: `user1`             | valid                   | Registrasi berhasil               |               |
| 2  | username: kosong              | invalid (kosong)        | Gagal, flash error ditampilkan    |               |
| 3  | email: `user@mail.com`        | valid email             | Registrasi berhasil               |               |
| 4  | email: `usermail.com`         | invalid (format email)  | Gagal, flash error ditampilkan    |               |
| 5  | password: `abc123`            | valid                   | Registrasi berhasil               |               |

### 📏 Boundary Value Analysis (BVA)

| No | Input            | Nilai Uji         | Hasil yang Diharapkan         | 📸 Screenshot |
|----|------------------|-------------------|-------------------------------|---------------|
| 1  | username length  | 1 karakter        | Registrasi berhasil           |               |
| 2  | username length  | 0 karakter        | Gagal, input kosong           |               |
| 3  | username length  | 255 karakter      | Registrasi berhasil           |               |
| 4  | email length     | 0 karakter        | Gagal, input kosong           |               |

---

## 2. 🔓 Form Login

### 🎯 Equivalence Partitioning (EP)

| No | Input                     | Kelas Ekivalen     | Hasil yang Diharapkan           | 📸 Screenshot |
|----|---------------------------|---------------------|----------------------------------|---------------|
| 1  | username + password valid | valid combo         | Login berhasil                  |               |
| 2  | username salah            | invalid username    | Gagal login                     |               |
| 3  | password salah            | invalid password    | Gagal login                     |               |
| 4  | username kosong           | invalid kosong      | Gagal login                     |               |

---

## 3. 📥 Tambah Tugas

### 🎯 Equivalence Partitioning (EP)

| No | Input                          | Kelas Ekivalen         | Hasil yang Diharapkan           | 📸 Screenshot |
|----|--------------------------------|--------------------------|----------------------------------|---------------|
| 1  | title: `Belajar Flask`         | valid                   | Tugas ditambahkan               |               |
| 2  | title kosong                   | invalid (kosong)        | Gagal, tidak disimpan           |               |
| 3  | description kosong             | valid (optional field)  | Tugas tetap disimpan            |               |

### 📏 Boundary Value Analysis (BVA)

| No | Input        | Nilai Uji         | Hasil yang Diharapkan         | 📸 Screenshot |
|----|--------------|-------------------|-------------------------------|---------------|
| 1  | title        | 1 karakter        | Tugas disimpan                |               |
| 2  | title        | 0 karakter        | Gagal simpan                  |               |
| 3  | title        | 255 karakter      | Tugas disimpan                |               |

---

## 4. 🔁 Update Status Tugas

### 🎯 Equivalence Partitioning (EP)

| No | Input status  | Kelas Ekivalen      | Hasil yang Diharapkan           | 📸 Screenshot |
|----|---------------|---------------------|----------------------------------|---------------|
| 1  | `pending`     | valid               | Status diperbarui               |               |
| 2  | `completed`   | valid               | Status diperbarui               |               |
| 3  | `archived`    | invalid (tidak ada) | Tidak diperbarui / error silent |               |

---

## 📎 Catatan
- Kolom **📸 Screenshot** dapat diisi dengan path file atau link ke gambar hasil pengujian.
- Semua pengujian dilakukan melalui UI web pengguna akhir.
