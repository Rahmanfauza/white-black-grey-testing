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

| ID             | Parameter | Nilai Input      | Kategori       | Expected Result | Actual Result | Status (✔/✖) | Screenshot | Catatan |
|----------------|-----------|------------------|----------------|-----------------|---------------|-------------|------------|---------|
| TC-REG-BVA-001 | Username  | "" (kosong)      | Batas Invalid  | Error           | Error         | ✔           |            |         |
| TC-REG-BVA-002 | Username  | "a"              | Batas Valid    | Sukses          | Sukses        | ✔           |            | Min     |
| TC-REG-BVA-003 | Username  | 12 chars         | Batas Valid    | Sukses          | Sukses        | ✔           |            | Max     |
| TC-REG-BVA-004 | Username  | 13 chars         | Batas Invalid  | Error           | Sukses        | ✖           |            | Max+1   |
| TC-REG-BVA-005 | Password  | "" (kosong)      | Batas Invalid  | Error           | Error         | ✔           |            |         |
| TC-REG-BVA-006 | Password  | "a"              | Batas Valid    | Sukses          | Sukses        | ✔           |            | Min     |
| TC-REG-BVA-007 | Password  | "aa"             | Batas Valid    | Sukses          | Sukses        | ✔           |            | Min+1   |
| TC-REG-BVA-008 | Password  | 12 chars         | Batas Valid    | Sukses          | Sukses        | ✔           |            | Max     |
| TC-REG-BVA-009 | Password  | 13 chars         | Batas Invalid  | Error           | Sukses        | ✖           |            | Max+1   |

**Fitur: Login**

| ID             | Parameter | Nilai Input      | Kategori       | Expected Result | Actual Result | Status (✔/✖) | Screenshot | Catatan |
|----------------|-----------|------------------|----------------|-----------------|---------------|-------------|------------|---------|
| TC-LOG-BVA-001 | Username  | "" (kosong)      | Batas Invalid  | Error           | Error         | ✔           |            |         |
| TC-LOG-BVA-002 | Username  | "a"              | Batas Valid    | Tergantung auth | Sukses        | ✔           |            | Min     |
| TC-LOG-BVA-003 | Password  | "" (kosong)      | Batas Invalid  | Error           | Error         | ✔           |            |         |
| TC-LOG-BVA-004 | Password  | "a"              | Batas Valid    | Tergantung auth | Sukses        | ✔           |            | Min     |

**Fitur: Tambah Tugas (Add Task)**

| ID             | Parameter    | Nilai Input      | Kategori       | Expected Result | Actual Result | Status (✔/✖) | Screenshot | Catatan |
|----------------|--------------|------------------|----------------|-----------------|---------------|-------------|------------|---------|
| TC-ADD-BVA-001 | Title        | "" (kosong)      | Batas Invalid  | Error           | Error         | ✔           |            |         |
| TC-ADD-BVA-002 | Title        | "a"              | Batas Valid    | Sukses          | Sukses        | ✔           |            | Min     |
| TC-ADD-BVA-003 | Title        | 12 chars         | Batas Valid    | Sukses          | Sukses        | ✔           |            | Max     |
| TC-ADD-BVA-004 | Title        | 13 chars         | Batas Invalid  | Error           | Sukses        | ✖           |            | Max+1   |
| TC-ADD-BVA-005 | Description  | "" (kosong)      | Batas Valid*   | Sukses          | Sukses        | ✔           |            | Min (Opsional) |
| TC-ADD-BVA-006 | Description  | "a"              | Batas Valid    | Sukses          | Sukses        | ✔           |            | Min+1   |
| TC-ADD-BVA-007 | Description  | 12 chars         | Batas Valid    | Sukses          | Sukses        | ✔           |            | Max     |
| TC-ADD-BVA-008 | Description  | 13 chars         | Batas Invalid  | Error           | Sukses        | ✖           |            | Max+1   |

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

| ID            | Deskripsi Input                         | Contoh Input                            | Partisi | Expected Result          | Screenshot | Catatan            |
|---------------|-----------------------------------------|-----------------------------------------|---------|--------------------------|------------|--------------------|
| TC-REG-EP-001 | Semua input valid                       | `("admin", "rahman@mail.com", "123")` | Valid   | Registrasi sukses        |            |                    |
| TC-REG-EP-002 | Username kosong                         | `("", "rahman@mail.com", "123")`      | Invalid | Error: "Username kosong" |            |                    |
| TC-REG-EP-003 | Format email salah                      | `("admin", "rahmanemail", "123")`       | Invalid | Error: "Email invalid"   |            |                    |
| TC-REG-EP-004 | Password kosong                         | `("admin", "rahman@mail.com", "")`      | Invalid | Error: "Password kosong" |            |                    |
| TC-REG-EP-005 | Username sudah ada (asumsi "admin" ada) | `("admin", "baru@mail.com", "456")`   | Invalid | Error: "Username exists" |            | Perlu data existing |
| TC-REG-EP-006 | Email sudah ada (asumsi email ada)      | `("userbaru", "rahman@mail.com", "456")`| Invalid | Error: "Email exists"    |            | Perlu data existing |

### 2.2. Fitur Login

**Partisi Input:**

| Input     | Partisi Valid               | Partisi Invalid                 |
|-----------|-----------------------------|----------------------------------|
| Username  | Terdaftar di database       | Tidak terdaftar / Kosong         |
| Password  | Sesuai dengan database      | Salah / Kosong                   |

**Kasus Uji EP:**

| ID            | Deskripsi Input         | Contoh Input        | Partisi | Expected Result          | Screenshot | Catatan            |
|---------------|-------------------------|---------------------|---------|--------------------------|------------|--------------------|
| TC-LOG-EP-001 | Kredensial valid        | `("admin", "123")`  | Valid   | Login sukses             |            |                    |
| TC-LOG-EP-002 | Username kosong         | `("", "123")`       | Invalid | Error: "Username kosong" |            |                    |
| TC-LOG-EP-003 | Password kosong         | `("admin", "")`       | Invalid | Error: "Password kosong" |            |                    |
| TC-LOG-EP-004 | Password salah          | `("admin", "321")`  | Invalid | Error: "Password salah"  |            |                    |
| TC-LOG-EP-005 | Username tidak terdaftar| `("userX", "123")`  | Invalid | Error: "User not found"|            |                    |

### 2.3. Fitur Tambah Tugas (Add Task)

**Partisi Input:**

| Input        | Partisi Valid          | Partisi Invalid       |
|--------------|------------------------|-----------------------|
| Title        | String (≥1 karakter)   | Kosong                |
| Description  | String (boleh kosong)  | -                     |

**Kasus Uji EP:**

| ID            | Deskripsi Input         | Contoh Input                   | Partisi | Expected Result            | Screenshot | Catatan                  |
|---------------|-------------------------|--------------------------------|---------|----------------------------|------------|--------------------------|
| TC-ADD-EP-001 | Semua input valid       | `("Task valid", "Deskripsi")`  | Valid   | Task berhasil ditambahkan  |            |                          |
| TC-ADD-EP-002 | Title kosong            | `("", "Deskripsi")`            | Invalid | Error: "Title kosong"      |            |                          |
| TC-ADD-EP-003 | Description kosong      | `("Task", "")`                 | Valid   | Task berhasil ditambahkan  |            | Description boleh kosong |

