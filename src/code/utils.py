import re
def split_sentences(text):
    text = text.replace("\n", " ")

    # Detectar oraciones usando puntuación
    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z]\.)(?<=\.|\?|!|;)\s", text)

    # Eliminar oraciones vacías
    sentences = [sentence for sentence in sentences if sentence.strip()]
    return sentences
