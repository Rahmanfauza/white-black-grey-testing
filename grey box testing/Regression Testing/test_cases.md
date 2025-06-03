🧪 Regression Testing – Task Manager App

Dokumen ini berisi skenario pengujian untuk memastikan bahwa perubahan pada sistem `created_at` tidak merusak fitur-fitur utama dalam aplikasi Task Manager.

---

✅ Test Case 1: Login

**Langkah Pengujian:**
1. Buka halaman `/login`
2. Masukkan username dan password valid

**Hasil yang Diharapkan:**
- ✅ Berpindah ke halaman `/dashboard`
- ✅ Muncul flash message: `Login berhasil!`

**Status:** [✅]  
**Catatan:** sesuai dengan yang diharapkan, hanyasaja database terlalu lambat merekam input sesuai perkiraan


---

✅ Test Case 2: Register

**Langkah Pengujian:**
1. Buka halaman `/register`
2. Isi form: username, email, password

**Hasil yang Diharapkan:**
- ✅ Redirect ke `/login`
- ✅ Flash message: `Registrasi berhasil`

**Status:** [✅]  
**Catatan:** sesuai

---

✅ Test Case 3: Tambah Tugas

**Langkah Pengujian:**
1. Login terlebih dahulu
2. Di dashboard, isi form tambah tugas

**Data yang Diperiksa:**
- ✅ Data masuk ke database
- ✅ Kolom `created_at` menyimpan waktu ISO (cek via SQLite)
- ✅ Di UI, waktu diformat `dd-mm-yyyy hh:mm`

**Status:** [✅]  
**Catatan:** database lambat dalam input yang dimasukkan

---

✅ Test Case 4: Lihat Daftar Tugas

**Langkah Pengujian:**
1. Login
2. Buka `/dashboard`

**Hasil yang Diharapkan:**
- ✅ Tugas muncul
- ✅ Tersortir dari waktu terbaru ke lama

**Status:** [✅]  
**Catatan:** sesuai

---

✅ Test Case 5: Detail Tugas

**Langkah Pengujian:**
1. Klik salah satu tugas

**Hasil yang Diharapkan:**
- ✅ Semua info tampil (title, desc, status, waktu)
- ✅ Format waktu rapi dan terbaca

**Status:** [✅]  
**Catatan:** sesuai

---

✅ Test Case 6: Update Status Tugas

**Langkah Pengujian:**
1. Masuk ke detail tugas
2. Ubah status (*pending → selesai*)

**Hasil yang Diharapkan:**
- ✅ Status tersimpan di database
- ✅ Muncul flash message konfirmasi

**Status:** [✅]  
**Catatan:** sesuai, hanya saja database tidak dapat di akses
---

✅ Test Case 7: Hapus Tugas

**Langkah Pengujian:**
1. Masuk ke detail tugas
2. Klik tombol "hapus"

**Hasil yang Diharapkan:**
- ✅ Tugas dihapus dari database
- ✅ Tidak muncul lagi di dashboard

**Status:** [✅]  
**Catatan:** sudah sesuai

---

#✅ Test Case 8: Logout

**Langkah Pengujian:**
1. Klik tombol "Logout"

**Hasil yang Diharapkan:**
- ✅ Dialihkan ke halaman `/login`
- ✅ Session dihapus

**Status:** [❌]  
**Catatan:** nama user masih tertera ketika logout
