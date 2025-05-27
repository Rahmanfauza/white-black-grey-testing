### delete_task
```python
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 'username' in session:
        ...
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))
```
| Kondisi Yang Diuji  | Hasil Yang Diharapkan  | Hasil Aktual | Status |
| ------------------- | ---------------------- | ------------ | ------ |
| `session tidak ada` | Redirect ke login      | Sesuai       | ✅      |
| `session ada`       | Task dihapus, redirect | Sesuai       | ✅      |
