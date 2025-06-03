## Fungsi register()

```python
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        ...
        if existing_user:
            flash('Username/email sudah digunakan')
        else:
            cursor.execute(...)
            conn.commit()
            return redirect(url_for('login'))
    return render_template('register.html')
```

### Flow Diagram
```
(1) ───> [request.method == 'POST']
  |                    |
  |                    v
  |             (2) Ambil input
  |                    |
  |           [username/email tersedia?]
  |              |             \
  |              v              v
  |       (3) Flash error   (4) Simpan DB
  |                            |
  |                      (5) Redirect ke login
  |                                   |
  |<---------------------------------/
  |
  v
(6) Render register.html
```
