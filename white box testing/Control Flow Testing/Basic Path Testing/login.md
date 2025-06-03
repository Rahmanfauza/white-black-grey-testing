## Fungsi login()

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':                      
        username = request.form['username']            
        password = request.form['password']            

        conn = get_db()                                
        user = conn.execute(
            'SELECT * FROM users WHERE username = ?', 
            (username,)
        ).fetchone()                                   
        conn.close()                                   

        if user and check_password_hash(user['password'], password):  
            session['user_id'] = user['id']            
            session['username'] = user['username']     
            flash('Login berhasil!', 'success')        
            return redirect(url_for('dashboard'))      
        else:
            flash('Username atau password salah', 'danger')  

    return render_template('login.html')               
```
### Flow Diagram
```
(1) ────> [request.method == 'POST']
  |                    |
  |                    v
  |                (2) Ambil user/pass
  |                    |
  |                (3) Query DB
  |                    |
  |              [user & pw cocok?]
  |                    |         \
  |                    v          v
  |               (4) Redirect   (5) Flash error
  |                    |           |
  |                    v           |
  |               return dashboard |
  |                                |
  v                                v
(6) <------------------------------|
|
v
(7) Render login.html
```
