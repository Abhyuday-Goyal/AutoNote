import google.generativeai as genai
import os, base64
from pathlib import Path
from PIL import Image
from conversion import convert
import time

def OCR(img_path = 'Real-Time-Object-Detection-With-OpenCV/frame.jpg'):
    image_path = img_path
    img = Image.open(image_path)
    print(img.format.lower())

    prompt = "convert this into latex code, include the document header and everything"

    genai.configure(api_key="add_api_key")
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(
        contents=[prompt, img]
    ).text
    # convert(response)
    print(response)
    return response

starting_time = time.time()
OCR()
print(time.time()- starting_time)