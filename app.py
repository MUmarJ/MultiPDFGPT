import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
import openai
import time

def is_api_key_valid():
    openai.api_key = st.session_state.OPENAI_API_KEY
    if openai.api_key != "":
        try:
            response = openai.Completion.create(
                engine="davinci",
                prompt="Hi",
                max_tokens=1
            )
        except:
            return False
        else:
            return True
    return False


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=800, chunk_overlap=100, length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(chunks, MODEL="OpenAI"):
    placeholder = st.empty()

    match MODEL:
        case "OpenAI":
            embeddings = OpenAIEmbeddings()
            placeholder.write("Using OpenAI Embeddings - ADA")
        case "Instructor":
            embeddings = HuggingFaceInstructEmbeddings(
                model_name="hkunlp/instructor-xl"
            )
            placeholder.write("Using HuggingFace Instruct Embeddings - Instructor XL")
        case "MiniLM":
            embeddings = HuggingFaceInstructEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
            placeholder.write("Using HuggingFace Instruct Embeddings - MiniLM")

    vectorstore = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings,
    )
    placeholder.empty()
    return vectorstore


def get_conversation_chain(vectorestore):
    llm = ChatOpenAI()
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorestore.as_retriever(),
        memory=ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        ),
    )
    return conversation_chain

def handle_question(question):
    response = st.session_state.conversation_chain({"question": question})
    st.session_state.chat_history = response["chat_history"]
    for i, message in enumerate(st.session_state.chat_history):
        if i%2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

def load_page():
    question = st.text_input("Ask your question!")
    if question:
        handle_question(question)
    st.write(user_template.replace("{{MSG}}", "Hello Bot"), unsafe_allow_html=True)
    st.write(bot_template.replace("{{MSG}}", "Hi User!"), unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Documents")
        pdf_docs = st.file_uploader("Upload PDFs", accept_multiple_files=True)

        if st.button("Submit"):
            with st.spinner("Processing..."):
                # GET PDF Text
                text = get_pdf_text(pdf_docs)
                # st.write(text)

                # GET TEXT CHUNKS
                text_chunks = get_text_chunks(text)
                # st.write(text_chunks)

                # CREATE VECTOR STORE
                vectorstore = get_vectorstore(text_chunks)

                # CREATE CONVERSATION CHAIN
                st.session_state.conversation_chain = get_conversation_chain(
                    vectorstore
                )

            st.success("Upload Success!")


def main():
    load_dotenv()
    openAIKeyValid = False
    if "conversation_chain" not in st.session_state:
        st.session_state.conversation_chain = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if "OPENAI_API_KEY" not in st.session_state:
        st.session_state.OPENAI_API_KEY = ""
        if "OPEN_API_KEY" in os.environ:
            st.session_state.OPENAI_API_KEY = os.environ.OPENAI_API_KEY
            openAIKeyValid = is_api_key_valid()

    st.set_page_config(
        page_title="Multi PDF GPT",
        page_icon="🤖",
    )
    st.write(css, unsafe_allow_html=True)
    st.header("Multi PDF GPT with Umar! 🤖")
    keyContainer = st.empty()
    successContainer = st.empty()
    if openAIKeyValid == False:
        try:
            st.session_state.OPENAI_API_KEY= keyContainer.text_input("Please enter your valid OpenAI key - This is not stored and reset on refresh!")
            with st.spinner("Validating..."):
                openAIKeyValid = is_api_key_valid()
            if not openAIKeyValid:
                st.session_state.OPENAI_API_KEY = ""
                successContainer.warning(f"Valid OpenAI API Key found? {openAIKeyValid}")
            else:
                os.environ.OPENAI_API_KEY = st.session_state.OPENAI_API_KEY
                successContainer.success("You are good to go!")
                time.sleep(1)
            # st.write(os.environ.OPENAI_API_KEY)
        except:
            raise Exception("Please set the OPENAI_API_KEY environment variable")
    if openAIKeyValid == True:
        load_page()
        successContainer.empty()
        keyContainer.empty()

if __name__ == "__main__":
    main()
