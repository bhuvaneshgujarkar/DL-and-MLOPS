import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
text = "Apple Inc. was founded by Steve Jobs and is headquartered in Cupertino, California."
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, "->", ent.label_)