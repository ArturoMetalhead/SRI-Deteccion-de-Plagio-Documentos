import os
import re

def split_sentences(text):
    """
    Split a text into sentences using punctuation as a delimiter
    """

    text = text.replace("\n", " ")

    # Detectar oraciones usando puntuación
    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z]\.)(?<=\.|\?|!|;)\s", text)

    # Eliminar oraciones vacías
    sentences = [sentence for sentence in sentences if sentence.strip()]
    return sentences

def read_documents(doc1,doc2):
    """
    Read documents from the docs folder
    """

    # Leer documentos de la carpeta docs
    with open("src/docs/"+doc1, "r") as file:
        document1 = file.read()
    with open("src/docs/"+doc2, "r") as file:
        document2 = file.read()
    return [document1, document2]

def get_documents():
    """
    Get documents from the docs folder
    """

    path = "src/docs"
    docs_names = os.listdir(path)

    print("Escoja los documentos que desea comparar")
    for i in range(0,len(docs_names)):
        print(f"{i+1}.{docs_names[i]}")

    doc1_index = int(input("Primer documento:"))
    doc2_index = int(input("Segundo documento:"))

    doc1, doc2 = read_documents(docs_names[doc1_index-1], docs_names[doc2_index-1])
    return [doc1, doc2]