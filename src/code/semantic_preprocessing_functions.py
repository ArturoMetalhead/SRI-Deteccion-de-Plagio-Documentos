import torch
from transformers import BertTokenizer, BertModel
from utils import split_sentences

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def vectorize_sentences(sentences):
    sentence_embeddings = []
    tokens = tokenizer.batch_encode_plus(sentences,padding=True, truncation=True, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**tokens)
        embeddings = outputs.last_hidden_state

    for embedding in embeddings:
        sentence_embeddings.append(torch.mean(embedding, dim=0))

    return sentence_embeddings
