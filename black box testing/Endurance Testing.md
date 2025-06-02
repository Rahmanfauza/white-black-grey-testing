# Black Box Testing Scenarios: Task Manager Application

Berikut adalah rancangan skenario pengujian black-box menggunakan teknik Boundary Value Analysis (BVA) dan Equivalence Partitioning (EP) untuk aplikasi Task Manager. Pengujian aktual tidak dapat dilakukan karena kendala teknis akses aplikasi.

**Catatan:** Asumsi batas panjang karakter (Min/Max) dibuat berdasarkan praktik umum dan mungkin perlu disesuaikan jika ada spesifikasi yang berbeda dari aplikasi.

## Boundary Value Analysis (BVA)

Tabel ini merinci kasus uji BVA untuk memvalidasi input pada nilai batasnya.

| Fitur         | Input Field   | Test Case ID          | Deskripsi Pengujian                   | Tipe      | Ekspektasi Hasil (Umum) |
|---------------|---------------|-----------------------|---------------------------------------|-----------|-------------------------|
| **Registrasi**| Username      | TC-BVA-REG-USR-01     | Input 2 karakter                      | Invalid   | Gagal (Below Min)       |
|               | Username      | TC-BVA-REG-USR-02     | Input 3 karakter                      | Valid     | Berhasil (Min)          |
|               | Username      | TC-BVA-REG-USR-03     | Input 4 karakter                      | Valid     | Berhasil (Min+1)        |
|               | Username      | TC-BVA-REG-USR-04     | Input 19 karakter                     | Valid     | Berhasil (Max-1)        |
|               | Username      | TC-BVA-REG-USR-05     | Input 20 karakter                     | Valid     | Berhasil (Max)          |
|               | Username      | TC-BVA-REG-USR-06     | Input 21 karakter                     | Invalid   | Gagal (Above Max)       |
|               | Password      | TC-BVA-REG-PWD-01     | Input 5 karakter                      | Invalid   | Gagal (Below Min)       |
|               | Password      | TC-BVA-REG-PWD-02     | Input 6 karakter                      | Valid     | Berhasil (Min)          |
|               | Password      | TC-BVA-REG-PWD-03     | Input 7 karakter                      | Valid     | Berhasil (Min+1)        |
|               | Password      | TC-BVA-REG-PWD-04     | Input 29 karakter                     | Valid     | Berhasil (Max-1)        |
|               | Password      | TC-BVA-REG-PWD-05     | Input 30 karakter                     | Valid     | Berhasil (Max)          |
|               | Password      | TC-BVA-REG-PWD-06     | Input 31 karakter                     | Invalid   | Gagal (Above Max)       |
| **Login**     | Username      | TC-BVA-LOG-USR-01     | Input 2 karakter                      | Invalid   | Gagal (Below Min)       |
|               | Username      | TC-BVA-LOG-USR-02     | Input 3 karakter                      | Valid     | Berhasil/Gagal (Min)*   |
|               | Username      | TC-BVA-LOG-USR-03     | Input 20 karakter                     | Valid     | Berhasil/Gagal (Max)*   |
|               | Username      | TC-BVA-LOG-USR-04     | Input 21 karakter                     | Invalid   | Gagal (Above Max)       |
|               | Password      | TC-BVA-LOG-PWD-01     | Input 5 karakter                      | Invalid   | Gagal (Below Min)       |
|               | Password      | TC-BVA-LOG-PWD-02     | Input 6 karakter                      | Valid     | Berhasil/Gagal (Min)*   |
|               | Password      | TC-BVA-LOG-PWD-03     | Input 30 karakter                     | Valid     | Berhasil/Gagal (Max)*   |
|               | Password      | TC-BVA-LOG-PWD-04     | Input 31 karakter                     | Invalid   | Gagal (Above Max)       |
| **Tambah Tugas**| Title         | TC-BVA-TSK-TTL-01     | Input 0 karakter (Kosong)             | Invalid   | Gagal (Below Min/Empty) |
|               | Title         | TC-BVA-TSK-TTL-02     | Input 1 karakter                      | Valid     | Berhasil (Min)          |
|               | Title         | TC-BVA-TSK-TTL-03     | Input 2 karakter                      | Valid     | Berhasil (Min+1)        |
|               | Title         | TC-BVA-TSK-TTL-04     | Input 99 karakter                     | Valid     | Berhasil (Max-1)        |
|               | Title         | TC-BVA-TSK-TTL-05     | Input 100 karakter                    | Valid     | Berhasil (Max)          |
|               | Title         | TC-BVA-TSK-TTL-06     | Input 101 karakter                    | Invalid   | Gagal (Above Max)       |
|               | Description   | TC-BVA-TSK-DSC-01     | Input 0 karakter (Kosong)             | Valid     | Berhasil (Empty/Min)    |
|               | Description   | TC-BVA-TSK-DSC-02     | Input 1 karakter                      | Valid     | Berhasil (Min+1)        |
|               | Description   | TC-BVA-TSK-DSC-03     | Input 499 karakter                    | Valid     | Berhasil (Max-1)        |
|               | Description   | TC-BVA-TSK-DSC-04     | Input 500 karakter                    | Valid     | Berhasil (Max)          |
|               | Description   | TC-BVA-TSK-DSC-05     | Input 501 karakter                    | Invalid   | Gagal (Above Max)       |

_* Catatan Login: Hasil valid/gagal juga tergantung pada apakah username/password cocok dengan data yang ada di database._

## Equivalence Partitioning (EP)

Tabel ini merinci kasus uji EP untuk memvalidasi input berdasarkan partisi kelas ekuivalensi (valid dan invalid).

| Fitur         | Input Field   | Test Case ID          | Partisi / Deskripsi Pengujian             | Contoh Input                               | Tipe      | Ekspektasi Hasil (Umum) |
|---------------|---------------|-----------------------|-------------------------------------------|--------------------------------------------|-----------|-------------------------|
| **Registrasi**| Username      | TC-EP-REG-USR-01      | Valid Alphanumeric [3-20]                 | "testuser1"                                | Valid     | Berhasil                |
|               | Username      | TC-EP-REG-USR-02      | Invalid - Empty                           | ""                                         | Invalid   | Gagal                   |
|               | Username      | TC-EP-REG-USR-03      | Invalid - Too Short [<3]                  | "us"                                       | Invalid   | Gagal                   |
|               | Username      | TC-EP-REG-USR-04      | Invalid - Too Long [>20]                  | "averylongusernamemorethan20chars"         | Invalid   | Gagal                   |
|               | Username      | TC-EP-REG-USR-05      | Invalid - Special Chars (jika dilarang)   | "user@#$"                                  | Invalid   | Gagal                   |
|               | Username      | TC-EP-REG-USR-06      | Invalid - Existing                        | Username yang sudah terdaftar              | Invalid   | Gagal                   |
|               | Email         | TC-EP-REG-EML-01      | Valid Format                              | "test@example.com"                         | Valid     | Berhasil                |
|               | Email         | TC-EP-REG-EML-02      | Invalid - Missing '@'                     | "testexample.com"                          | Invalid   | Gagal                   |
|               | Email         | TC-EP-REG-EML-03      | Invalid - Missing '.' (domain part)       | "test@examplecom"                          | Invalid   | Gagal                   |
|               | Email         | TC-EP-REG-EML-04      | Invalid - Empty                           | ""                                         | Invalid   | Gagal                   |
|               | Email         | TC-EP-REG-EML-05      | Invalid - Existing                        | Email yang sudah terdaftar                 | Invalid   | Gagal                   |
|               | Password      | TC-EP-REG-PWD-01      | Valid [6-30]                              | "password123"                              | Valid     | Berhasil                |
|               | Password      | TC-EP-REG-PWD-02      | Invalid - Too Short [<6]                  | "pass"                                     | Invalid   | Gagal                   |
|               | Password      | TC-EP-REG-PWD-03      | Invalid - Too Long [>30]                  | "averylongpasswordmorethan30chars12345"    | Invalid   | Gagal                   |
| **Login**     | Username      | TC-EP-LOG-USR-01      | Valid - Existing                          | Username valid terdaftar                   | Valid     | Berhasil                |
|               | Username      | TC-EP-LOG-USR-02      | Invalid - Non-Existing                    | Username tidak terdaftar                   | Invalid   | Gagal                   |
|               | Username      | TC-EP-LOG-USR-03      | Invalid - Format/Length                   | "u"                                        | Invalid   | Gagal                   |
|               | Username      | TC-EP-LOG-USR-04      | Invalid - Empty                           | ""                                         | Invalid   | Gagal                   |
|               | Password      | TC-EP-LOG-PWD-01      | Valid - Correct                           | Password benar untuk username valid        | Valid     | Berhasil                |
|               | Password      | TC-EP-LOG-PWD-02      | Invalid - Incorrect                       | Password salah untuk username valid        | Invalid   | Gagal                   |
|               | Password      | TC-EP-LOG-PWD-03      | Invalid - Format/Length                   | "pwd"                                      | Invalid   | Gagal                   |
|               | Password      | TC-EP-LOG-PWD-04      | Invalid - Empty                           | ""                                         | Invalid   | Gagal                   |
| **Tambah Tugas**| Title         | TC-EP-TSK-TTL-01      | Valid [1-100]                             | "Selesaikan Laporan Bulanan"               | Valid     | Berhasil                |
|               | Title         | TC-EP-TSK-TTL-02      | Invalid - Empty                           | ""                                         | Invalid   | Gagal                   |
|               | Title         | TC-EP-TSK-TTL-03      | Invalid - Too Long [>100]                 | String > 100 karakter                      | Invalid   | Gagal                   |
|               | Description   | TC-EP-TSK-DSC-01      | Valid [0-500]                             | "Detail laporan mencakup..."               | Valid     | Berhasil                |
|               | Description   | TC-EP-TSK-DSC-02      | Valid - Empty                             | ""                                         | Valid     | Berhasil                |
|               | Description   | TC-EP-TSK-DSC-03      | Invalid - Too Long [>500]                 | String > 500 karakter                      | Invalid   | Gagal                   |
| **Update Status**| Status        | TC-EP-TSK-STS-01      | Valid - 'pending'                         | Pilih 'pending'                            | Valid     | Berhasil                |
|               | Status        | TC-EP-TSK-STS-02      | Valid - 'completed'                       | Pilih 'completed'                          | Valid     | Berhasil                |
|               | Status        | TC-EP-TSK-STS-03      | Valid - 'in progress' (jika ada)          | Pilih 'in progress'                        | Valid     | Berhasil                |
|               | Status        | TC-EP-TSK-STS-04      | Invalid - Nilai Lainnya                   | Input/Pilih nilai selain yang valid        | Invalid   | Gagal                   |

