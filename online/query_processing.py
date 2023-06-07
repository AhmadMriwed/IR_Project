
from data_source import docs
from data_source import doc
from service import tokenize
from service import stemming
from service import lemmatize
from service import stop_words
from service import punctuation
from service import store_file

# read query


#corpus ={"query":"what is step by india"}
corpus ={"query":"Did Ben Affleck shine more than Christian Bale as Batman??"}
#corpus ={"query":"Who were the Aztec?"}
#print(corpus)
#print("count query : " +f"{len(corpus)}")
#print(store_file.convert_map_to_text_limit(corpus,10))
print("query : "+f"{corpus}")
store_file.creat_file_from_map(store_file.path_query,corpus)

# clean query
def clean_query(corpus):
    # print("=============================================")
    # print("==                Clean Query              ==")
    # print("=============================================")
    # tokenize
    tokenized_corpus = tokenize.tokenize(corpus)
    # print("Done tokenize")
    store_file.creat_file_from_map(store_file.path_tokenize_q,tokenized_corpus)
    # punctuation
    punctuation_corpus = punctuation.remove_punctuation(tokenized_corpus)
    #print(punctuation_corpus)
    # print("Done remove punctuation")
    store_file.creat_file_from_map(store_file.path_punctuation_q,punctuation_corpus)
    # stemming
    stemming_corpus=stemming.stemming(punctuation_corpus)
    #print(stemming_corpus)
    # print("Done stemming")
    store_file.creat_file_from_map(store_file.path_stemming_q,stemming_corpus)
    # lemmatize
    lemmatize_corpus = lemmatize.lemmatize(stemming_corpus)
    #print(lemmatize_corpus)
    # print("Done lemmatize")
    store_file.creat_file_from_map(store_file.path_lemmatize_q,lemmatize_corpus)
    # stopwords
    stopwords_corpus = stop_words.remove_stopwords(lemmatize_corpus)
    #print(stopwords_corpus)
    # print("Done remove stopwords")
    store_file.creat_file_from_map(store_file.path_stopwords_q, stopwords_corpus)

    # duplicated
    #duplicated_corpus = remove_duplicated.remove_duplicated(stopwords_corpus)
    # print(duplicated_corpus)
    #print("Done remove duplicated")
    # print("******************* Done *********************\n")
    del tokenized_corpus,punctuation_corpus,stemming_corpus,lemmatize_corpus
    return stopwords_corpus


# query preprocessing
def query_processing(corpus=corpus):
    return  clean_query(corpus)






