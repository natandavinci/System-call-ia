
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

PASTA_BASE = "base"


def criar_db():
    #Loading docs
    documentos = loading_docs()
    #Split i chunks
    chunks = split_chunks(documentos)
    #Vetorization with process embeddning
    vetor_chunks(chunks)

def loading_docs():
    carrega = PyPDFDirectoryLoader(PASTA_BASE, glob="*.pdf")
    documentos = carrega.load()
    return documentos

def split_chunks(documentos):
    spliter_docs = RecursiveCharacterTextSplitter(
        chunk_size = 2000,
        chunk_overlap = 500,
        length_function=len,
        add_start_index=True
    )

    chunks = spliter_docs.split_documents(documentos)
    print(len(chunks))
    return chunks

def vetor_chunks(chunks):
    db = Chroma.from_documents(chunks, OpenAIEmbeddings(), persist_directory="db")
    print("banco criado")


criar_db()