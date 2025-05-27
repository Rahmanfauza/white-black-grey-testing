# Boundary Value Analysis (BVA)

## **Fitur yang Diuji**: [Registrasi, login, dan add task.]  

### **Parameter Input**:
| Parameter | Tipe Data | Batas Valid | Batas Invalid      |
|-----------|-----------|-------------|--------------------|
| Username  | String    | 1–12 chars | Kosong / >12 chars |
| Password  | String    | 1–12 chars | Kosong / >12 chars |
# Boundary Value Analysis (BVA)

## 1. Fitur Registrasi
| ID   | Parameter | Nilai Input      | Kategori       | Expected Result | Actual Result | Status (✔/✖) | Catatan |
|------|-----------|------------------|----------------|------------------|---------------|-------------|---------|
| BVA1 | Username  | "" (kosong)      | Batas Invalid  | Error            | Error         |    ✔          |         |
| BVA2 | Username  | "a"              | Batas Valid    | Sukses           | Sukses        |     ✔         |         |
| BVA3 | Username  | 12 chars        | Batas Valid    | Sukses           |  Sukses             |    ✔     |         |
| BVA4 | Username  | 13 chars        | Batas Invalid    | Error           |  Sukses             |   ✖     |         |
| BVA5 | Password  | "" (kosong)      | Batas Invalid  | Error            | Error              |     ✔        |         |
| BVA6 | Password  | "a"              | Batas Valid    | Sukses           |  Sukses             |     ✔        |         |
| BVA7 | Password  | "aa"             | Batas Valid    | Sukses           |  Sukses             |      ✔       |         |
| BVA8| Password  | 12 chars        | Batas Valid    | Sukses           |    Sukses           |       ✔      |         |
| BVA9| Password  | 13 chars        | Batas Invalid    | Error           |  Sukses             |      ✖       |         |

## 2. Fitur Login
| ID   | Parameter | Nilai Input      | Kategori       | Expected Result | Actual Result | Status (✔/✖) | Catatan |
|------|-----------|------------------|----------------|------------------|---------------|-------------|---------|
| BVA1 | Username  | "" (kosong)      | Batas Invalid  | Error            | Error              |    ✔         |         |
| BVA2 | Username  | "a"              | Batas Valid    | Tergantung auth  |  Sukses             |   ✔          |         |
| BVA3 | Password  | "" (kosong)      | Batas Invalid  | Error            | Error              |     ✔        |         |
| BVA4 | Password  | "a"              | Batas Valid    | Tergantung auth  | Sukses              |     ✔        |         |

### **Parameter Input**:
| Parameter | Tipe Data | Batas Valid | Batas Invalid      |
|-----------|-----------|-------------|--------------------|
| Title  | String    | 1–12 chars | Kosong / >12 chars |
| Description  | String    | 1– 12 chars | Kosong / >12 chars |

## 3. Fitur Add Task
| ID   | Parameter    | Nilai Input      | Kategori       | Expected Result | Actual Result | Status (✔/✖) | Catatan |
|------|--------------|------------------|----------------|------------------|---------------|-------------|---------|
| BVA1 | Title        | "" (kosong)      | Batas Invalid  | Error            | Error         |   ✔        |         |
| BVA2 | Title        | "a"              | Batas Valid    | Sukses           | Sukses        |    ✔         |         |
| BVA3 | Title        | 12 chars        | Batas Valid    | Sukses           |  Sukses             |  ✔           |         |
| BVA4 | Title        | 13 chars        | Batas Invalid  | Error            |  Sukses             |  ✖          |         |
| BVA5 | Description  | "" (kosong)      | Batas Valid*   | Sukses           | Sukses              | ✔            |         |
| BVA6 | Description  | 1 char           | Batas Valid    | Sukses           | Sukses              | ✔           |         |
| BVA7| Description  | 13 chars       | Batas Invalid    | Error           |     Sukses          |  ✖            |         |
---

# Equivalence Partitioning (EP) Test Cases

## Fitur yang Diuji: Register, Login, dan Add Task

### 1. Fitur Register
**Deskripsi**: Pendaftaran user baru dengan username, email, dan password.

#### Partisi Input:
| Input     | Partisi Valid               | Partisi Invalid                 |
|-----------|-----------------------------|----------------------------------|
| Username  | String unik (≥1 karakter)   | Kosong/sudah ada di database    |
| Email     | Format valid & unik         | Format invalid/sudah terdaftar  |
| Password  | String (≥1 karakter)        | Kosong                          |

#### Test Case:
| ID  | Input                                   | Partisi  | Expected Result                  | Catatan               |
|-----|-----------------------------------------|----------|-----------------------------------|-----------------------|
| EP1  | `("admin", "rahmanfauza@mail.com", "123")`| Valid    | Registrasi sukses                 | Semua input valid     |
| EP2  | `("", "rahmanfauza@mail.com", "123")`       | Invalid  | Error: "Username kosong"          | Username kosong       |
| EP3  | `("admin", "rahmanfauzaemail", "123")`   | Invalid  | Error: "Email invalid"            | Format email salah    |
| EP4  | `("admin", "rahmanfauza@mail.com", "")`        | Invalid  | Error: "Password kosong"          | Password kosong       |

---

### 2. Fitur Login
**Deskripsi**: Autentikasi user dengan username dan password.

#### Partisi Input:
| Input     | Partisi Valid               | Partisi Invalid                 |
|-----------|-----------------------------|----------------------------------|
| Username  | Terdaftar di database       | Tidak terdaftar/kosong          |
| Password  | Sesuai dengan database      | Salah/kosong                    |

#### Test Case:
| ID  | Input                     | Partisi  | Expected Result          | Catatan               |
|-----|---------------------------|----------|---------------------------|-----------------------|
| EP1  | `("admin", "123")`  | Valid    | Login sukses              | Credential valid      |
| EP2  | `("", "123")`       | Invalid  | Error: "Username kosong"  | Username kosong       |
| EP3  | `("admin", "")`           | Invalid  | Error: "Password kosong"  | Password kosong       |
| EP4  | `("admin", "321")`      | Invalid  | Error: "Password salah"   | Password tidak match  |

---

### 3. Fitur Add Task
**Deskripsi**: Menambahkan task baru dengan title dan description.

#### Partisi Input:
| Input        | Partisi Valid          | Partisi Invalid       |
|--------------|------------------------|-----------------------|
| Title        | String (≥1 karakter)   | Kosong                |
| Description  | String (boleh kosong)  | -                     |

#### Test Case:
| ID  | Input                              | Partisi  | Expected Result               | Catatan               |
|-----|------------------------------------|----------|--------------------------------|-----------------------|
| EP1  | `("Task valid", "Deskripsi")`     | Valid    | Task berhasil ditambahkan      | Semua input valid     |
| EP2  | `("", "Deskripsi")`               | Invalid  | Error: "Title kosong"          | Title kosong          |
| EP3  | `("Task", "")`                    | Valid    | Task berhasil ditambahkan      | Description boleh kosong |

