import re
def split_sentences(text):
    text = text.replace("\n", " ")

    # Detectar oraciones usando puntuación
    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z]\.)(?<=\.|\?|!|;)\s", text)

    # Eliminar oraciones vacías
    sentences = [sentence for sentence in sentences if sentence.strip()]
    return sentences

def read_documents(doc1,doc2):
    # Leer documentos de la carpeta docs
    with open("src/docs/"+doc1, "r") as file:
        document1 = file.read()
    with open("src/docs/"+doc2, "r") as file:
        document2 = file.read()
    return [document1, document2]
