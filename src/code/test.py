# from transformers import BertTokenizer, BertModel



# tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
# model = BertModel.from_pretrained('bert-base-uncased')

# text="The dog (Canis familiaris[4][5] or Canis lupus familiaris[5]) is a domesticated descendant of the wolf. Also called the domestic dog, it is derived from extinct gray wolves,[6][7] and the gray wolf is the dog's closest living relative.[8] The dog was the first species to be domesticated[9][8] by humans. Hunter-gatherers did this over 15,000 years ago in Oberkassel, Bonn,[7] which was before the development of agriculture.[1] Due to their long association with humans, dogs have expanded to a large number of domestic individuals[10] and gained the ability to thrive on a starch-rich diet that would be inadequate for other canids."


# inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
# outputs = model(**inputs)
# trueoutput=outputs.last_hidden_state.mean(dim=1).detach().numpy()[0]

# print("hello")