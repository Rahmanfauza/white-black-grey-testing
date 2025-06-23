## Loop Testing

Model Loop Testing bertujuan untuk memverifikasi bahwa semua perulangan (loop) dalam aplikasi berjalan sesuai logika dan tidak menyebabkan error atau infinite loop.


| Komponen         | Lokasi Fungsi / Template          | Jenis Loop   | Deskripsi                                                                 |
|------------------|-----------------------------------|--------------|---------------------------------------------------------------------------|
| `for task in tasks` | `dashboard.html`, `add_task.html`  | Jinja2 `for` | Menampilkan daftar tugas berdasarkan hasil query dari database            |
| `for row in rows`   | `register()`, `update_task()`      | Python `for` | Iterasi hasil query SQL atau list data yang diambil dari database        |
| `for` pada template | Semua template yang looping `tasks`| Jinja2 loop  | Perulangan otomatis untuk menampilkan data list dalam halaman HTML       |
