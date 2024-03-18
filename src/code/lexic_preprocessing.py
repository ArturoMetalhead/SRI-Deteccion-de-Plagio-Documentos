from src.code.lexic_preprocessing_functions import *
import numpy as np

def preprocess(sentence1,sentence2):
    """
    Preprocess two sentences to be compared

    Parameters
    ----------
    sentence1 : str
        First sentence to be compared
    sentence2 : str
        Second sentence to be compared

    Returns
    -------
    np.array
        Vector representation of the first sentence
    np.array
        Vector representation of the second sentence
    """

    sentences= sentence1 + sentence2

    vectors1=[]
    vectors2=[]

    #Tokenizar documentos
    tokenized_docs = tokenization(sentences) 

    #Eliminar ruido
    cleaned_docs = remove_noise(tokenized_docs)

    #Eliminar Stop-words
    no_stop_words_docs = remove_stopwords(cleaned_docs)

    #Reducir Morfológicamente
    reduced_docs = morphological_reduction(no_stop_words_docs)

    #Filtrar por ocurrencia
    filtered_docs, dictionary = filter_tokens_by_occurrence(reduced_docs)

    #Construir Vocabulario
    vocabulary = build_vocabulary(dictionary)

    #Representar Vectorialmente
    vector_rep = vector_representation(filtered_docs, vocabulary)

    #Agregar vectores a la lista
    for i in range(len(sentence1)):
        vectors1.append(vector_rep[i])
    
    for i in range(len(sentence1),len(sentences)):
        vectors2.append(vector_rep[i])

    #Convertir a np array
    vectors1=np.array(vectors1)
    vectors2=np.array(vectors2)

    return vectors1, vectors2