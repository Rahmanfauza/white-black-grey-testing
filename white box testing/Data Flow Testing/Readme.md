## Data Flow Testing

Model Data Flow Testing menelusuri bagaimana data dan variabel dideklarasikan, dimodifikasi, dan digunakan di setiap fungsi dalam program.

| Komponen     | Definisi                                      | Penggunaan                                   | Deskripsi                                                                 |
|--------------|-----------------------------------------------|----------------------------------------------|---------------------------------------------------------------------------|
| `username`   | Diform input di `register`, `login`           | Digunakan untuk autentikasi dan penyimpanan  | Digunakan untuk identifikasi unik user dalam sesi dan database.          |
| `password`   | Diform input di `register`, `login`           | Digunakan untuk verifikasi                   | Disimpan dalam bentuk hash untuk keamanan, diverifikasi saat login.      |
| `email`      | Diform input di `register`                    | Disimpan dalam database                      | Informasi tambahan yang divalidasi keunikannya saat registrasi.          |
| `task`       | Dibentuk saat tambah, edit, dan ambil dari DB | Digunakan untuk manipulasi tampilan & update | Struktur utama yang direpresentasikan sebagai tugas per user.            |
| `task_id`    | Parameter URL & query database                | Digunakan untuk identifikasi tugas spesifik  | ID unik untuk manipulasi task (edit, delete, complete).                  |
| `session`    | Dibentuk saat login                           | Digunakan untuk menjaga autentikasi sesi     | Menyimpan status login dan identitas pengguna dalam sesi web.            |
| `date`       | Diform input di tambah & update task          | Digunakan untuk filter & tampilan            | Digunakan untuk menjadwalkan tugas dan klasifikasi waktu.                |
| `tasks`      | Hasil dari query DB di dashboard/today        | Di-loop untuk ditampilkan                    | Kumpulan data tugas yang akan dirender dalam halaman HTML.               |
