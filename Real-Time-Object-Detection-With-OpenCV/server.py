from flask import Flask
from flask import Flask, request

from hand_detection import 

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/whiteboard_upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    if file.filename.endswith('.mp4'):
        # Do something with the uploaded mp4 file
        file.save('/tmp/video.mp4')
        
    else:
        return 'Invalid file format. Only mp4 files are allowed', 400

    return 'File uploaded successfully'

@app.route('/hand_upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    # Do something with the uploaded file

    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run()