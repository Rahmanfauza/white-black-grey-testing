# Basic Path Testing Report

Model Basic Path Testing digunakan untuk menghitung kompleksitas jalur logika dan mengidentifikasi jumlah minimum jalur pengujian yang harus diuji berdasarkan fungsi yang ada.

Rumus:
V(G) = E - N + 2P

- E = Jumlah edge (alur kontrol)

- N = Jumlah node (aksi / kondisi)

- P = Komponen terhubung (1 untuk setiap fungsi mandiri)

### Tabel Basic Path Testing

| Fungsi         | Node (N) | Edge (E) | Komponen (P) | Cyclomatic (V(G)) | Jalur Uji Minimum | Keterangan                                                  |
|----------------|----------|----------|----------------|-------------------|-------------------|-------------------------------------------------------------|
| `register`     | 6        | 7        | 1              | 3                 | 3                 | User/email tersedia, tidak tersedia, GET form              |
| `login`        | 6        | 7        | 1              | 3                 | 3                 | Login berhasil, login gagal, dan GET login form            |
| `dashboard`    | 3        | 4        | 1              | 3                 | 2                 | Session ada → tampilkan, tidak ada → redirect login        |
| `add_task`     | 4        | 5        | 1              | 3                 | 2                 | POST task, GET form                                         |
| `update_task`  | 3        | 4        | 1              | 3                 | 2                 | Proses update, redirect login                              |
| `delete_task`  | 3        | 4        | 1              | 3                 | 2                 | Login dan hapus, redirect login                            |
| `logout`       | 2        | 1        | 1              | 1                 | 1                 | Jalur linier: clear session & redirect   |



## register()
[Lihat disini](register.md)

## login()
[Lihat disini](login.md)

## dashboard()
[Lihat disini](dashboard.md)

## add_task()
[Lihat disini](add_task.md)

## update_task()
[Lihat disini](update_task.md)

## delete_task()
[Lihat disini](delete_task.md)

## logout()
[Lihat disini](logout.md)
