📊 Matrix Testing – Gray Box Testing

✅ Tujuan

Matrix Testing digunakan untuk menguji kombinasi dari berbagai kondisi input dan status aplikasi, agar dapat mendeteksi interaksi yang dapat menyebabkan bug.

---

🔎 Fitur yang Diuji

- Login dan Akses Task
- Status Task (`pending` dan `selesai`)
- Kondisi Data (ada / kosong)

---

🧪 Matriks Pengujian

| TC | Status   | Login | Data | Hasil yang Diharapkan                | Hasil Aktual       | Sesuai? | Catatan                        |
|----|----------|-------|------|--------------------------------------|--------------------|---------|---------------------------------|
| 1  | pending  | ✔️     | ✔️    | Tampil normal                        |<img width="570" alt="Image" src="https://github.com/user-attachments/assets/0987cd22-c152-44c6-a637-c0efeba4031e" />
                    |         |                                 |
| 2  | selesai  | ✔️     | ✔️    | Tampil dengan status selesai         |<img width="565" alt="Image" src="https://github.com/user-attachments/assets/91cd1281-0642-49d9-997b-78075590889e" />
                    |         |                                 |
| 3  | pending  | ❌     | ✔️    | Redirect ke login                    |<img width="543" alt="Image" src="https://github.com/user-attachments/assets/b8f57448-f45a-444c-a8e8-63aa608d9c84" />
                    |         |                                 |
| 4  | selesai  | ❌     | ✔️    | Redirect ke login                    |<img width="446" alt="Image" src="https://github.com/user-attachments/assets/a594574a-a28d-4509-8e51-50e575b7ad6c" />
                    |         |                                 |
| 5  | pending  | ✔️     | ❌    | Halaman valid, data kosong           |<img width="598" alt="Image" src="https://github.com/user-attachments/assets/3553986f-bdfb-4216-9f28-fcde85fa1878" />
                    |         |                                 |
| 6  | selesai  | ✔️     | ❌    | Halaman valid, data kosong           |<img width="577" alt="Image" src="https://github.com/user-attachments/assets/cc48a924-7473-48fb-a335-dbb94b229996" />

                    |         |                                 |
| 7  | pending  | ❌     | ❌    | Redirect ke login                    |<img width="584" alt="Image" src="https://github.com/user-attachments/assets/57746678-40ee-4687-82bd-f49cbc97f14c" />
                    |         |                                 |
| 8  | selesai  | ❌     | ❌    | Redirect ke login                    |<img width="584" alt="Image" src="https://github.com/user-attachments/assets/bbdd4dad-6b6c-4764-be7b-274799adb5aa" />                    |         |                                 |

---

📌 Keterangan Kolom

- **Status:** Status tugas yang dipilih
- **Login:** Kondisi apakah user sudah login
- **Data:** Apakah ada data task di database
- **Hasil yang Diharapkan:** Prediksi perilaku sistem
- **Hasil Aktual:** Diisi setelah pengujian manual/otomatis
- **Sesuai?:** ✅ atau ❌
- **Catatan:** Tambahan info jika ada error, bug, atau anomaly

---


