## Fungsi Update Task

```python
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    if 'username' in session:
        ...
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))
```
Flow Diagram
```
(1) ───> [session ada?]
  |           |
  |           v
  |     (2) Update task
  |           |
  |     (3) Redirect dashboard
  |
  v
(4) Redirect ke login
```
