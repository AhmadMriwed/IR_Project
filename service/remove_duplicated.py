
#duplicated_corpus = {}
def remove_duplicated(corpus):
    duplicated_corpus = {}
    for doc_id, words in corpus.items():
        duplicated_corpus[doc_id] = list(set(words))
    #print("Done remove duplicated")
    return duplicated_corpus
 










 