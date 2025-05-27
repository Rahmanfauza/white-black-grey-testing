## register()
```python
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        ...
        if existing_user:
            flash('Username/email sudah digunakan')
        else:
            cursor.execute(...)
            conn.commit()
            return redirect(url_for('login'))
    return render_template('register.html')

| Kondisi Yang Diuji                         | Hasil Yang Diharapkan | Hasil Aktual | Status |
| ------------------------------------------ | --------------------- | ------------ | ------ |
| `request.method == 'POST'`                 | Proses login dimulai  | Sesuai       | ✅      |
| `user ditemukan & password benar`          | Redirect ke dashboard | Sesuai       | ✅      |
| `user tidak ditemukan atau password salah` | Tampilkan flash error | Sesuai       | ✅      |
| `request.method != 'POST'`                 | Render login.html     | Sesuai       | ✅      |
