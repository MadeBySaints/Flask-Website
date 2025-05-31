## Flask Website File Manager
## Overview
This is a file management web application built using Flask. It allows users to securely upload, download, and view files with a clean and modern user interface. The system supports user login, logout, and includes features such as file metadata display and image previews for a smoother user experience.

## Features
Login and Logout System
Secure user authentication with role-based session handling and a logout button on every main page.

## Home Page
A beautifully designed landing page with navigation links to Upload, Downloads, and Profile.

## Downloads Page
Displays files and folders in a gallery-style view with:

Click-to-download functionality

"Details" button to view file metadata

## Upload Page
Simple file selection and upload interface.

Shows selected filename before uploading

Automatically adds uploaded file to the system's file directory

## File Metadata
View important details like:

File name

Upload date

IP address of the uploader

Profile Page

Displays user information such as name, email, and contact number

Can be expanded for editing or adding profile pictures

Responsive Design

Works well on desktop and mobile

Styled using HTML and CSS for a clean user experience

## Installation
Clone the Repository

bash
Copy
Edit
git clone https://github.com/MadeBySaints/Flask-Website.git
cd Flask-Website
Create a Virtual Environment

bash
Copy
Edit
python -m venv venv
Activate the Virtual Environment

On Windows:

bash
Copy
Edit
venv\Scripts\activate
On macOS/Linux:

bash
Copy
Edit
source venv/bin/activate
Install the Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Application

bash
Copy
Edit
python app.py
Then open your browser and go to:
http://localhost:5000
Or access from another device via your IP address with port 5000.

## Usage
Login
Go to /login, enter credentials, and access your dashboard.

Home
Navigate to other pages like Upload, Download, Profile, or click Logout.

Upload Page
Choose and upload files. The interface shows the selected file name before upload.

Downloads Page
View all uploaded files in a gallery format. Download files or check their metadata.

Profile Page
See your personal information (optional editing feature can be added later).

Logout
Click the Logout link in the navigation to safely end your session.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

