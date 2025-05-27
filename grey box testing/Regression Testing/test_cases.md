# 🧪 Test Case – Regression Testing

Berikut ini adalah skenario pengujian fitur-fitur utama aplikasi setelah penambahan sistem waktu:

---

## ✅ Login

**Langkah Pengujian:**
1. Buka halaman `/login`
2. Masukkan username dan password yang valid

**Hasil yang Diharapkan:**
- Berpindah ke `/dashboard`
- Muncul flash message: `"Login berhasil!"`

---

## ✅ Register

**Langkah Pengujian:**
1. Buka halaman `/register`
2. Masukkan username, email, dan password baru

**Hasil yang Diharapkan:**
- Redirect ke `/login`
- Muncul pesan: `"Registrasi berhasil"`

---

## ✅ Tambah Tugas

**Langkah Pengujian:**
1. Login
2. Isi form tambah tugas di `/dashboard`

**Data yang Diperiksa:**
- Data tersimpan di database
- Kolom `created_at` menyimpan waktu dalam format ISO
- Format waktu di UI: `27-05-2025 10:30`

---

## ✅ Lihat Daftar Tugas

**Langkah Pengujian:**
1. Login
2. Buka halaman `/dashboard`

**Hasil yang Diharapkan:**
- Semua tugas tampil
- Urutan berdasarkan `created_at` dari terbaru ke lama

---

## ✅ Lihat Detail Tugas

**Langkah Pengujian:**
1. Klik salah satu tugas dari dashboard

**Hasil yang Diharapkan:**
- Informasi lengkap tugas tampil
- Waktu tampil dengan format yang rapi

---

## ✅ Update Status Tugas

**Langkah Pengujian:**
1. Buka detail tugas
2. Ubah status (misal: *pending → selesai*)

**Hasil yang Diharapkan:**
- Status berubah di database
- Muncul flash message konfirmasi

---

## ✅ Hapus Tugas

**Langkah Pengujian:**
1. Buka detail tugas
2. Klik tombol hapus

**Hasil yang Diharapkan:**
- Tugas terhapus dari database
- Tidak muncul lagi di dashboard

---

## ✅ Logout

**Langkah Pengujian:**
1. Klik tombol logout

**Hasil yang Diharapkan:**
- Dialihkan ke halaman login
- Session pengguna terhapus
