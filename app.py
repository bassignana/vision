from flask import Flask

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#This below line is required when you want to serve the file or image from static folder only.
#https://roytuts.com/upload-and-display-image-using-python-flask/
#return redirect(url_for('static', filename='uploads/' + filename), code=301)



