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
| `login`        | 6        | 7        | 1              | 3                 | 3                 | Login berhasil, login gagal, dan GET login form            |
| `register`     | 6        | 7        | 1              | 3                 | 3                 | User/email tersedia, tidak tersedia, GET form              |
| `dashboard`    | 3        | 4        | 1              | 3                 | 2                 | Session ada → tampilkan, tidak ada → redirect login        |
| `add_task`     | 4        | 5        | 1              | 3                 | 2                 | POST task, GET form                                         |
| `delete_task`  | 3        | 4        | 1              | 3                 | 2                 | Login dan hapus, redirect login                            |
| `update_task`  | 3        | 4        | 1              | 3                 | 2                 | Proses update, redirect login                              |


## login()
[Lihat disini](login.md)
