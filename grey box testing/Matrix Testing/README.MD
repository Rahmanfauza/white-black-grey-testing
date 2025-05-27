📊 Matrix Testing – Gray Box Testing

✅ Tujuan
Matrix Testing digunakan untuk menguji kombinasi dari berbagai kondisi input dan status aplikasi, agar dapat mendeteksi interaksi yang dapat menyebabkan bug.

🔎 Fitur yang Diuji
- Login dan Akses Task
- Status Task (`pending` dan `selesai`)
- Kondisi Data (ada / kosong)

🧪 Matriks Pengujian

| TC | Status | Login | Data      | Hasil yang Diharapkan                           |
|----|--------|--------|-----------|--------------------------------------------------|
| 1  | pending | ✔️      | ✔️         | Tampil normal                                   |
| 2  | selesai | ✔️      | ✔️         | Tampil dengan status selesai                    |
| 3  | pending | ❌      | ✔️         | Redirect ke login                               |
| 4  | selesai | ❌      | ✔️         | Redirect ke login                               |
| 5  | pending | ✔️      | ❌         | Halaman valid, data kosong                      |
| 6  | selesai | ✔️      | ❌         | Halaman valid, data kosong                      |
| 7  | pending | ❌      | ❌         | Redirect ke login                               |
| 8  | selesai | ❌      | ❌         | Redirect ke login                               |

## 📷 Screenshot
Lihat folder `/screenshots` untuk bukti hasil uji.

