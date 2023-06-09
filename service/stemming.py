from nltk.stem import PorterStemmer
from nltk.stem import ISRIStemmer

from configoration import configoration

stemmer=PorterStemmer()
stemmer_ar= ISRIStemmer()

#stemming_corpus = {}

def stemming(corpus,language_code=configoration.language_code):
    if language_code is configoration.language_code_ar:
        return stemming_en(corpus)
    else:
        return stemming_en(corpus)

def stemming_en(corpus):
    stemming_corpus = {}
    for doc_id, words in corpus.items():
        stemmed_words = [stemmer.stem(word) for word in words]
        stemming_corpus[doc_id] = stemmed_words
    #print("Done stemming")
    return stemming_corpus

def stemming_ar(corpus):
    stemming_corpus = {}
    for doc_id, words in corpus.items():
        stemmed_words = [stemmer_ar.stem(word) for word in words]
        stemming_corpus[doc_id] = stemmed_words
    #print("Done stemming")
    return stemming_corpus

# def stemming_ar(corpus):
#     stemming_corpus = {}
#     for doc_id, words in corpus.items():
#         stemmed_words = [stemmer_ar.stem(word) for word in words]
#         stemming_corpus[doc_id] = stemmed_words
#     #print("Done stemming")
#     return stemming_corpus










 