import string

# Define the punctuation marks to be removed
from configoration import configoration

punctuation_list=' '.join(string.punctuation).split()


#punctuation_corpus = {}
def remove_punctuation(corpus,language_code=configoration.language_code):
    if language_code is configoration.language_code_ar:
        return remove_punctuation_ar(corpus)
    else:
        return remove_punctuation_en(corpus)

def remove_punctuation_en(corpus):
    punctuation_corpus = {}
    for doc_id, words in corpus.items():
        filtered_words = [word for word in words if word not in punctuation_list]
        punctuation_corpus[doc_id] = filtered_words
    #print("Done remove punctuation")
    return punctuation_corpus

def remove_punctuation_ar(corpus):
    punctuation_corpus = {}
    arabic_punctuation = "،؛؟.٪؛،:«»()[]{}<>+=-*/&|~"
    translator = str.maketrans('', '', arabic_punctuation)
    for doc_id, words in corpus.items():
        filtered_words = [word.translate(translator) for word in words]
        punctuation_corpus[doc_id] = filtered_words

    return punctuation_corpus











 