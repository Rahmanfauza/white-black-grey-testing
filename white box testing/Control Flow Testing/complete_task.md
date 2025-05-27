### complete_task
```python
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 'username' in session:
        ...
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))
```
| Kondisi Yang Diuji  | Hasil Yang Diharapkan       | Hasil Aktual | Status |
| ------------------- | --------------------------- | ------------ | ------ |
| `session tidak ada` | Redirect ke login           | Sesuai       | ✅      |
| `session ada`       | Status task menjadi selesai | Sesuai       | ✅      |
