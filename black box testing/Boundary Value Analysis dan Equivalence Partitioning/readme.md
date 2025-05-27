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
