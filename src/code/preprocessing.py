from preprocessing_functions import *

def preprocess(documents, queries, qrels):
    """
    Preprocess a list of documents by performing tokenization, noise removal, stopword removal,
    morphological reduction, filtering by occurrence, building a vocabulary, vector representation,
    part-of-speech tagging, calculating correlation matrix, and saving the preprocessed data to a JSON file.

    Args:
        documents (list): A list of documents to be preprocessed.

    Returns:
        None
    """
    #Tokenizar documentos
    tokenized_docs = tokenization(documents) 

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

    vectorial_docs = docs_vectorial_rep(vocabulary, filtered_docs)