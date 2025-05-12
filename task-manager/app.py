from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from sqlite3 import Error
import os
from datetime import datetime
import pytz  # Make sure to install pytz: pip install pytz

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Initialize database
def init_db():
    if not os.path.exists('database.db'):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Create users table
        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        ''')

        # Create tasks table with created_at that will store timezone-aware datetime
        cursor.execute('''
            CREATE TABLE tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'pending',
                user_id INTEGER NOT NULL,
                created_at TEXT NOT NULL,  # Changed to TEXT to store ISO format
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        conn.commit()
        conn.close()

init_db()

# Database helper function
def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Middleware to check login
@app.before_request
def require_login():
    allowed_routes = ['login', 'register', 'static']
    if request.endpoint not in allowed_routes and 'user_id' not in session:
        return redirect(url_for('login'))

# Helper function to get Jakarta time
def get_jakarta_time():
    jakarta_tz = pytz.timezone('Asia/Jakarta')
    return datetime.now(jakarta_tz)

# Format datetime for display
# Format datetime for display - simplified version
def format_datetime(dt_str, format='%d-%m-%Y %H:%M'):  # Format Indonesia (hari-bulan-tahun jam:menit)
    if dt_str is None:
        return ""
    try:
        dt = datetime.fromisoformat(dt_str)
        return dt.strftime(format)
    except ValueError:
        return dt_str
app.jinja_env.filters['datetime'] = format_datetime

@app.route('/')
def home():
    return redirect(url_for('dashboard'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db()
        user = conn.execute(
            'SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Login berhasil!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Username atau password salah', 'danger')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        conn = get_db()
        try:
            conn.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                         (username, email, password))
            conn.commit()
            conn.close()
            flash('Registrasi berhasil! Silakan login', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            conn.close()
            flash('Username atau email sudah digunakan', 'danger')

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    conn = get_db()
    tasks = conn.execute('''
        SELECT * FROM tasks 
        WHERE user_id = ?
        ORDER BY datetime(created_at) DESC
    ''', (session['user_id'],)).fetchall()
    conn.close()
    return render_template('dashboard.html', tasks=tasks)

@app.route('/tasks/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form.get('description', '')
    
    # Get current Jakarta time
    jakarta_time = get_jakarta_time()
    created_at = jakarta_time.isoformat()

    conn = get_db()
    conn.execute('''
        INSERT INTO tasks (title, description, user_id, created_at) 
        VALUES (?, ?, ?, ?)
    ''', (title, description, session['user_id'], created_at))
    conn.commit()
    conn.close()

    flash('Tugas berhasil ditambahkan', 'success')
    return redirect(url_for('dashboard'))

@app.route('/settings')
def settings():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # You can add any user-specific settings data here
    user_id = session['user_id']
    username = session['username']
    
    return render_template('settings.html', username=username, user_id=user_id)

@app.route('/tasks')
def all_tasks():
    conn = get_db()
    tasks = conn.execute('''
        SELECT * FROM tasks 
        WHERE user_id = ?
        ORDER BY datetime(created_at) DESC
    ''', (session['user_id'],)).fetchall()
    conn.close()
    return render_template('all_tasks.html', tasks=tasks)

@app.route('/tasks/<int:task_id>')
def task_detail(task_id):
    conn = get_db()
    task = conn.execute('SELECT * FROM tasks WHERE id = ? AND user_id = ?',
                        (task_id, session['user_id'])).fetchone()
    conn.close()

    if task:
        return render_template('task_detail.html', task=task)
    else:
        flash('Tugas tidak ditemukan', 'danger')
        return redirect(url_for('dashboard'))

@app.route('/tasks/<int:task_id>/update', methods=['POST'])
def update_task(task_id):
    status = request.form['status']

    conn = get_db()
    conn.execute('UPDATE tasks SET status = ? WHERE id = ? AND user_id = ?',
                 (status, task_id, session['user_id']))
    conn.commit()
    conn.close()

    flash('Status tugas diperbarui', 'success')
    return redirect(url_for('task_detail', task_id=task_id))

@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    conn = get_db()
    conn.execute('DELETE FROM tasks WHERE id = ? AND user_id = ?',
                 (task_id, session['user_id']))
    conn.commit()
    conn.close()

    flash('Tugas dihapus', 'success')
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    flash('Anda telah logout', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)