## Fungsi Add Task

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
## Flow Diagram
```
(1) ──> [session ada?]
  |           |
  |           v
  |   [request.method == 'POST']
  |       |           \
  |       v            v
  | (2) Tambah task  (3) Tampilkan form
  |       |
  | (4) Redirect dashboard
  |
  v
(5) Redirect ke login
```
