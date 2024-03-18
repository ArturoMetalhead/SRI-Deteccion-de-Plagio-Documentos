from src.code.lexic_preprocessing import *
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from src.code.utils import *
from src.code.similarity import *
from src.code.semantic_preprocessing_functions import *

def detect_plagiarism():

    documents=get_documents()

    # Separar por oraciones los documentos
    sentences1 = split_sentences(documents[0])
    sentences2 = split_sentences(documents[1])

    # Preprocesar documentos para similitud lexica
    lex1,lex2 = preprocess(sentences1,sentences2)

    #Preprocesar documentos para similitud semantica
    semantic_list1, semantic_list2 = vectorize_sentences(sentences1), vectorize_sentences(sentences2)

    # Calcular similitud lexica entre los documentos
    lexic_sim=similarity(lex1,lex2)

    sem_sim = similarity(semantic_list1, semantic_list2)

    total_sim = total_similarity(lexic_sim, sem_sim)
    return lexic_sim, sem_sim, total_sim

    
def total_similarity(lexic_sim, sem_sim):
    return ((3/4)*lexic_sim + (1/4)*sem_sim)

#document1 = "the dog eats a fish. I like big butts and i cannot lie."
#document2 = "the cat eats a fish. Its only for the weak. No one can deny."
print(detect_plagiarism())
