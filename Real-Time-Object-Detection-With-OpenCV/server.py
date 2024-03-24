from flask import Flask
from flask import Flask, request, send_file, make_response
from flask_cors import CORS
from hand_detection import HandDetection
from conversion import convert
from person_detection import PersonDetection

app = Flask(__name__)
CORS(app, origins='*')

@app.route('/hand_upload', methods=['POST'])
def hand_upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    if file.filename.endswith('.mp4'):
        # Do something with the uploaded mp4 file
        file.save('video.mp4')
        final_latex = HandDetection('video.mp4')
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
        file.save('video.mp4')
        final_latex = PersonDetection('video.mp4')
        pdf_path = convert(final_latex)
        response = make_response(send_file(path_or_file=pdf_path,mimetype='application/pdf', as_attachment=True))
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    else:
        return 'Invalid file format. Only mp4 files are allowed', 400
    
@app.route('/pdf_parse', methods=['POST'])
def pdf_parse_chat():
    return 'Not implemented', 501

@app.route('/pdf_chat', methods=['POST'])
def pdf_chat():
    return 'Not implemented', 501

if __name__ == '__main__':
    app.run(debug=True)