## Fungsi Logout

```python
@app.route('/logout')
def logout():
    session.clear()
    flash('Logout berhasil.', 'success')
    return redirect(url_for('login'))
```
### Flow Diagram
```
(1) Start
 |
 v
(2) session.clear()
 |
 v
(3) flash('Logout berhasil')
 |
 v
(4) redirect ke login
 |
 v
(5) End
```
