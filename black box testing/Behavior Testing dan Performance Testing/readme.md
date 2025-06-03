# Pengujian Behavior Testing dan Performance testing 

## 1. Behavior Testing 
Behavioral testing, atau pengujian berbasis perilaku, adalah pendekatan pengujian perangkat lunak yang fokus pada bagaimana perangkat lunak berperilaku di bawah berbagai kondisi dan skenario. Ini sering disebut juga sebagai pengujian black box karena penguji tidak perlu melihat struktur kode internal perangkat lunak. 

| No. | Fitur               | BDD (Given – When – Then)                                                                                                                                             |  Flowchart                                                                                       |
|-----|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| 1   | Registrasi Pengguna | **Given** pengguna berada di halaman registrasi <br> **When** pengguna mengisi username, email, dan password yang valid <br> **Then** akun berhasil dibuat dan pengguna diarahkan ke halaman login | <img src="https://github.com/user-attachments/assets/8347595b-6448-4e0e-992e-cf0160012f5e" width="250"/>   |
| 2   | Login Pengguna      | **Given** pengguna berada di halaman login <br> **When** pengguna memasukkan username dan password yang valid <br> **Then** pengguna berhasil masuk ke dashboard     | <img src="https://github.com/user-attachments/assets/b905b9b4-cd71-4748-b0f5-b36241500675" width="250"/>   |
| 3   | Tambah Tugas        | **Given** pengguna berada di dashboard <br> **When** pengguna mengklik tombol tambah dan mengisi form judul dan deskripsi yang valid <br> **Then** tugas ditambahkan ke daftar tugas | <img src="https://github.com/user-attachments/assets/f958cc54-a794-4af6-aca2-edb2617d87ba" width="250"/>   |
| 4   | Lihat Detail Tugas  | **Given** pengguna melihat daftar tugas <br> **When** pengguna mengklik salah satu tugas <br> **Then** halaman detail tugas ditampilkan secara lengkap                | <img src="https://github.com/user-attachments/assets/aec970e6-a0b0-4bd1-b240-91c0f775db51" width="250"/>   |
| 5   | Perbarui Status     | **Given** pengguna berada di halaman detail tugas <br> **When** pengguna memilih status baru (misalnya: "selesai") <br> **Then** status tugas diperbarui dan ditampilkan | <img src="https://github.com/user-attachments/assets/3e22c6ed-dbc0-4c47-b44b-6bdb0f98b9a3" width="250"/>   |
| 6   | Hapus Tugas         | **Given** pengguna berada di daftar tugas <br> **When** pengguna menekan tombol hapus pada salah satu tugas <br> **Then** tugas dihapus dari sistem dan hilang dari tampilan | <img src="https://github.com/user-attachments/assets/cd6fe5ba-2b23-4f6b-b653-e746f23c452f" width="250"/>   |
| 7   | Logout              | **Given** pengguna sedang login <br> **When** pengguna menekan tombol logout <br> **Then** sesi berakhir dan pengguna diarahkan kembali ke halaman login              | <img src="https://github.com/user-attachments/assets/ba580406-8c3f-4735-9017-53db4b49f6e8" width="250"/>   |
|

## 2. Performance Testing
Performance testing adalah jenis pengujian perangkat lunak yang bertujuan untuk mengevaluasi kinerja, stabilitas, dan skalabilitas sistem di bawah beban kerja tertentu. Pengujian ini membantu mengidentifikasi botol leher, mengukur responsivitas sistem, dan memastikan bahwa aplikasi dapat menangani jumlah pengguna yang diharapkan tanpa penurunan performa yang signifikan. 

| No. | Fitur               | Performance Testing                                                                                   |
|-----|---------------------|--------------------------------------------------------------------------------------------------------|
| 1   | Registrasi Pengguna | <img src="https://github.com/user-attachments/assets/37ab1b07-8a98-4cca-b6d6-00624a376ef1" width="300"/> |
| 2   | Login Pengguna      | <img src="https://github.com/user-attachments/assets/b37c07a1-8b09-4c99-94f2-abc236591117" width="300"/> |
| 3   | Dashboard           | <img src="https://github.com/user-attachments/assets/c731ee98-b051-47f3-a5e9-3a16a5c291d4" width="300"/> |
| 4   | Detail Tugas        | <img src="https://github.com/user-attachments/assets/183c00d2-e346-4137-bf87-2a0026141dfc" width="300"/> |
| 5   | Daftar Semua Tugas  | <img src="https://github.com/user-attachments/assets/d65a8e3a-b7d2-4dd0-b934-3d83ca2bb2cb" width="300"/> |




