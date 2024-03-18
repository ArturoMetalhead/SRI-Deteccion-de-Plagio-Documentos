import torch
from transformers import BertTokenizer, BertModel
from utils import split_sentences
import torch.nn.functional as F

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def vectorize_sentences(sentences):
    sentence_embeddings = []
    tokens = tokenizer.batch_encode_plus(sentences,padding=True, truncation=True, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**tokens)
        embeddings = outputs.last_hidden_state

    normalized_sentences = [F.normalize(embedding, p=2, dim=0) for embedding in embeddings]

    for embedding in normalized_sentences:
        sentence_embeddings.append(torch.mean(embedding, dim=0))


    return sentence_embeddings