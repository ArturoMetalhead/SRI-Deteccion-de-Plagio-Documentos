import nltk
import spacy
import gensim
from math import log

def tokenization(documents):
    """
    Perform tokenization on a list of documents using the "en_core_web_sm" model from spaCy.

    Args:
        documents (list): A list of documents to tokenize.

    Returns:
        list: A list of lists of tokens, where each inner list represents the tokens of a document.
    """
    nlp = spacy.load("en_core_web_sm")
    return [[token for token in nlp(doc)] for doc in documents]


def remove_noise(tokenized_docs):
    """
    Remove non-alphabetic tokens from a list of tokenized documents.

    Args:
        tokenized_docs (list): A list of tokenized documents.

    Returns:
        list: A list of tokenized documents with non-alphabetic tokens removed.
    """
    return [[token for token in doc if token.is_alpha] for doc in tokenized_docs]


def remove_stopwords(tokenized_docs):
    """
    Remove stopwords from a list of tokenized documents.

    Args:
        tokenized_docs (list): A list of tokenized documents.

    Returns:
        list: A list of tokenized documents with stopwords removed.
    """
    stopwords = spacy.lang.en.stop_words.STOP_WORDS
    return [[token for token in doc if token.text not in stopwords] for doc in tokenized_docs]


def morphological_reduction(tokenized_docs, use_lemmatization=True):
    """
    Perform morphological reduction on a list of tokenized documents.

    Args:
        tokenized_docs (list): A list of tokenized documents.
        use_lemmatization (bool, optional): Flag indicating whether to use lemmatization (default: True).

    Returns:
        list: A list of tokenized documents with morphological reduction applied.
    """
    stemmer = nltk.stem.PorterStemmer()
    return [
        [token.lemma_ if use_lemmatization else stemmer.stem(token.text) for token in doc]
        for doc in tokenized_docs
    ]


def filter_tokens_by_occurrence(tokenized_docs, no_below=1, no_above=20):
    """
    Filter tokens in a list of tokenized documents based on their occurrence frequency.

    Args:
        tokenized_docs (list): A list of tokenized documents.
        no_below (int, optional): Minimum number of occurrences for a token to be included.
        no_above (float, optional): Maximum proportion of documents a token can appear in.

    Returns:
        tuple: A tuple containing the filtered tokens and the dictionary used for filtering.
            - filtered_tokens (list): A list of tokenized documents with filtered tokens.
            - dictionary (gensim.corpora.Dictionary): The dictionary used for filtering.
    """
    dictionary = {}
    dictionary = gensim.corpora.Dictionary(tokenized_docs)
    dictionary.filter_extremes(no_below=no_below, no_above=no_above)

    filtered_words = [word for _, word in dictionary.iteritems()]
    filtered_tokens = [
        [word for word in doc if word in filtered_words]
        for doc in tokenized_docs
    ]

    return filtered_tokens, dictionary


def build_vocabulary(dictionary):
    """
    Build a vocabulary list from a dictionary object.

    Args:
        dictionary (gensim.corpora.Dictionary): A dictionary object.

    Returns:
        list: A list of tokens representing the vocabulary.
    """
    vocabulary = list(dictionary.token2id.keys())
    return vocabulary


def vector_representation(filtered_docs, vocabulary):
    """
    Generate vector representations of filtered documents using term frequency-inverse document frequency (TF-IDF).

    Args:
        filtered_docs (list): A list of tokenized documents with filtered tokens.
        vocabulary (list): A list of tokens representing the vocabulary.

    Returns:
        list: A list of vector representations of the filtered documents.
    """
    vector_repr=[]
    term_frequency = []
    
    for doc in filtered_docs:
        doc_i=[]
        for voc in vocabulary:
            term_frequency.append(doc.count(voc))

        for word in vocabulary:
            f=doc.count(word)
            tf = f / max(term_frequency)
            idf=log(len(filtered_docs)/(1+sum([1 for doc in filtered_docs if word in doc])))
            doc_i.append(tf*idf)
        vector_repr.append(doc_i)

    return vector_repr