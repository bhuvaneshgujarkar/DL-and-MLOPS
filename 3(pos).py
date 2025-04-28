import spacy
nlp = spacy.load("en_core_web_sm")
sentence = "The quick brown fox jumps over the lazy dog and eats it."
doc = nlp(sentence)
print("\nPOS Tagging using spaCy:")
for token in doc:
    print(f"{token.text}: {token.pos_} ({token.tag_})")