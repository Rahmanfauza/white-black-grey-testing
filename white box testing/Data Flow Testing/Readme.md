## Data Flow Testing

Model Data Flow Testing menelusuri bagaimana data dan variabel dideklarasikan, dimodifikasi, dan digunakan di setiap fungsi dalam program.

| Komponen   | Definisi                                               | Penggunaan                                        | Deskripsi                                                              |
|------------|--------------------------------------------------------|--------------------------------------------------|------------------------------------------------------------------------|
| `username` | Form input di `register()` dan `login()`               | Untuk pengecekan user di DB, disimpan di session | Identitas utama pengguna untuk autentikasi dan pemrosesan user login   |
| `password` | Form input di `register()` dan `login()`               | Dicek dengan `check_password_hash()`             | Digunakan untuk autentikasi dan disimpan dalam bentuk hash             |
| `email`    | Form input di `register()`                             | Validasi unik dan penyimpanan ke database        | Informasi tambahan untuk identifikasi pengguna                         |
| `session`  | Dibentuk saat login berhasil                           | Mengecek status login di setiap route            | Menyimpan identitas dan menjaga autentikasi pengguna selama sesi aktif |
| `task`     | Hasil query dari DB dalam `dashboard()`                | Ditampilkan di dashboard, diproses pada update   | Struktur utama yang merepresentasikan satu unit pekerjaan              |
| `task_id`  | Parameter URL pada `update_task()` dan `delete_task()` | Identifikasi task spesifik yang akan dimodifikasi| ID unik yang menjadi referensi saat operasi edit, hapus, atau update   |
| `date`     | Input form di `add_task()` dan `update_task()`         | Disimpan ke DB dan digunakan saat menampilkan    | Menentukan jadwal tugas yang diinputkan pengguna                       |
| `tasks`    | Variabel dari hasil `fetchall()` query                 | Di-loop pada template dashboard                  | List tugas per user yang digunakan untuk ditampilkan di frontend       |
