from src.code.lexic_preprocessing import *
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from src.code.utils import *

def detect_plagiarism(documents):

    # Separar por oraciones los documentos

    sentences1 = split_sentences(documents[0])
    sentences2 = split_sentences(documents[1])

    # Preprocesar documentos
    vect_text = np.array(preprocess(documents))
    
    # Calcular similitud
    similarity = cosine_similarity(vect_text[0].reshape(1, -1), vect_text[1].reshape(1, -1))[0][0]

    # Retornar similitud
    return similarity


document1 = "the dog eats a fish"
document2 = "the cat eats a fish"
similarity = detect_plagiarism([document1, document2])
print(similarity)