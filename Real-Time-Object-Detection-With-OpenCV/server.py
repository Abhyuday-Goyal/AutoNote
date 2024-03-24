from flask import Flask
from flask import Flask, request, send_file

from hand_detection import HandDetection
from conversion import convert
from person_detection import PersonDetection

app = Flask(__name__)

@app.route('/hand_upload', methods=['POST'])
def hand_upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    if file.filename.endswith('.mp4'):
        # Do something with the uploaded mp4 file
        file.save('/tmp/video.mp4')
        final_latex = HandDetection('/tmp/video.mp4')
        pdf_path = convert(final_latex)
        return send_file(pdf_path, mimetype='application/pdf')
    else:
        return 'Invalid file format. Only mp4 files are allowed', 400

@app.route('/whiteboard_upload', methods=['POST'])
def whiteboard_upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    if file.filename.endswith('.mp4'):
        # Do something with the uploaded mp4 file
        file.save('/tmp/video.mp4')
        final_latex = PersonDetection('/tmp/video.mp4')
        pdf_path = convert(final_latex)
        return send_file(pdf_path, mimetype='application/pdf')
    else:
        return 'Invalid file format. Only mp4 files are allowed', 400
    
@app.route('/pdf_parse', methods=['POST'])
def pdf_parse_chat():
    return 'Not implemented', 501

@app.route('/pdf_chat', methods=['POST'])
def pdf_chat():
    return 'Not implemented', 501

if __name__ == '__main__':
    app.run()