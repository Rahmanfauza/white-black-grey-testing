📋 Tabel Uji

| TC | Status  | Login | Data | Hasil yang Diharapkan             | Hasil Aktual                  | Sesuai? | Catatan |
|----|---------|-------|------|-----------------------------------|-------------------------------|---------|---------|
| 1  | pending | ✔️     | ✔️    | Tampil normal                     | ![TC1](https://github.com/user-attachments/assets/0987cd22-c152-44c6-a637-c0efeba4031e) | ✅ | Tampilan normal, data tampil sesuai status |
| 2  | selesai | ✔️     | ✔️    | Tampil dengan status selesai      | ![TC2a](https://github.com/user-attachments/assets/baa10c1c-2803-4c5e-a0a6-cb9cbd166741) <br> ![TC2b](https://github.com/user-attachments/assets/91cd1281-0642-49d9-997b-78075590889e) | ✅ | Status “selesai” tampil sesuai, tidak ada error |
| 3  | pending | ❌     | ✔️    | Redirect ke login                 | ![TC3a](https://github.com/user-attachments/assets/4169eca9-6ebe-43b5-827a-e00195b9664c) <br> ![TC3b](https://github.com/user-attachments/assets/cb45ba08-43b4-4c71-b75f-48fd9cb3958c) <br> ![TC3c](https://github.com/user-attachments/assets/b8f57448-f45a-444c-a8e8-63aa608d9c84) | ✅ | Tidak bisa akses data, sistem langsung redirect |
| 4  | selesai | ❌     | ✔️    | Redirect ke login                 | ![TC4a](https://github.com/user-attachments/assets/8c5c2006-793f-4655-b860-0caabcb549d2) <br> ![TC4b](https://github.com/user-attachments/assets/a8dc95c8-d6fe-49f6-a5a1-7212fc145148) <br> ![TC4c](https://github.com/user-attachments/assets/a594574a-a28d-4509-8e51-50e575b7ad6c) | ✅ | Proteksi login berhasil; tidak bisa akses tanpa autentikasi |
| 5  | pending | ✔️     | ❌    | Halaman valid, data kosong        | ![TC5a](https://github.com/user-attachments/assets/27f5e01d-081f-46df-a92a-4756b97ea4b7) <br> ![TC5b](https://github.com/user-attachments/assets/ac288dcc-fe42-4692-a964-586f5777e921) <br> ![TC5c](https://github.com/user-attachments/assets/3553986f-bdfb-4216-9f28-fcde85fa1878) | ✅ | UI menampilkan pesan “no data” dengan baik |
| 6  | selesai | ✔️     | ❌    | Halaman valid, data kosong        | ![TC6a](https://github.com/user-attachments/assets/ac6c8441-f94a-4930-a04c-7421048ba574) <br> ![TC6b](https://github.com/user-attachments/assets/d1be81a2-75de-448a-bb25-78606651957c) <br> ![TC6c](https://github.com/user-attachments/assets/cc48a924-7473-48fb-a335-dbb94b229996) | ✅ | Tampilan tetap stabil meskipun tidak ada data |
| 7  | pending | ❌     | ❌    | Redirect ke login                 | ![TC7a](https://github.com/user-attachments/assets/b2f23461-5118-47ec-98d4-285baa00c4b7) <br> ![TC7b](https://github.com/user-attachments/assets/57746678-40ee-4687-82bd-f49cbc97f14c) | ✅ | Sistem aman dari akses tidak sah, langsung redirect |
| 8  | selesai | ❌     | ❌    | Redirect ke login                 | ![TC8a](https://github.com/user-attachments/assets/048062b2-dc65-47e6-a98f-3c5d28eade86) <br> ![TC8b](https://github.com/user-attachments/assets/bbdd4dad-6b6c-4764-be7b-274799adb5aa) | ✅ | Mekanisme keamanan konsisten di semua status |

### 📌 Keterangan Kolom
- **Status:** Status tugas yang dipilih
- **Login:** Kondisi apakah user sudah login
- **Data:** Apakah ada data task di database
- **Hasil yang Diharapkan:** Prediksi perilaku sistem
- **Hasil Aktual:** Gambar hasil dari uji nyata
- **Sesuai?:** ✅ jika hasil sesuai ekspektasi
- **Catatan:** Penjelasan hasil & temuan
