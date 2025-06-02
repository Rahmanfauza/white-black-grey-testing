# Endurance Testing dan Cause Effect Testing 
## Endurance Testing 
Endurance Testing adalah teknik pengujian non-fungsional untuk memeriksa bagaimana aplikasi bertahan dalam jangka waktu panjang dengan beban kerja normal atau tinggi. Fokus utamanya adalah stabilitas sistem dalam jangka waktu lama — biasanya dilakukan beberapa jam hingga hari.

| Skenario                                                 | Input/Simulasi                                           | Ekspektasi                                                                              | Status |
|----------------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------------------------------------------|--------|
| Jalankan aplikasi 24 jam non-stop dengan aktivitas rutin | Tambah, update, hapus task setiap 10 menit selama 24 jam | Aplikasi tetap responsif, tidak crash, memori tidak naik terus menerus (no memory leak) |        |
| Simulasi 50 user aktif selama 8 jam                      | 50 user login, tambah task setiap 5 menit                | Tidak ada error, performa stabil, tidak ada bottleneck                                  |        |
| Dashboard refresh otomatis setiap 30 detik selama 12 jam | Fetch data task setiap 30 detik                          | Tidak ada timeout, aplikasi tidak lambat                                                |        |


## Cause Effect Testing 
Cause-Effect Relationship Testing (atau sering disebut juga Cause-Effect Graphing) adalah salah satu metode dalam pengujian perangkat lunak (software testing) yang digunakan untuk mengidentifikasi dan memverifikasi hubungan sebab-akibat (cause-effect) antara berbagai kondisi input (sebab) dan output atau hasil yang diharapkan (akibat) pada suatu sistem.

| Cause (Input/Kondisi)                                       | Effect (Output/Respons yang Diharapkan)                             | Status (Pass/Fail) |
|-------------------------------------------------------------|---------------------------------------------------------------------|--------------------|
| Username benar, password benar                              | Login berhasil, redirect ke dashboard                               |                |
| Username benar, password salah                              | Gagal login, muncul error "Username atau password salah"            |                |
| Form registrasi kosong                                      | Gagal registrasi, muncul error validasi                             |                |
| Task dibuat dengan title kosong                             | Gagal tambah task, muncul error validasi                            |                |
| User menghapus task yang bukan miliknya                     | Tidak bisa menghapus, muncul error "Task tidak ditemukan"           |                |
| User menambahkan task dengan deskripsi panjang (>1000 char) | Task disimpan (jika tidak ada batasan) atau muncul error (jika ada) |                |
| User menambahkan task dengan special character (`<script>`) | Input disanitasi, tidak ada XSS                                     |                |

