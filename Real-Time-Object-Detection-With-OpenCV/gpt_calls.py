from openai import OpenAI
import subprocess 
import tempfile
import base64
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key_abhy = "insert key"
api_key = os.getenv('OPENAI_KEY')

def gpt(latex):
    load_dotenv()
    api_key = os.getenv('OPENAI_KEY')

    client = OpenAI(api_key=api_key)

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Getting the base64 string

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "system", "content": "you only return latex without the header and footer of the code and only return all the code after begin and before end document. DO NOT INCLUDE THOSE TWO."},
        {"role": "user", "content": latex}],
    "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    content = response.json()['choices'][0]['message']['content']
    print("GPT CONTENT: " + content)
    return content

def post(latex_content = r''''''):
        temp_latex_file = 'tmp/created.tex'
        with open(temp_latex_file,'w') as file:
            file.write(latex_content)

        output = subprocess.run(['pdflatex', '-interaction=nonstopmode','-output-directory','tmp', temp_latex_file])

        pdf_path = 'tmp/created.pdf'
        print('output',output)


if __name__ == "__main__":
    # gpt(api_key)
    gpt(r'''\documentclass[12pt]{article}
\usepackage{amsmath}
\begin{document}
\section{Lecture 2}
\subsection{Integration}
$$\int e^x dx = e^x + C$$
\end{document}''')
    # convert(latex_content = r'''''')