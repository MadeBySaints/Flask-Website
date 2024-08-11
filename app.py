from flask import Flask, render_template, send_from_directory, request, redirect, url_for, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'files'
METADATA_FILE = 'file_metadata.json'

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Load metadata from JSON file
def load_metadata():
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save metadata to JSON file
def save_metadata(metadata):
    with open(METADATA_FILE, 'w') as f:
        json.dump(metadata, f, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/downloads')
@app.route('/downloads/<path:folder>')
def downloads(folder=None):
    base_folder = app.config['UPLOAD_FOLDER']
    if folder:
        path = os.path.join(base_folder, folder)
    else:
        path = base_folder

    if os.path.isdir(path):
        files = []
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            files.append({
                'name': item,
                'is_folder': os.path.isdir(item_path)
            })
        return render_template('downloads.html', files=files, current_folder=folder)
    return "Folder not found", 404

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Track metadata
        metadata = load_metadata()
        metadata[file.filename] = {
            'upload_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'ip_address': request.remote_addr
        }
        save_metadata(metadata)

        return redirect(url_for('downloads'))
    return render_template('upload.html')

@app.route('/download_file/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/file_metadata/<path:filename>')
def file_metadata(filename):
    metadata = load_metadata()
    file_metadata = metadata.get(filename, {
        'upload_date': 'Unknown',
        'ip_address': 'Unknown'
    })
    return jsonify(file_metadata)

if __name__ == '__main__':
    app.run(debug=True)
