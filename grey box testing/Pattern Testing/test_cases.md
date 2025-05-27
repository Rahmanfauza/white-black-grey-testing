Pattern Testing – Test Cases

| No | Skenario | Input | Ekspektasi | Status |
|----|----------|-------|------------|--------|
| 1 | Tambah tugas biasa | "Belajar AI" | Tugas muncul di dashboard | ✅ |
| 2 | Tambah tugas tanpa judul | "" | Error muncul | ✅ |
| 3 | Judul aneh | "@@@###" | Tersimpan tanpa gangguan | ✅ |
| 4 | Deskripsi sangat panjang | 10.000 karakter | Tidak crash | ✅ |
| 5 | Tambah 100 tugas | Loop manual/script | Dashboard tetap lancar | ✅ |
| 6 | Edit dan hapus berulang | Tugas dummy | Tidak error | ✅ |
| 7 | Login di 2 tab | Sama user | Tidak logout paksa | ✅ |
| 8 | Masukan tahun salah (di register) | "abc" | Validasi error | ✅ |
| 9 | Coba input script | `<script>` | Tidak dieksekusi | ✅ |
| 10 | Coba navigasi semua menu | Navbar | Semua bisa diakses | ✅ |
