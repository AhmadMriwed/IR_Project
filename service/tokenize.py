from nltk.tokenize import sent_tokenize, word_tokenize

#tokenized_corpus = {}

#rom farasa.segmenter import FarasaSegmenter
from configoration import configoration


def tokenize(corpus,language_code=configoration.language_code):

    if language_code is configoration.language_code_ar:
        return tokenize_en(corpus)
    else:
        return tokenize_en(corpus)


def tokenize_ar(corpus):
    from farasa.segmenter import FarasaSegmenter
    segmenter = FarasaSegmenter()
    tokenized_corpus = {}
    for doc_id, text in corpus.items():
        tokens = segmenter.segment(text).replace("+", " ").split()
        tokenized_corpus[doc_id] = tokens
    #print("Done tokenize")
    return tokenized_corpus

def tokenize_en(corpus):
    tokenized_corpus = {}
    for doc_id, text in corpus.items():
        tokens = word_tokenize(text.lower())
        tokenized_corpus[doc_id] = tokens
    #print("Done tokenize")
    return tokenized_corpus
 
#tokenize(corpus)
#print(tokenized_corpus) 









 