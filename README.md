##Flask Website##
##Overview##
Flask Website is a web application built with Flask that provides a user-friendly interface for managing files. The application supports file browsing, uploading, downloading, and viewing metadata. It offers a clean design with image previews.

##Features##
- Home Page: Entry point of the application with navigation options.
- Downloads Page: Displays files and folders in a gallery view with download and details options.
- Upload Page: Allows users to upload files to the server.
- File Metadata: Provides file details such as upload date and IP address of the uploader.
- Folder Navigation: Browse through folders and view their contents.

##Installation##
Follow these steps to set up and run the application:

1. Clone the Repository

git clone https://github.com/your-username/flask-file-manager.git

cd flask-file-manager

2. Create a Virtual Environment

python -m venv venv

3. Activate the Virtual Environment

On Windows: venv\Scripts\activate
On macOS/Linux: source venv/bin/activate
Install Dependencies

pip install -r requirements.txt

5. Run the Application

python app.py

Open your web browser and navigate to http://127.0.0.1:5000 to access the application.

##Usage##
##Home Page##
Navigate to the home page to access the main features of the application.
##Downloads Page
- Browse through files and folders displayed in a gallery view.
- Click on folder thumbnails to open and view the contents.
- Use the "Details" button to view metadata such as upload date and IP address.
##Upload Page##
- Click the "Select files from computer" button to choose a file.
- The selected file will be displayed above the button.
- Click "Upload" to save the file to the files directory.
##File Metadata##
- The "Details" button next to each file shows a tooltip with the following information:
    - File Name
    - Upload Date (Placeholder, adjust as needed)
    - IP Address of Uploader (Placeholder, adjust as needed)

License:
This project is licensed under the MIT License. See the LICENSE file for details.
