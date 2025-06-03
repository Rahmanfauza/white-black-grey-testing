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
