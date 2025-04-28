from nltk import ngrams
from collections import Counter
text = "Named Entity Recognition is a part of NLP."
tokens = text.lower().split()
bigrams = list(ngrams(tokens, 2))
bigram_freq = Counter(bigrams)
for bigram, frequency in bigram_freq.items():
    print(f"{bigram} : {frequency}")

    

