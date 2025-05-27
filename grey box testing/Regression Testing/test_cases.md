# 🧪 Test Case – Regression Testing

Berikut ini adalah skenario pengujian fitur-fitur utama aplikasi setelah penambahan sistem waktu:

---

## ✅ Login

- **Langkah**:
  1. Buka `/login`
  2. Masukkan username dan password valid
- **Hasil Diharapkan**: 
  - Berpindah ke `/dashboard`
  - Muncul flash message: `"Login berhasil!"`

---

## ✅ Register

- **Langkah**:
  1. Buka `/register`
  2. Masukkan username/email/password baru
- **Hasil Diharapkan**: 
  - Redirect ke `/login`
  - Muncul pesan: `"Registrasi berhasil"`

---

## ✅ Tambah Tugas

- **Langkah**:
  1. Login
  2. Isi form tambah tugas di `/dashboard`
- **Periksa**:
  - Data masuk ke database
  - Kolom `created_at` menyimpan waktu dalam format ISO
  - Format waktu di UI: `27-05-2025 10:30`

---

## ✅ Lihat Daftar Tugas

- **Langkah**:
  1. Login
  2. Buka `/dashboard`
- **Hasil Diharapkan**: 
  - Semua tugas tampil
  - Urutan berdasarkan waktu `created_at` dari terbaru ke lama

---

## ✅ Lihat Detail Tugas

- **Langkah**:
  1. Klik salah satu tugas dari dashboard
- **Hasil Diharapkan**:
  - Informasi lengkap tugas tampil
  - Waktu tampil dengan format yang rapi

---

## ✅ Update Status Tugas

- **Langkah**:
  1. Buka detail tugas
  2. Ubah status (pending → selesai)
- **Hasil Diharapkan**: 
  - Status berubah di database
  - Muncul flash message konfirmasi

---

## ✅ Hapus Tugas

- **Langkah**:
  1. Buka detail tugas
  2. Klik delete
- **Hasil Diharapkan**: 
  - Tugas terhapus
  - Tidak muncul lagi di dashboard

---

## ✅ Logout

- **Langkah**:
  1. Klik logout
- **Hasil Diharapkan**:
  - Kembali ke halaman login
  - Session terhapus
