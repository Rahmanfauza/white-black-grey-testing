# Comparison Testing Report

## **Fitur yang Diuji**: Register, Login, dan Add Task  
**Tujuan**: Membandingkan perubahan fungsionalitas antara versi lama (`v1.0`) dan versi baru (`v2.0`).

---

### **1. Fitur Register**
#### **Perubahan**: Batas panjang username dan password (12 karakter)  
| **Test ID** | **Input** (`username`, `email`, `password`)       | **Versi Lama (`v1.0`)**       | **Versi Baru (`v2.0`)**        | **Status** | **Catatan**                  |
|-------------|--------------------------------------------------|-------------------------------|--------------------------------|------------|------------------------------|
| CT-R1       | `("userbaru", "baru@mail.com", "pass123")`       | Bisa >12 karakter            | Dibatasi 12 karakter           | ✅         | Perubahan fungsionalitas     |
| CT-R2       | `("userbaru1234567", "valid@mail.com", "pass1234567890")` | Diterima | Error: "Username/password max 12 karakter" | ⚠️ | Validasi baru |

---

### **2. Fitur Login**
#### **Perubahan**: Batas panjang input dan pesan error  
| **Test ID** | **Input** (`username`, `password`) | **Versi Lama (`v1.0`)**       | **Versi Baru (`v2.0`)**        | **Status** | **Catatan**                  |
|-------------|------------------------------------|-------------------------------|--------------------------------|------------|------------------------------|
| CT-L1       | `("user1234567", "pass1234567890")` | Diterima                     | Error: "Input max 12 karakter" | ⚠️       | Validasi baru di `v2.0`      |
| CT-L2       | `("user1", "pass1")`               | Sukses                        | Sukses                         | ✅         | Tidak terpengaruh perubahan  |

---


### **Legenda Status**  
- ✅ **Consistent**: Perilaku sama atau perubahan disengaja.  
- ⚠️ **Changed**: Perilaku berubah karena validasi baru.  

---

