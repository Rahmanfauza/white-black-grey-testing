# 📊 White Box Testing – Data Flow Testing (Task Manager App)

Dokumen ini berisi hasil pengujian **White Box Testing** dengan fokus pada teknik **Data Flow Testing** terhadap aplikasi Task Manager berbasis Flask.

---

## 📌 Tujuan

Data Flow Testing bertujuan untuk:
- Memeriksa bagaimana variabel didefinisikan (`define`) dan digunakan (`use`)
- Menemukan potensi kesalahan seperti variabel tidak digunakan atau digunakan sebelum didefinisikan
- Memastikan program memproses input dengan benar

---

## 📂 Struktur Direktori

- **data-flow-testing/**
  - `README.md`
  - `hasil_testing.md`
  - **diagrams/**
    - `dd_task_flowchart.png`
  - **screenshots/**
    - `add_task_code.png`
    - `add_task_ui.png`
    - `login_code.png`
    - `login_ui.png`



---

## 📄 Daftar Fungsi yang Diuji

| Fungsi           | Tujuan                                                        |
|------------------|---------------------------------------------------------------|
| `add_task()`     | Menyimpan data task ke database berdasarkan input user        |
| `login()`        | Verifikasi kredensial user dan menyimpan `user_id` ke session|
| `delete_task()`  | Menghapus task berdasarkan `task_id` dan `user_id` dari session|
| `dashboard()`    | melihat apakah semua sudah sesuai dengan alur|


---

## 🔁 Diagram Flowchart

🖼️ Lihat di folder [`diagrams/`](./diagrams/) untuk visualisasi flow fungsi `add_task()` yang diuji berdasarkan alur data.

---

## 🧪 Hasil Pengujian

Lihat file [`hasil_testing.md`](./Hasil_testing.md) untuk tabel pengujian lengkap dengan:
- Deskripsi penggunaan variabel
- Hasil yang diharapkan
- Screenshot kode dan tampilan

---

## 📌 Catatan

- Semua pengujian dilakukan secara manual dengan memeriksa source code.
- Tidak ditemukan error `use-before-define`.
- Semua aliran data berjalan sesuai skenario yang diharapkan.

---




