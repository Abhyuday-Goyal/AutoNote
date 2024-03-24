import google.generativeai as genai
import os, base64
from pathlib import Path
from PIL import Image
from conversion import convert
import time
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_KEY")

def OCR(api_key = "", img_path = 'frame.jpg'):
    image_path = img_path
    img = Image.open(image_path)

    prompt = "convert this into latex code, do not include the document header and ending. Focus on getting the text and equations right."

    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(
        contents=[prompt, img]
    ).text
    # convert(response)
    print(response)
    return response