# Test Case Design

## Boundary Value Analysis (BVA)

### 1. Registrasi

**Input Field: Username** (Asumsi: Min Length=3, Max Length=20)
- TC-BVA-REG-USR-01: Input 2 karakter (Invalid - Below Min)
- TC-BVA-REG-USR-02: Input 3 karakter (Valid - Min)
- TC-BVA-REG-USR-03: Input 4 karakter (Valid - Min+1)
- TC-BVA-REG-USR-04: Input 19 karakter (Valid - Max-1)
- TC-BVA-REG-USR-05: Input 20 karakter (Valid - Max)
- TC-BVA-REG-USR-06: Input 21 karakter (Invalid - Above Max)

**Input Field: Email** (BVA kurang relevan, fokus pada format di EP)

**Input Field: Password** (Asumsi: Min Length=6, Max Length=30)
- TC-BVA-REG-PWD-01: Input 5 karakter (Invalid - Below Min)
- TC-BVA-REG-PWD-02: Input 6 karakter (Valid - Min)
- TC-BVA-REG-PWD-03: Input 7 karakter (Valid - Min+1)
- TC-BVA-REG-PWD-04: Input 29 karakter (Valid - Max-1)
- TC-BVA-REG-PWD-05: Input 30 karakter (Valid - Max)
- TC-BVA-REG-PWD-06: Input 31 karakter (Invalid - Above Max)

### 2. Login

**Input Field: Username** (Menggunakan batas yang sama dengan Registrasi)
- TC-BVA-LOG-USR-01: Input 2 karakter (Invalid - Below Min)
- TC-BVA-LOG-USR-02: Input 3 karakter (Valid - Min)
- TC-BVA-LOG-USR-03: Input 20 karakter (Valid - Max)
- TC-BVA-LOG-USR-04: Input 21 karakter (Invalid - Above Max)

**Input Field: Password** (Menggunakan batas yang sama dengan Registrasi)
- TC-BVA-LOG-PWD-01: Input 5 karakter (Invalid - Below Min)
- TC-BVA-LOG-PWD-02: Input 6 karakter (Valid - Min)
- TC-BVA-LOG-PWD-03: Input 30 karakter (Valid - Max)
- TC-BVA-LOG-PWD-04: Input 31 karakter (Invalid - Above Max)

### 3. Tambah Tugas

**Input Field: Title** (Asumsi: Min Length=1, Max Length=100)
- TC-BVA-TSK-TTL-01: Input 0 karakter (Invalid - Below Min/Empty)
- TC-BVA-TSK-TTL-02: Input 1 karakter (Valid - Min)
- TC-BVA-TSK-TTL-03: Input 2 karakter (Valid - Min+1)
- TC-BVA-TSK-TTL-04: Input 99 karakter (Valid - Max-1)
- TC-BVA-TSK-TTL-05: Input 100 karakter (Valid - Max)
- TC-BVA-TSK-TTL-06: Input 101 karakter (Invalid - Above Max)

**Input Field: Description** (Asumsi: Max Length=500, Opsional)
- TC-BVA-TSK-DSC-01: Input 0 karakter (Valid - Empty/Min)
- TC-BVA-TSK-DSC-02: Input 1 karakter (Valid - Min+1)
- TC-BVA-TSK-DSC-03: Input 499 karakter (Valid - Max-1)
- TC-BVA-TSK-DSC-04: Input 500 karakter (Valid - Max)
- TC-BVA-TSK-DSC-05: Input 501 karakter (Invalid - Above Max)


