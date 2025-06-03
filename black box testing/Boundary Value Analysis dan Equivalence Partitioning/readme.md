# Rangkuman Skenario Pengujian Black Box (Update)

Boundary Value Analysis adalah teknik desain test case black-box yang melengkapi Equivalence Partitioning. Teknik ini fokus pada pengujian nilai-nilai yang berada di "batas" atau "tepi" dari partisi ekuivalen.

## 1. Boundary Value Analysis (BVA)

Pengujian BVA fokus pada nilai-nilai di batas valid dan invalid dari suatu input.

### 1.1. Definisi Parameter dan Batas (BVA)

| Fitur         | Parameter    | Tipe Data | Batas Valid (Asumsi) | Batas Invalid (Asumsi)      |
|---------------|--------------|-----------|----------------------|-----------------------------|
| Registrasi    | Username     | String    | 1–12 karakter        | Kosong / >12 karakter       |
| Registrasi    | Password     | String    | 1–12 karakter        | Kosong / >12 karakter       |
| Login         | Username     | String    | 1–12 karakter        | Kosong / >12 karakter       |
| Login         | Password     | String    | 1–12 karakter        | Kosong / >12 karakter       |
| Tambah Tugas  | Title        | String    | 1–12 karakter        | Kosong / >12 karakter       |
| Tambah Tugas  | Description  | String    | 0–12 karakter*       | >12 karakter                |

_* Catatan: Description pada BVA di file asli memiliki batas bawah 0 (kosong) yang dianggap valid, dan batas atas 12._

### 1.2. Kasus Uji BVA

**Fitur: Registrasi**

| ID             | Parameter | Nilai Input       | Kategori       | Expected Result | Actual Result | Status (✔/✖) | Screenshot                                                                                          | Catatan |
|----------------|-----------|-------------------|----------------|-----------------|----------------|---------------|------------------------------------------------------------------------------------------------------|---------|
| TC-REG-BVA-001 | Username  | "" (kosong)       | Batas Invalid  | Error           | Error          | ✔             | <img src="https://github.com/user-attachments/assets/42719675-53c6-4221-a6aa-3eb5144e5ae8" width="250"/> |         |
| TC-REG-BVA-002 | Username  | "a"               | Batas Valid    | Sukses          | Sukses         | ✔             | <img src="https://github.com/user-attachments/assets/6c745df5-e5f2-43a3-864e-ebf9c9ae3eb0" width="250"/> | Min     |
| TC-REG-BVA-003 | Username  | 12 chars          | Batas Valid    | Sukses          | Sukses         | ✔             | <img src="https://github.com/user-attachments/assets/58cb216a-f102-46fb-913d-a6c8a6530203" width="250"/> | Max     |
| TC-REG-BVA-004 | Username  | 13 chars          | Batas Invalid  | Error           | Sukses         | ✖             | <img src="https://github.com/user-attachments/assets/58cb216a-f102-46fb-913d-a6c8a6530203" width="250"/> | Max+1   |
| TC-REG-BVA-005 | Password  | "" (kosong)       | Batas Invalid  | Error           | Error          | ✔             | <img src="https://github.com/user-attachments/assets/7016939a-257d-4840-8a71-1b625b4f9644" width="250"/> |         |
| TC-REG-BVA-006 | Password  | "a"               | Batas Valid    | Sukses          | Sukses         | ✔             | <img src="https://github.com/user-attachments/assets/58cb216a-f102-46fb-913d-a6c8a6530203" width="250"/> | Min     |
| TC-REG-BVA-007 | Password  | "aa"              | Batas Valid    | Sukses          | Sukses         | ✔             | <img src="https://github.com/user-attachments/assets/58cb216a-f102-46fb-913d-a6c8a6530203" width="250"/> | Min+1   |
| TC-REG-BVA-008 | Password  | 12 chars          | Batas Valid    | Sukses          | Sukses         | ✔             | <img src="https://github.com/user-attachments/assets/e18f6308-e86e-4af7-ad49-af0e0ef64c82" width="250"/> | Max     |
| TC-REG-BVA-009 | Password  | 13 chars          | Batas Invalid  | Error           | Sukses         | ✖             | <img src="https://github.com/user-attachments/assets/7335d617-4d6e-43e9-b71c-f4f496a0f52a" width="250"/> | Max+1   |


**Fitur: Login**

| ID             | Parameter | Nilai Input       | Kategori       | Expected Result | Actual Result | Status (✔/✖) | Screenshot                                                                                          | Catatan |
|----------------|-----------|-------------------|----------------|-----------------|----------------|---------------|------------------------------------------------------------------------------------------------------|---------|
| TC-LOG-BVA-001 | Username  | "" (kosong)       | Batas Invalid  | Error           | Error          | ✔             | <img src="https://github.com/user-attachments/assets/75fe4ac0-29d6-4637-8f9d-41fccd6ec91d" width="250"/> |         |
| TC-LOG-BVA-002 | Username  | "a"               | Batas Valid    | Tergantung auth | Sukses         | ✔             | <img src="https://github.com/user-attachments/assets/d1369163-4453-4492-a47d-7bc90aea2ab3" width="250"/> | Min     |
| TC-LOG-BVA-003 | Password  | "" (kosong)       | Batas Invalid  | Error           | Error          | ✔             | <img src="https://github.com/user-attachments/assets/e3ff24d2-41ef-43d9-8362-a1808bae010f" width="250"/> |         |
| TC-LOG-BVA-004 | Password  | "a"               | Batas Valid    | Tergantung auth | Sukses         | ✔             | <img src="https://github.com/user-attachments/assets/d1369163-4453-4492-a47d-7bc90aea2ab3" width="250"/> | Min     |



**Fitur: Tambah Tugas (Add Task)**

| ID             | Parameter   | Nilai Input      | Kategori       | Expected Result | Actual Result | Status (✔/✖) | Screenshot                                                                                          | Catatan         |
|----------------|-------------|------------------|----------------|-----------------|----------------|---------------|------------------------------------------------------------------------------------------------------|-----------------|
| TC-ADD-BVA-001 | Title       | "" (kosong)      | Batas Invalid  | Error           | Error          | ✔             | <img src="https://github.com/user-attachments/assets/b0848ce1-70f3-45b5-940b-ebc41ab54153" width="250"/> |                 |
| TC-ADD-BVA-002 | Title       | "a"              | Batas Valid    | Sukses          | Sukses         | ✔             | <img src="https://github.com/user-attachments/assets/655d80db-0d27-4c72-87a5-e43c7b28c7a7" width="250"/> | Min             |
| TC-ADD-BVA-003 | Title       | 12 chars         | Batas Valid    | Sukses          | Sukses         | ✔             | <img src="https://github.com/user-attachments/assets/9d63dec6-2132-4a10-bc71-c12461581e68" width="250"/> | Max             |
| TC-ADD-BVA-004 | Title       | 13 chars         | Batas Invalid  | Error           | Sukses         | ✖             | <img src="https://github.com/user-attachments/assets/9d63dec6-2132-4a10-bc71-c12461581e68" width="250"/> | Max+1           |
| TC-ADD-BVA-005 | Description | "" (kosong)      | Batas Valid*   | Sukses          | Sukses         | ✔             | <img src="https://github.com/user-attachments/assets/5b53b746-1164-456c-a3ae-3c9002d67dc8" width="250"/> | Min (Opsional)  |
| TC-ADD-BVA-006 | Description | "a"              | Batas Valid    | Sukses          | Sukses         | ✔             | <img src="https://github.com/user-attachments/assets/c7e0c262-d38f-40fe-98a4-dba5601ea413" width="250"/> | Min+1           |
| TC-ADD-BVA-007 | Description | 12 chars         | Batas Valid    | Sukses          | Sukses         | ✔             | <img src="https://github.com/user-attachments/assets/d2ed49cc-45e5-4cd8-a3db-cca359fbdcc0" width="250"/> | Max             |
| TC-ADD-BVA-008 | Description | 13 chars         | Batas Invalid  | Error           | Sukses         | ✖             | <img src="https://github.com/user-attachments/assets/d2ed49cc-45e5-4cd8-a3db-cca359fbdcc0" width="250"/> | Max+1           |


## 2. Equivalence Partitioning (EP)

Equivalence Partitioning (juga dikenal sebagai Equivalence Class Partitioning) adalah teknik desain test case black-box yang bertujuan untuk mengurangi jumlah total test case yang perlu dijalankan sambil tetap memastikan cakupan pengujian yang memadai. Teknik ini bekerja dengan membagi data input suatu komponen perangkat lunak menjadi beberapa partisi atau kelas ekuivalen.

### 2.1. Fitur Registrasi

**Partisi Input:**

| Input     | Partisi Valid               | Partisi Invalid                 |
|-----------|-----------------------------|----------------------------------|
| Username  | String unik (≥1 karakter)   | Kosong / Sudah ada di database   |
| Email     | Format valid & unik         | Format invalid / Sudah terdaftar |
| Password  | String (≥1 karakter)        | Kosong                           |

**Kasus Uji EP:**

| ID            | Deskripsi Input                         | Contoh Input                              | Partisi | Expected Result          | Screenshot                                                                                          | Catatan             |
|---------------|------------------------------------------|--------------------------------------------|---------|---------------------------|------------------------------------------------------------------------------------------------------|---------------------|
| TC-REG-EP-001 | Semua input valid                       | `("admin", "rahmanf@mail.com", "123")`     | Valid   | Registrasi sukses         | <img src="https://github.com/user-attachments/assets/489243d6-dc62-4acc-ae26-d7027afe0411" width="250"/> |                     |
| TC-REG-EP-002 | Username kosong                         | `("", "rahmanf@mail.com", "123")`          | Invalid | Error: "Username kosong"  | <img src="https://github.com/user-attachments/assets/1875dda6-3734-4914-b180-43e76abec3bc" width="250"/> |                     |
| TC-REG-EP-003 | Format email salah                      | `("admin", "rahmanemail", "123")`          | Invalid | Error: "Email invalid"    | <img src="https://github.com/user-attachments/assets/fd7c6a51-726a-4848-9bc6-46670f46133d" width="250"/> |                     |
| TC-REG-EP-004 | Password kosong                         | `("admin", "rahman@mail.com", "")`         | Invalid | Error: "Password kosong"  | <img src="https://github.com/user-attachments/assets/e5fe88b6-c560-4aa0-8c64-a44dd897deee" width="250"/> |                     |
| TC-REG-EP-005 | Username sudah ada (asumsi "admin" ada) | `("admin", "baru@mail.com", "456")`        | Invalid | Error: "Username exists"  | <img src="https://github.com/user-attachments/assets/0e438aad-ac9f-4c6a-b030-267d0a27a54c" width="250"/> | Perlu data existing |
| TC-REG-EP-006 | Email sudah ada (asumsi email ada)      | `("userbaru", "rahman@mail.com", "456")`   | Invalid | Error: "Email exists"     | <img src="https://github.com/user-attachments/assets/0e438aad-ac9f-4c6a-b030-267d0a27a54c" width="250"/> | Perlu data existing |

### 2.2. Fitur Login

**Partisi Input:**

| Input     | Partisi Valid               | Partisi Invalid                 |
|-----------|-----------------------------|----------------------------------|
| Username  | Terdaftar di database       | Tidak terdaftar / Kosong         |
| Password  | Sesuai dengan database      | Salah / Kosong                   |

**Kasus Uji EP:**

| ID            | Deskripsi Input          | Contoh Input         | Partisi | Expected Result            | Screenshot                                                                                          | Catatan |
|---------------|---------------------------|------------------------|---------|-----------------------------|------------------------------------------------------------------------------------------------------|---------|
| TC-LOG-EP-001 | Kredensial valid          | `("admin", "123")`     | Valid   | Login sukses                | <img src="https://github.com/user-attachments/assets/3a15c5fc-63ed-49fe-bd2b-e41c629bc1a3" width="250"/> |         |
| TC-LOG-EP-002 | Username kosong           | `("", "123")`          | Invalid | Error: "Username kosong"    | <img src="https://github.com/user-attachments/assets/10fbde19-e81e-4c6b-bf1f-7b0d22b040fa" width="250"/> |         |
| TC-LOG-EP-003 | Password kosong           | `("admin", "")`        | Invalid | Error: "Password kosong"    | <img src="https://github.com/user-attachments/assets/16092a45-57d2-4809-9380-c1cf964ce623" width="250"/> |         |
| TC-LOG-EP-004 | Password salah            | `("admin", "321")`     | Invalid | Error: "Password salah"     | <img src="https://github.com/user-attachments/assets/d2f1ed29-12b2-4030-af00-ed096b147151" width="250"/> |         |
| TC-LOG-EP-005 | Username tidak terdaftar | `("userX", "123")`     | Invalid | Error: "User not found"     | <img src="https://github.com/user-attachments/assets/d2f1ed29-12b2-4030-af00-ed096b147151" width="250"/> |         |


### 2.3. Fitur Tambah Tugas (Add Task)

**Partisi Input:**

| Input        | Partisi Valid          | Partisi Invalid       |
|--------------|------------------------|-----------------------|
| Title        | String (≥1 karakter)   | Kosong                |
| Description  | String (boleh kosong)  | -                     |

**Kasus Uji EP:**

| ID            | Deskripsi Input         | Contoh Input                   | Partisi | Expected Result            | Screenshot                                                                                           | Catatan                  |
|---------------|-------------------------|--------------------------------|---------|----------------------------|--------------------------------------------------------------------------------------------------------|--------------------------|
| TC-ADD-EP-001 | Semua input valid       | `("Task valid", "Deskripsi")`  | Valid   | Task berhasil ditambahkan  | <img src="https://github.com/user-attachments/assets/edd954f3-9613-442c-8c3d-270c0449b6f1" width="250"/> |                          |
| TC-ADD-EP-002 | Title kosong            | `("", "Deskripsi")`            | Invalid | Error: "Title kosong"       | <img src="https://github.com/user-attachments/assets/6d026bd6-60c2-4116-bcca-3b90c52b1148" width="250"/> |                          |
| TC-ADD-EP-003 | Description kosong      | `("Task", "")`                 | Valid   | Task berhasil ditambahkan  | <img src="https://github.com/user-attachments/assets/95a065db-e1b7-4d25-898a-9c35ab0a6326" width="250"/> | Description boleh kosong |


