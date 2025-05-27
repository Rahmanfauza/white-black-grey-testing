### update_task
```python
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    if 'username' in session:
        ...
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))
```
| Kondisi Yang Diuji  | Hasil Yang Diharapkan | Hasil Aktual | Status |
| ------------------- | --------------------- | ------------ | ------ |
| `session tidak ada` | Redirect ke login     | Sesuai       | ✅      |
| `session ada`       | Task diperbarui       | Sesuai       | ✅      |
