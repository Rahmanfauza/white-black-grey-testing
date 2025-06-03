## Fungsi Dashboard

```python
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        conn = get_db()
        tasks = conn.execute(
            'SELECT * FROM tasks WHERE user_id = ?', 
            (session['user_id'],)
        ).fetchall()
        conn.close()
        return render_template('dashboard.html', tasks=tasks)
    else:
        return redirect(url_for('login'))
```
Flow Diagram
```
(1) Start
 |
 v
[Apakah 'username' ada di session?]
 |                     \
Yes                     No
 |                       \
 v                        v
(2) Koneksi ke database   (5) Redirect ke login
 |
 v
(3) Ambil semua tasks user dari DB
 |
 v
(4) Tampilkan dashboard.html dengan tasks
 |
 v
End
