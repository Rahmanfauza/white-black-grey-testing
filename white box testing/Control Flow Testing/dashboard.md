### dashboard
```python
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        ...
        return render_template('dashboard.html', tasks=tasks)
    else:
        return redirect(url_for('login'))

| Kondisi Yang Diuji      | Hasil Yang Diharapkan       | Hasil Aktual | Status |
| ----------------------- | --------------------------- | ------------ | ------ |
| `'username' in session` | Tampilkan halaman dashboard | Sesuai       | ✅      |
| `else (tidak login)`    | Redirect ke login           | Sesuai       | ✅      |
