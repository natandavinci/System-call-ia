
from langchain_community.document_loaders import PyPDFDirectoryLoader



PASTA_BASE = "base"


def criar_db():
    #Loading docs
    documentos = loading_docs()
    print(documentos)
    #Split i chunks

    #Vetorization with process embeddning

def loading_docs():
    carrega = PyPDFDirectoryLoader(PASTA_BASE, glob="*.pdf")
    documentos = carrega.load()
    return documentos

def split_chunks(documentos):

    

    return chunks


criar_db()