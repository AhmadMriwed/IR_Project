from nltk import ISRIStemmer
from nltk.stem import WordNetLemmatizer
#from farasa.segmenter import FarasaSegmenter

from configoration import configoration

lemmatizer = WordNetLemmatizer()

def lemmatize(corpus,language_code=configoration.language_code):
    if configoration.language_code is configoration.language_code_ar:
        return lemmatize_ar(corpus)
    else:
        return lemmatize_en(corpus)

#lemmatize_corpus = {}
def lemmatize_en(corpus):
    lemmatize_corpus = {}
    lemmatize_corpus = lemmatize_non(corpus)
    lemmatize_corpus = lemmatize_noun(lemmatize_corpus)
    lemmatize_corpus = lemmatize_verb(lemmatize_corpus)
    lemmatize_corpus = lemmatize_adjective(lemmatize_corpus)
    #print("Done lemmatize")
    return lemmatize_corpus

def lemmatize_non(corpus):
    lemmatize_corpus = {}
    for doc_id, words in corpus.items():
        lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
        lemmatize_corpus[doc_id] = lemmatized_words
    return lemmatize_corpus
def lemmatize_adjective(corpus):
    lemmatize_corpus = {}
    for doc_id, words in corpus.items():
        lemmatized_words = [lemmatizer.lemmatize(word, "a") for word in words]
        lemmatize_corpus[doc_id] = lemmatized_words
    return lemmatize_corpus
def lemmatize_verb(corpus):
    lemmatize_corpus = {}
    for doc_id, words in corpus.items():
        lemmatized_words = [lemmatizer.lemmatize(word, "v") for word in words]
        lemmatize_corpus[doc_id] = lemmatized_words
    return lemmatize_corpus
def lemmatize_noun(corpus):
    lemmatize_corpus = {}
    for doc_id, words in corpus.items():
        lemmatized_words = [lemmatizer.lemmatize(word, "n") for word in words]
        lemmatize_corpus[doc_id] = lemmatized_words
    return lemmatize_corpus



def lemmatize_ar(corpus):
    lemmatizer_ar=ISRIStemmer()
   # lemmatizer_ar = FarasaLemmatizer()
    lemmatized_corpus = {}

    for doc_id, words in corpus.items():
        lemmatized_words = [lemmatizer_ar.suf32(word) for word in words]
        lemmatized_corpus[doc_id] = lemmatized_words

    return lemmatized_corpus
 










 