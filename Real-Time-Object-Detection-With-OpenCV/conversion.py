from openai import OpenAI
import subprocess 
import base64
import requests
import os

# api_key_abhy = "insert key here"
# api_key = "insert key here"
def gpt(api_key):
    client = OpenAI(api_key=api_key)

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Path to your image
    image_path = "./latex_test.jpg"

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
        "content": "You are an image to latex bot, which only and only converts image to latex"},
        {
        "role": "user",
        "content": [
            # {
            # "type": "text",
            # "text": "convert this image into latex"
            # },
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

    # payload = {
    #      "model": "gpt-4-vision-preview",
    # "messages": [{"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."},
    #               {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."}]
    # }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    content = response.json()['choices'][0]['message']['content']
    print(content)
    return content

def convert(latex_content = r''''''):
        temp_latex_file = os.path.join("tmp/created.tex")
        with open(temp_latex_file,'w') as file:
            file.write(latex_content)

        output = subprocess.run(['pdflatex', '-interaction=nonstopmode','-output-directory','/tmp', temp_latex_file])
        
        pdf_path = os.path.join('tmp/created.pdf')
        return pdf_path

# latex= r'\documentclass{article} \usepackage[utf8]{inputenc} \usepackage{amsmath} \begin{document}'+ '\n\\text{Rank-Nullity Theorem:} \\\\\n\\text{Let } V \\text{ be a finite dimensional vector space over } \\mathbb{F}. \\text{ Let } T: V \\rightarrow W \\text{ be a } \\\\\n\\text{linear transformation. Then:} \\\\\n\\text{rank}(T) + \\text{nullity}(T) = \\text{dim}(V) \\\\\n\n\\text{Proof: Exercise for the reader.} \\\\\n\n\\sum_{n=0}^{\\infty} n = -\\frac{1}{12}\n' + r'\end{document}'
# convert(latex_content=latex)
# post(latex_content=repr(gpt(api_key= api_key)))