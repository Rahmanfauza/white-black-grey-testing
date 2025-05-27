### login
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        ...
        if user and check_password_hash(user[2], password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Login gagal!')
    return render_template('login.html')
```
| Kondisi Yang Diuji                         | Hasil Yang Diharapkan | Hasil Aktual | Status |
| ------------------------------------------ | --------------------- | ------------ | ------ |
| `request.method == 'POST'`                 | Proses login dimulai  | Sesuai       | ✅      |
| `user ditemukan & password benar`          | Redirect ke dashboard | Sesuai       | ✅      |
| `user tidak ditemukan atau password salah` | Tampilkan flash error | Sesuai       | ✅      |
| `request.method != 'POST'`                 | Render login.html     | Sesuai       | ✅      |
