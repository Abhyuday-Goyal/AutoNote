from flask import Flask
from flask import Flask, request, send_file, make_response, jsonify
from flask_cors import CORS
from hand_detection import HandDetection
from conversion import convert
from person_detection import PersonDetection
from dotenv import load_dotenv
load_dotenv()
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
from langchain.vectorstores import Pinecone as Pine
from pinecone import Pinecone
from pinecone.config import Config
from pinecone import ServerlessSpec
from langchain.embeddings.openai import OpenAIEmbeddings
import os 
from langchain.chat_models import ChatOpenAI

from rags import create_index, read_pdf, add_embeds, convert_pdf_to_text, split_into_sentence_chunks, execute_query

app = Flask(__name__)
CORS(app, origins='*')

#rag initialization
pc_api_key = os.getenv("PINECONE_KEY")

# configure client
pc = Pinecone(api_key=pc_api_key)

spec = ServerlessSpec(
    cloud="aws", region="us-west-2"
)

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or "YOUR_API_KEY"
OPENAI_KEY = os.getenv("OPENAI_KEY")
chat = ChatOpenAI(
    openai_api_key= OPENAI_KEY,
    model='gpt-3.5-turbo'
)

#the embeddings model for vector embeddings
embed_model = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key = OPENAI_KEY)

#messages log for the AI chat
messages = [
    SystemMessage(content="You are a helpful assistant that answers questions and asks questions if prompted using the contexts given."),
    HumanMessage(content="Hi AI, how are you today?"),
    AIMessage(content="I'm great thank you. How can I help you?"),
    # HumanMessage(content="I'd like to understand string theory.")
]

max_chunk_length = 500  # Choose the maximum length for each chunk
index_name = 'pdfsearch'

# pc.delete_index(index_name)

# create_index(index_name, spec, pc)

index = pc.Index(index_name)

text_field = "context"  # the metadata field that contains our text

# initialize the vector store object
vectorstore = Pine(
    index, embed_model.embed_query, text_field
)
# convert_pdf_to_text('Real-Time-Object-Detection-With-OpenCV/COMM107-1-90.pdf')
# data = read_pdf(path='Real-Time-Object-Detection-With-OpenCV/COMM107-1-90.txt')
# print('data', data[0:100])
# sentence_chunks = split_into_sentence_chunks(data, max_chunk_length)
# add_embeds(sentence_chunks, embed_model, index)



@app.route('/hand_upload', methods=['POST'])
def hand_upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    if file.filename.endswith('.mp4'):
        # Do something with the uploaded mp4 file
        upload_path = "C:/Nishkal/HooHacks 2024/AutoNote/videos/video.mp4"
        # upload_path = 'videos/video.mp4'
        file.save(upload_path)
        final_latex = HandDetection(upload_path)
        pdf_path = convert(final_latex)
        convert_pdf_to_text('Real-Time-Object-Detection-With-OpenCV/pdfs/uploaded.pdf')
        data = read_pdf(path='Real-Time-Object-Detection-With-OpenCV/pdfs/uploaded.txt')
        sentence_chunks = split_into_sentence_chunks(data, max_chunk_length)
        add_embeds(sentence_chunks, embed_model, index)
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
        upload_path = "C:/Nishkal/HooHacks 2024/AutoNote/videos/video.mp4"
        file.save(upload_path)
        final_latex = PersonDetection(upload_path)
        pdf_path = convert(final_latex)
        convert_pdf_to_text('Real-Time-Object-Detection-With-OpenCV/pdfs/uploaded.pdf')
        data = read_pdf(path='Real-Time-Object-Detection-With-OpenCV/pdfs/uploaded.txt')
        sentence_chunks = split_into_sentence_chunks(data, max_chunk_length)
        add_embeds(sentence_chunks, embed_model, index)
        response = make_response(send_file(path_or_file=pdf_path,mimetype='application/pdf', as_attachment=True))
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    else:
        return 'Invalid file format. Only mp4 files are allowed', 400
    
@app.route('/pdf_parse', methods=['POST'])
def pdf_parse_chat():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    upload_path = './pdfs/uploaded.pdf'
    file.save(upload_path)
    convert_pdf_to_text('./pdfs/uploaded.pdf')
    data = read_pdf(path='./pdfs/uploaded.txt')
    sentence_chunks = split_into_sentence_chunks(data, max_chunk_length)
    add_embeds(sentence_chunks, embed_model, index)
    return 'Embeds Added', 200

@app.route('/pdf_chat', methods=['POST'])
def pdf_chat():
    data = request.json  # Access JSON data from request body
    query = data.get('query')
    print(query)
    output = execute_query(query, messages, chat, vectorstore)
    print(output)
    return jsonify(output=output)

if __name__ == '__main__':
    app.run(debug=True)