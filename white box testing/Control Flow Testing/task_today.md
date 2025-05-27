### task_today
```python
@app.route('/today')
def tasks_today():
    if 'username' in session:
        ...
        return render_template('tasks_today.html', tasks=tasks)
    return redirect(url_for('login'))
```
| Kondisi Yang Diuji  | Hasil Yang Diharapkan         | Hasil Aktual | Status |
| ------------------- | ----------------------------- | ------------ | ------ |
| `session tidak ada` | Redirect ke login             | Sesuai       | ✅      |
| `session ada`       | Tampilkan task untuk hari ini | Sesuai       | ✅      |
