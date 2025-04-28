def perform_ner(text):
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for ent in doc.ents:
        print(f"{ent.text} -> {ent.label_}")
your_text = "Elon Musk is the CEO of Tesla, based in the United States."
perform_ner(your_text)