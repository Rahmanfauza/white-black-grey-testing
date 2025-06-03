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
| 1  | pending  | ✔️     | ✔️    | Tampil normal                        | <img width="570" alt="Image" src="https://github.com/user-attachments/assets/0987cd22-c152-44c6-a637-c0efeba4031e" />                   |         |                                 |
| 2  | selesai  | ✔️     | ✔️    | Tampil dengan status selesai         |<img width="578" alt="Image" src="https://github.com/user-attachments/assets/baa10c1c-2803-4c5e-a0a6-cb9cbd166741" /> <img width="565" alt="Image" src="https://github.com/user-attachments/assets/91cd1281-0642-49d9-997b-78075590889e" />                    |         |                                 |
| 3  | pending  | ❌     | ✔️    | Redirect ke login                    |<img width="554" alt="Image" src="https://github.com/user-attachments/assets/4169eca9-6ebe-43b5-827a-e00195b9664c" /> <img width="283" alt="Image" src="https://github.com/user-attachments/assets/cb45ba08-43b4-4c71-b75f-48fd9cb3958c" /> <img width="543" alt="Image" src="https://github.com/user-attachments/assets/b8f57448-f45a-444c-a8e8-63aa608d9c84" />                    |         |                                 |
| 4  | selesai  | ❌     | ✔️    | Redirect ke login                    |<img width="566" alt="Image" src="https://github.com/user-attachments/assets/8c5c2006-793f-4655-b860-0caabcb549d2" /> <img width="574" alt="Image" src="https://github.com/user-attachments/assets/a8dc95c8-d6fe-49f6-a5a1-7212fc145148" /> <img width="446" alt="Image" src="https://github.com/user-attachments/assets/a594574a-a28d-4509-8e51-50e575b7ad6c" />                    |         |                                 |
| 5  | pending  | ✔️     | ❌    | Halaman valid, data kosong           |<img width="578" alt="Image" src="https://github.com/user-attachments/assets/27f5e01d-081f-46df-a92a-4756b97ea4b7" /> <img width="602" alt="Image" src="https://github.com/user-attachments/assets/ac288dcc-fe42-4692-a964-586f5777e921" /> <img width="598" alt="Image" src="https://github.com/user-attachments/assets/3553986f-bdfb-4216-9f28-fcde85fa1878" />                    |         |                                 |
| 6  | selesai  | ✔️     | ❌    | Halaman valid, data kosong           |<img width="599" alt="Image" src="https://github.com/user-attachments/assets/ac6c8441-f94a-4930-a04c-7421048ba574" /> <img width="557" alt="Image" src="https://github.com/user-attachments/assets/d1be81a2-75de-448a-bb25-78606651957c" /> <img width="577" alt="Image" src="https://github.com/user-attachments/assets/cc48a924-7473-48fb-a335-dbb94b229996" />                    |         |                                 |
| 7  | pending  | ❌     | ❌    | Redirect ke login                    |<img width="578" alt="Image" src="https://github.com/user-attachments/assets/b2f23461-5118-47ec-98d4-285baa00c4b7" /> <img width="584" alt="Image" src="https://github.com/user-attachments/assets/57746678-40ee-4687-82bd-f49cbc97f14c" />                    |         |                                 |
| 8  | selesai  | ❌     | ❌    | Redirect ke login                    |<img width="578" alt="Image" src="https://github.com/user-attachments/assets/048062b2-dc65-47e6-a98f-3c5d28eade86" /> <img width="584" alt="Image" src="https://github.com/user-attachments/assets/bbdd4dad-6b6c-4764-be7b-274799adb5aa" />                    |         |                                 |

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

