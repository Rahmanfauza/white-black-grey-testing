📌📌📌 model data flow testing

| **Komponen**           | **Definisi**                                                                                          | **Penggunaan**                                                | **Deskripsi**                                             |
| ---------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------- |
| Input Pengguna         | - `title` (string) <br> - `description` (string) <br> - `task_id` <br> - `username` <br> - `password` | - Fungsi `add_task()` <br> - `delete_task()` <br> - `login()` | Data dimasukkan lewat form task dan login                 |
| Fungsi `add_task()`    | - `title`, `description` dari form <br> - `user_id` dari session                                      | - Menambahkan data ke tabel `tasks`                           | Fungsi ini memvalidasi dan menyimpan task baru ke DB      |
| Fungsi `delete_task()` | - `task_id` dari URL <br> - `user_id` dari session                                                    | - Menghapus task berdasarkan id dan user                      | Menghapus data task dari DB jika milik user tersebut      |
| Fungsi `login()`       | - `username`, `password` dari form                                                                    | - Autentikasi user, menyimpan `session['user_id']`            | Fungsi login memverifikasi password dan menyimpan session |
| Tampilan Dashboard     | - `tasks[]` hasil query berdasarkan user\_id                                                          | - Menampilkan task yang sesuai milik user                     | Menampilkan data task dari DB ke tampilan pengguna        |






📌📌📌 test

| **Bagian**             | **Komponen**    | **Deskripsi Pemeriksaan**                                                      | **Hasil Pemeriksaan**                        | **Screenshot Code**                                      | **Screenshot Tampilan**                              |
| ---------------------- | --------------- | ------------------------------------------------------------------------------ | -------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------- |
| Input Pengguna         | `form input`    | Input `title`, `description`, `task_id`, `username`, dan `password` dari form  | ✔️ Input diterima dan diproses sesuai fungsi | ![Form Input Code](path_ke_gambar/form_input_code.png)   | ![Form Input UI](path_ke_gambar/form_input_ui.png)   |
| Fungsi `add_task()`    | `add_task()`    | Mengambil `title`, `description`, dan `user_id` dari session lalu simpan ke DB | ✔️ Task berhasil ditambahkan ke database     | ![Add Task Code](path_ke_gambar/add_task_code.png)       | ![Add Task UI](path_ke_gambar/add_task_ui.png)       |
| Fungsi `delete_task()` | `delete_task()` | Mengambil `task_id` dari URL, `user_id` dari session untuk proses DELETE       | ✔️ Task berhasil dihapus sesuai hak akses    | ![Delete Task Code](path_ke_gambar/delete_task_code.png) | ![Delete Task UI](path_ke_gambar/delete_task_ui.png) |
| Fungsi `login()`       | `login()`       | Validasi `username`, `password`, lalu simpan `user_id` ke session              | ✔️ Login berhasil jika data valid            | ![Login Code](path_ke_gambar/login_code.png)             | ![Login UI](path_ke_gambar/login_ui.png)             |
| Tampilan Dashboard     | `dashboard()`   | Mengambil daftar task berdasarkan `user_id` dari session, ditampilkan via loop | ✔️ Task tampil sesuai user yang login        | ![Dashboard Code](path_ke_gambar/dashboard_code.png)     | ![Dashboard UI](path_ke_gambar/dashboard_ui.png)     |
