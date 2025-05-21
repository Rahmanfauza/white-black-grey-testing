| **Komponen**           | **Definisi**                                                                                          | **Penggunaan**                                                | **Deskripsi**                                             |
| ---------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------- |
| Input Pengguna         | - `title` (string) <br> - `description` (string) <br> - `task_id` <br> - `username` <br> - `password` | - Fungsi `add_task()` <br> - `delete_task()` <br> - `login()` | Data dimasukkan lewat form task dan login                 |
| Fungsi `add_task()`    | - `title`, `description` dari form <br> - `user_id` dari session                                      | - Menambahkan data ke tabel `tasks`                           | Fungsi ini memvalidasi dan menyimpan task baru ke DB      |
| Fungsi `delete_task()` | - `task_id` dari URL <br> - `user_id` dari session                                                    | - Menghapus task berdasarkan id dan user                      | Menghapus data task dari DB jika milik user tersebut      |
| Fungsi `login()`       | - `username`, `password` dari form                                                                    | - Autentikasi user, menyimpan `session['user_id']`            | Fungsi login memverifikasi password dan menyimpan session |
| Tampilan Dashboard     | - `tasks[]` hasil query berdasarkan user\_id                                                          | - Menampilkan task yang sesuai milik user                     | Menampilkan data task dari DB ke tampilan pengguna        |






📌📌📌 test

| Bagian          | Komponen        | Deskripsi Pemeriksaan                                                  | Hasil Pemeriksaan                         | Screenshot Code                                              | Screenshot Tampilan                                           |
| --------------- | --------------- | ---------------------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| Manajemen Tugas | `add_task()`    | Variabel `title`, `description` didefinisikan lalu digunakan di query  | ✔️ Data berhasil ditambahkan ke database  | ![Add Task Code](path_ke_gambar/add_task_code.png)             | ![Add Task UI](path_ke_gambar/add_task_ui.png)                 |
| Autentikasi     | `login()`       | Variabel `username`, `password` divalidasi di DB dan digunakan session | ✔️ Login berhasil jika data valid         | ![Login Code](path_ke_gambar/login_code.png)                   | ![Login UI](path_ke_gambar/login_ui.png)                       |
| Manajemen Tugas | `delete_task()` | Variabel `task_id` digunakan untuk DELETE berdasarkan user login       | ✔️ Task berhasil dihapus sesuai hak akses | ![Delete Task Code](path_ke_gambar/delete_task_code.png)       | ![Delete Task UI](path_ke_gambar/delete_task_ui.png)           |
| Dashboard       | `dashboard()`   | Mengambil `user_id` dari session, tampilkan task via loop              | ✔️ Daftar task tampil sesuai user login   | ![Dashboard Code](path_ke_gambar/dashboard_code.png)           | ![Dashboard UI](path_ke_gambar/dashboard_ui.png)               |
