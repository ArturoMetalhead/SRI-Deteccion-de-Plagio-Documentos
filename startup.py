from src.code.lexic_preprocessing import *
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from src.code.utils import *
from src.code.lexic_similarity import *

def detect_plagiarism():

    # Lee input de usuario
    doc1 = input("Ingrese el nombre del primer documento: ")
    doc2 = input("Ingrese el nombre del segundo documento: ")

    # Leer documentos de la carpeta docs
    documents = read_documents(doc1,doc2)

    # Separar por oraciones los documentos
    sentences1 = split_sentences(documents[0])
    sentences2 = split_sentences(documents[1])

    # Preprocesar documentos
    vect_text1,vect_text2 = preprocess(sentences1,sentences2)

    # Calcular similitud entre los documentos
    lexic_sim=lexic_similarity(vect_text1,vect_text2)

    # Retornar similitud
    return lexic_sim


#document1 = "the dog eats a fish. I like big butts and i cannot lie."
#document2 = "the cat eats a fish. Its only for the weak. No one can deny."
similarity = detect_plagiarism()
print(similarity)