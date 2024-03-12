from src.code.preprocessing import *
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def detect_plagiarism(documents):

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