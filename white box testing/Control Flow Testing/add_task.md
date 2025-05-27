### add_task
```python
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if 'username' in session:
        if request.method == 'POST':
            ...
            return redirect(url_for('dashboard'))
        return render_template('add_task.html')
    return redirect(url_for('login'))
```
| Kondisi Yang Diuji         | Hasil Yang Diharapkan      | Hasil Aktual | Status |
| -------------------------- | -------------------------- | ------------ | ------ |
| `session tidak ada`        | Redirect ke login          | Sesuai       | ✅      |
| `request.method == 'POST'` | Tambah task ke database    | Sesuai       | ✅      |
| `request.method != 'POST'` | Tampilkan form tambah task | Sesuai       | ✅      |
