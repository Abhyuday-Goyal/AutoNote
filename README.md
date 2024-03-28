# AutoNote


As college students we often face the problem of not having well-structured and clear notes. Along with this, it is difficult to get answers to specific queries as it would involve a student flipping through endless pages of notes.

# What it does
AutoNote streamlines note-taking by transforming handwritten or whiteboard notes from uploaded videos into professional LaTeX-style PDFs. It also features secure storage for users' PDF documents and delivers tailored responses to their inquiries, enhancing productivity and organization.

# How we built it
Utilizing React for our front end, we created a user-friendly interface facilitating seamless PDF uploads, video-based OCR (Optical Character Recognition) execution, and effortless searches. For the backend, Flask was employed to integrate Gemini Pro Vision, enhancing our platform with robust image detection capabilities. This enabled us to detect text within frames and convert complex text into Latex documentation, further processing into PDFs using pdflatex. Vector databases, powered by Pinecone, efficiently stored PDF content. Leveraging RAG(Retrieval-Augmented Generation) with embedded queries through LangChain, we ensured tailored results for users. Finally, GPT-3.5 Turbo augmented search functionality, delivering strictly relevant results and mitigating AI hallucinations and outdated information.

# Challenges we ran into
For the front end, it was challenging to transition from one page to another with the help of animations. For the backend, it was challenging to deploy RAGs which needed to be connected to the vector database. Along with this getting image recognition to work at the right time to ensure that the OCR model can capture all the data was a major challenge.

# Accomplishments that we're proud of
Effectively using RAGs which we connected to our vector database to generate queries and finally passing those queries into GPT 3.5 Turbo to provide tailored results to users

# What we learned
We learned how to effectively use RAGs and vector databases along with Flask to connect the frontend to the backend

# What's next for AutoNote
To enhance model accuracies and efficiency for a smoother experience, our immediate action items for AutoNote include improving model accuracies and efficiency, as well as implementing additional functionalities such as creating custom chatbots based on specific PDFs and enhancing the functionality of RAGs. Additionally, we plan to implement automatic detection of whiteboards and handwritten notes using machine learning.

# Member Info:
Name: Abhyuday Goyal | School: The University of Maryland, College Park | Email: abhyuday2106@gmail.com Name: Pranav Chandar Sridar | School: The University of Maryland, College Park | Email: pranav.umd22@gmail.com Name: Swastik Agarwal | School: The University of Maryland, College Park | Email: swastikagrawal3@gmail.com Name: Nishkal Hundia | School: The University of Maryland, College Park | Email: nishkalnhundia@gmail.com
