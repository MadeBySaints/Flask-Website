from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
import sqlite3
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Upload folder
UPLOAD_FOLDER = 'files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# User model
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# User loader
@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("SELECT id, username, password FROM users WHERE id = ?", (user_id,))
    user = cur.fetchone()
    conn.close()
    if user:
        return User(id=user[0], username=user[1], password=user[2])
    return None

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute("SELECT id, username, password FROM users WHERE username = ? AND password = ?", (username, password))
        user = cur.fetchone()
        conn.close()
        if user:
            login_user(User(id=user[0], username=user[1], password=user[2]))
            return redirect(url_for('index'))
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Home page
@app.route('/')
@login_required
def index():
    return render_template('index.html')

# Upload page
@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            save_file_metadata(filename, request.remote_addr)
            return redirect(url_for('downloads'))
    return render_template('upload.html')

# Save metadata
def save_file_metadata(filename, ip_address):
    conn = sqlite3.connect('file_metadata.db')
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS metadata (
            filename TEXT,
            upload_date TEXT,
            ip_address TEXT
        )
    """)
    cur.execute("INSERT INTO metadata (filename, upload_date, ip_address) VALUES (?, ?, ?)",
                (filename, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ip_address))
    conn.commit()
    conn.close()

# Downloads page
@app.route('/downloads')
@login_required
def downloads():
    files = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        files.append({
            'name': filename,
            'is_folder': False
        })
    return render_template('downloads.html', files=files, current_folder='')

# Serve files
@app.route('/uploads/<filename>')
@login_required
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# File metadata
@app.route('/file_metadata/<filename>')
@login_required
def file_metadata(filename):
    conn = sqlite3.connect('file_metadata.db')
    cur = conn.cursor()
    cur.execute("SELECT upload_date, ip_address FROM metadata WHERE filename = ?", (filename,))
    data = cur.fetchone()
    conn.close()
    if data:
        return jsonify({'upload_date': data[0], 'ip_address': data[1]})
    else:
        return jsonify({'upload_date': 'N/A', 'ip_address': 'N/A'})

# Delete file route
@app.route('/delete_file/<filename>', methods=['DELETE'])
@login_required
def delete_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404
    try:
        os.remove(filepath)
        # Remove metadata
        conn = sqlite3.connect('file_metadata.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM metadata WHERE filename = ?", (filename,))
        conn.commit()
        conn.close()
        return jsonify({"message": "File deleted successfully"}), 200
    except Exception as e:
        print(f"Error deleting file: {e}")
        return jsonify({"error": "Failed to delete file"}), 500

# Rename file route with extension fix
@app.route('/rename_file/<old_filename>', methods=['POST'])
@login_required
def rename_file(old_filename):
    data = request.get_json()
    new_filename = data.get('new_filename')
    if not new_filename:
        return jsonify({"error": "New filename not provided"}), 400

    old_file_path = os.path.join(app.config['UPLOAD_FOLDER'], old_filename)

    if not os.path.exists(old_file_path):
        return jsonify({"error": "Original file not found"}), 404

    # Get original file extension
    _, ext = os.path.splitext(old_filename)

    # Append extension if missing
    if not new_filename.lower().endswith(ext.lower()):
        new_filename += ext

    new_filename_secure = secure_filename(new_filename)
    new_file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename_secure)

    if os.path.exists(new_file_path):
        return jsonify({"error": "New filename already exists"}), 409

    try:
        os.rename(old_file_path, new_file_path)
        # Update metadata filename too
        conn = sqlite3.connect('file_metadata.db')
        cur = conn.cursor()
        cur.execute("UPDATE metadata SET filename = ? WHERE filename = ?", (new_filename_secure, old_filename))
        conn.commit()
        conn.close()
        return jsonify({"message": "File renamed successfully"}), 200
    except Exception as e:
        print(f"Error renaming file: {e}")
        return jsonify({"error": "Error renaming file"}), 500

if __name__ == '__main__':
    app.run(debug=True)
