from openai import OpenAI
import subprocess 
import tempfile
import base64
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# api_key_abhy = "insert key"
api_key = os.getenv('GEMINI_API')

def gpt(api_key, image_path):
    client = OpenAI(api_key=api_key)

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {"role": "system", 
        "content": "you are an image to latex bot, which only and only converts image to latex"},
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "convert this image into latex"
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    content = response.json()['choices'][0]['message']['content']
    print(content)
    return content

def post(latex_content = r''''''):
        temp_latex_file = 'tmp/created.tex'
        with open(temp_latex_file,'w') as file:
            file.write(latex_content)

        output = subprocess.run(['pdflatex', '-interaction=nonstopmode','-output-directory','tmp', temp_latex_file])

        pdf_path = 'tmp/created.pdf'
        print('output',output)

