import os
from langchain.chat_models import ChatOpenAI
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
from chunk_converter import split_into_sentence_chunks
import PyPDF2

def create_index(index_name, spec, pc):
    if index_name not in pc.list_indexes():
    # if does not exist, create index
        pc.create_index(
        index_name,
        dimension=1536,  # dimensionality of ada 002
        metric='dotproduct',
        spec=spec
        )

def read_pdf(path = 'cs103x-notes.text'):
    with open(path, "r") as f: 
        data = f.read()
    return data

def add_embeds(sentence_chunks, embed_model, index):
    from tqdm.auto import tqdm
    from uuid import uuid4
    import time

    batch_size = 250
    for i in tqdm(range(0, len(sentence_chunks), batch_size)):
        
        i_min = min(i+batch_size, len(sentence_chunks))
        batch = sentence_chunks[i: i_min]
        meta_data = [{"title" : 'notes', 
                "context": row}
                    for row in batch]
        ids = [str(uuid4()) for _ in range(len(batch))]
        # Encode the text to obtain its vector representation
        embeds = embed_model.embed_documents(batch)
        
        # Upsert the vector and text into the Pinecone index
        index.upsert(vectors=zip(ids, embeds, meta_data))
        print('sleepin')
        time.sleep(4)

def augment_prompt(query: str, vectorstore: Pinecone):
    # get top 3 results from knowledge base
    results = vectorstore.similarity_search(query, k=5)
    # get the text from the results
    source_knowledge = "\n".join([x.page_content for x in results])
    # feed into an augmented prompt
    augmented_prompt = f"""Using the contexts below, answer the query.

    Contexts:
    {source_knowledge}

    Query: {query}"""
    return augmented_prompt


def execute_query(query, messages, chat, vectorstore: Pinecone):
    prompt = HumanMessage(
    content=augment_prompt(query, vectorstore=vectorstore))
    # add to messages
    messages.append(prompt)
    res = chat(messages)
    return res.content



def convert_pdf_to_text(pdf_path):
    """Converts a PDF file to a text file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        None
    """

    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        text = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            text += page_text

    base_filename = pdf_path.split(".")[0]  # Extract filename without extension
    text_filename = f"{base_filename}.txt"

    with open(text_filename, "w", encoding="utf-8") as text_file:
        text_file.write(text)

def main():
# initialize connection to pinecone (get API key at app.pinecone.io)
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

    max_chunk_length = 150  # Choose the maximum length for each chunk
    index_name = 'pdfsearch'

    # pc.delete_index(index_name)
    
    # create_index(index_name, spec, pc)

    index = pc.Index(index_name)

    text_field = "context"  # the metadata field that contains our text

    # initialize the vector store object

   
    # convert_pdf_to_text('Real-Time-Object-Detection-With-OpenCV/COMM107-1-90.pdf')
    # data = read_pdf(path='Real-Time-Object-Detection-With-OpenCV/COMM107-1-90.txt')
    # print('data', data[0:100])
    # sentence_chunks = split_into_sentence_chunks(data, max_chunk_length)
    # add_embeds(sentence_chunks, embed_model, index)

    vectorstore = Pine(
        index, embed_model.embed_query, text_field
    )
    query = "what is the linear model in oral communication"

    output = execute_query(query, messages, chat, vectorstore)
    print(output)
    
    #Get the PDF path from the user
#     pdf_path = "Real-Time-Object-Detection-With-OpenCV/cs103x-notes.pdf"

# #Convert the PDF to text
#     convert_pdf_to_text(pdf_path)

#     print("PDF has been converted to text successfully!")

if __name__ == "__main__":
    main()  







