## Fungsi Delete Task

```python
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 'username' in session:
        ...
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))
```
### Flow Diagram
```
(1) ───> [session ada?]
  |           |
  |           v
  |     (2) Hapus task
  |           |
  |     (3) Redirect dashboard
  |
  v
(4) Redirect ke login
```
