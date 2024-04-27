import os
from flask import Flask, flash, request
from flask_cors import CORS
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'}

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'videos'


@app.route('/videos', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return '{ "data" : "true" }'


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
