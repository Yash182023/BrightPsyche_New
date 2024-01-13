# # # import streamlit as st
# # # from dotenv import load_dotenv
# # # from PyPDF2 import PdfReader
# # # from langchain.text_splitter import CharacterTextSplitter
# # # from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
# # # from langchain.vectorstores import FAISS
# # # from langchain.chat_models import ChatOpenAI
# # # from langchain.memory import ConversationBufferMemory
# # # from langchain.chains import ConversationalRetrievalChain
# # # from htmlTemplates import css, bot_template, user_template
# # # from langchain.llms import HuggingFaceHub

# # # def get_pdf_text(pdf_docs):
# # #     text = ""
# # #     for pdf in pdf_docs:
# # #         pdf_reader = PdfReader(pdf)
# # #         for page in pdf_reader.pages:
# # #             text += page.extract_text()
# # #     return text


# # # def get_text_chunks(text):
# # #     text_splitter = CharacterTextSplitter(
# # #         separator="\n",
# # #         chunk_size=1000,
# # #         chunk_overlap=200,
# # #         length_function=len
# # #     )
# # #     chunks = text_splitter.split_text(text)
# # #     return chunks


# # # def get_vectorstore(text_chunks):
# # #     embeddings = OpenAIEmbeddings()
# # #     # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
# # #     vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
# # #     return vectorstore


# # # def get_conversation_chain(vectorstore):
# # #     llm = ChatOpenAI()
# # #     # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

# # #     memory = ConversationBufferMemory(
# # #         memory_key='chat_history', return_messages=True)
# # #     conversation_chain = ConversationalRetrievalChain.from_llm(
# # #         llm=llm,
# # #         retriever=vectorstore.as_retriever(),
# # #         memory=memory
# # #     )
# # #     return conversation_chain


# # # def handle_userinput(user_question):
# # #     response = st.session_state.conversation({'question': user_question})
# # #     st.session_state.chat_history = response['chat_history']

# # #     for i, message in enumerate(st.session_state.chat_history):
# # #         if i % 2 == 0:
# # #             st.write(user_template.replace(
# # #                 "{{MSG}}", message.content), unsafe_allow_html=True)
# # #         else:
# # #             st.write(bot_template.replace(
# # #                 "{{MSG}}", message.content), unsafe_allow_html=True)


# # # def main():
# # #     load_dotenv()
# # #     st.set_page_config(page_title="Mental Health Support",
# # #                        page_icon=":books:")
# # #     st.write(css, unsafe_allow_html=True)

# # #     if "conversation" not in st.session_state:
# # #         st.session_state.conversation = None
# # #     if "chat_history" not in st.session_state:
# # #         st.session_state.chat_history = None

# # #     st.header("Mental Health Support :brain:")
# # #     user_question = st.text_input("Ask a question about your documents:")
# # #     if user_question:
# # #         handle_userinput(user_question)

# # #     with st.sidebar:
# # #         st.subheader("Your documents")
# # #         pdf_docs = st.file_uploader(
# # #             "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
# # #         if st.button("Process"):
# # #             with st.spinner("Processing"):
# # #                 # get pdf text
# # #                 raw_text = get_pdf_text(pdf_docs)

# # #                 # get the text chunks
# # #                 text_chunks = get_text_chunks(raw_text)

# # #                 # create vector store
# # #                 vectorstore = get_vectorstore(text_chunks)

# # #                 # create conversation chain
# # #                 st.session_state.conversation = get_conversation_chain(
# # #                     vectorstore)
                


# # # if __name__ == '__main__':
# # #     main()
# # # import streamlit as st
# # # from dotenv import load_dotenv
# # # from PyPDF2 import PdfReader
# # # from langchain.text_splitter import CharacterTextSplitter
# # # from langchain.embeddings import OpenAIEmbeddings
# # # # from langchain.embeddings import HuggingFaceInstructEmbeddings
# # # from langchain.vectorstores import FAISS
# # # from langchain.chat_models import ChatOpenAI
# # # from langchain.memory import ConversationBufferMemory
# # # from langchain.chains import ConversationalRetrievalChain
# # # from htmlTemplates import css, bot_template, user_template
# # # # from langchain.llms import HuggingFaceHub
# # # # from streamlit_option_menu import option_menu
# # # import pyttsx3

# # # def get_pdf_text(pdf_paths):
# # #     text = ""
# # #     for pdf_path in pdf_paths:
# # #         with open(pdf_path, 'rb') as pdf_file:
# # #             pdf_reader = PdfReader(pdf_file)
# # #             for page in pdf_reader.pages:
# # #                 text += page.extract_text()
# # #     return text

# # # def get_text_chunks(text):
# # #     text_splitter = CharacterTextSplitter(
# # #         separator="\n",
# # #         chunk_size=1000,
# # #         chunk_overlap=200,
# # #         length_function=len
# # #     )
# # #     chunks = text_splitter.split_text(text)
# # #     return chunks

# # # def get_vectorstore(text_chunks):
# # #     embeddings = OpenAIEmbeddings()
# # #     #embeddings = HuggingFaceInstructEmbeddings(model_name="nomic-ai/gpt4all-j")
# # #     vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
# # #     return vectorstore

# # # def get_conversation_chain(vectorstore):
# # #     llm = ChatOpenAI()
# # #     #llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
# # #     memory = ConversationBufferMemory(
# # #         memory_key='chat_history', return_messages=True)
# # #     conversation_chain = ConversationalRetrievalChain.from_llm(
# # #         llm=llm,
# # #         retriever=vectorstore.as_retriever(),
# # #         memory=memory
# # #     )
# # #     return conversation_chain


    
# # # def handle_userinput(user_question):
# # #     response = st.session_state.conversation({'question': user_question})
# # #     st.session_state.chat_history = response['chat_history']

    
# # #     for i, message in enumerate(st.session_state.chat_history):
# # #         if i % 2 == 0:
# # #             st.write(user_template.replace(
# # #                 "{{MSG}}", message.content), unsafe_allow_html=True)
# # #         else:
# # #             st.write(bot_template.replace(
# # #                 "{{MSG}}", message.content), unsafe_allow_html=True)
            
# # #     engine = pyttsx3.init()
# # #     engine.say(response['answer'])
# # #     engine.runAndWait()

# # # def main():
# # #     load_dotenv()
# # #     st.set_page_config(page_title="Mental Health Support", page_icon=":brain:")
# # #     st.write(css, unsafe_allow_html=True)
    

# # #     if "conversation" not in st.session_state:
# # #         st.session_state.conversation = None
# # #     if "chat_history" not in st.session_state:
# # #         st.session_state.chat_history = None

# # #     st.header("Mental Health Support :brain:")
# # #     pdf_paths = [
# # #         'C:/Users/sharm/Downloads/ask-multiple-pdfs-main/ask-multiple-pdfs-main/Chat_data.pdf',
# # #         'C:/Users/sharm/Downloads/ask-multiple-pdfs-main/ask-multiple-pdfs-main/class 10 history ch 3.pdf'
# # #     ]
    
    
# # #         # get pdf text
# # #     raw_text = get_pdf_text(pdf_paths)

# # #         # get the text chunks
# # #     text_chunks = get_text_chunks(raw_text)

# # #         # create vector store
# # #     vectorstore = get_vectorstore(text_chunks)

# # #         # create conversation chain
# # #     st.session_state.conversation = get_conversation_chain(vectorstore)

# # #     user_question = st.text_input("Your therapist is there for you!:")
# # #     if user_question and st.session_state.conversation:
# # #         handle_userinput(user_question)

# # # if __name__ == '__main__':
# # #     main()
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings,HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFaceHub
from htmlTemplates import css, bot_template, user_template
#from InstructorEmbedding import INSTRUCTOR
import tempfile
import ttsmms
import soundfile as sf
from streamlit.components.v1 import html

def get_pdf_text(pdf_paths):
    text = ""
    for pdf_path in pdf_paths:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            for page in pdf_reader.pages:
                text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    #embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-base")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']
    
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

    audio_path = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
    tts = ttsmms.TTS("data/eng")  # Update with the correct path
    wav = tts.synthesis(response['answer'])
    sf.write(audio_path, wav["x"], wav["sampling_rate"])
    
    st.audio(audio_path, format="audio/wav", start_time=0, sample_rate=wav["sampling_rate"])

def main():
    load_dotenv()
    st.set_page_config(page_title="Mental Health Support", page_icon=":brain:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Mental Health Support :brain:")
    pdf_paths = [
        'C:/Users/sharm/Downloads/ask-multiple-pdfs-main/ask-multiple-pdfs-main/Chat_data.pdf',
        'C:/Users/sharm/Downloads/ask-multiple-pdfs-main/ask-multiple-pdfs-main/class 10 history ch 3.pdf'
    ]
    
    raw_text = get_pdf_text(pdf_paths)
    text_chunks = get_text_chunks(raw_text)
    vectorstore = get_vectorstore(text_chunks)
    st.session_state.conversation = get_conversation_chain(vectorstore)

    user_question = st.text_input("Your therapist is there for you!:")
    if user_question and st.session_state.conversation:
        handle_userinput(user_question)

if __name__ == '__main__':
    main()
# my_js = """
# alert("Please don't forget to enter you daily details!!!");
# """

# # Wrapt the javascript as html code
# my_html = f"<script>{my_js}</script>"

# # Execute your app

# html(my_html)