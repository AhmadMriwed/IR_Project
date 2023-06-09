from nltk.corpus import stopwords
from configoration import configoration
# Get the list of stopwords
stopwords_list =["''","``","..","n't","'s","u","'m","’","'","/","...",".",'”','””','wa','hi','doe','ha','whi']
stopwords_list += set(stopwords.words('english'))
stopwords_list_ar=['لل','أليس','','ك','س','ف','ب','أو','و','ما','لو','ال','لا','ّ','ٌ',' ','ء','ئ','‘','؛','أ','إ',',','’','آ','~','ًٍَُِْ',' ','  ','ؤ',' ',' ',' ',' ','لأ']
stopwords_list_ar += set(stopwords.words('arabic'))


def remove_stopwords(corpus,language_code=configoration.language_code):
    if configoration.language_code is configoration.language_code_ar:
        return remove_stopwords_ar(corpus)
    else:
        return remove_stopwords_en(corpus)


def remove_stopwords_en(corpus):
    stopwords_corpus = {}
    for doc_id, words in corpus.items():
        # Remove the stopwords from the words
        filtered_words = [word for word in words if word not in stopwords_list]
        stopwords_corpus[doc_id] = filtered_words
    #print("Done remove stopwords")
    return stopwords_corpus

def remove_stopwords_ar(corpus):
    stopwords_corpus = {}
    for doc_id, words in corpus.items():
        filtered_words = [word for word in words if word not in stopwords_list_ar]
        stopwords_corpus[doc_id] = filtered_words

    return stopwords_corpus









