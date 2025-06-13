## Flask Website File Manager
## Overview
This is a file management web application built using Flask. It allows users to securely upload, download, and view files with a clean and modern user interface. The system supports user login and includes features such as file metadata display, image previews, and file management tools.

## Login System
Secure user authentication with session handling.
Note: Only login functionality is implemented. Logout is not yet included.

## Home Page
A visually improved landing page with clean navigation links to Upload and Downloads sections.

##  Downloads Page
Displays files and folders in a card-style layout with:

Click-to-download functionality

"Details" button to view file metadata

New: Rename and Delete buttons for file management

## Upload Page
Clean and simple file selection and upload UI

Preview selected filename before upload

Uploads are automatically added to the file system directory

## File Metadata
View important details like:

File name

Upload date

IP address of the uploader

## What's New / Enhancements
Compared to the previous version of the Flask Website File Manager, the following improvements were added:

Delete Functionality – Easily remove uploaded files

Rename Functionality – Rename files directly from the downloads page

Enhanced UI/UX – Improved styling across all pages for a modern and intuitive look

Navigation Buttons – Consistent header navigation across all pages

Login Page Added – Basic login system to access the dashboard (logout to be added)

## Installation
Clone the Repository

git clone https://github.com/MadeBySaints/Flask-Website.git
cd Flask-Website
Create a Virtual Environment

python -m venv venv
Activate the Virtual Environment

On Windows:

venv\Scripts\activate
On macOS/Linux:

source venv/bin/activate
Install the Dependencies

pip install -r requirements.txt
Run the Application

python app.py
Then open your browser and go to:
http://localhost:5000
Or access from another device via your IP address with port 5000.

## Usage
Login
Go to /login, enter credentials, and access your dashboard.

## Note: The username is "admin" and the password is "adminpass".

Home
Navigate to other pages like Upload, and Download.

Upload Page
Choose and upload files. The interface shows the selected file name before upload.

Downloads Page
View all uploaded files in a gallery format. Download files or check their metadata.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

