### logout
```python
@app.route('/logout')
def logout():
    session.clear()
    flash('Logout berhasil.', 'success')
    return redirect(url_for('login'))
```
| Kondisi Yang Diuji          | Hasil Yang Diharapkan              | Hasil Aktual | Status |
| --------------------------- | ---------------------------------- | ------------ | ------ |
| Pemanggilan route `/logout` | Membersihkan session & flash pesan | Sesuai       | ✅      |
| Setelah logout              | Redirect ke halaman login          | Sesuai       | ✅      |


### Catatan:
- Fungsi `logout()` **tidak memiliki percabangan** (`if`, `else`, `try`, dll).
- Namun tetap diuji untuk memastikan alurnya **linear, aman**, dan **berhasil menghapus session serta me-redirect** pengguna.
