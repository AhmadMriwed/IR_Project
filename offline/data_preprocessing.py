
from service import tokenize
from service import stemming
from service import lemmatize
from service import stop_words
from service import punctuation
from service import store_file

# read data set
#corpus = docs.read_dataset()

#configoration.change_language(configoration.language_code_ar)
#corpus = doc.convert_data_to_corpous(doc.data_ar)
#corpus = doc.convert_data_to_corpous(doc.data)
#print(corpus)
#print("count docs : " +f"{len(corpus)}")
#print(store_file.convert_map_to_text_limit(corpus,10))
#store_file.creat_file_from_map(store_file.path_tokenize,corpus)

# clean data set
def clean_dataset(corpus,language_code):
    print("=============================================")
    print("==               Clean DataSet             ==")
    print("=============================================")
    # tokenize
    tokenized_corpus = tokenize.tokenize(corpus,language_code=language_code)
   # print(tokenized_corpus)
    print("Done tokenize")
    store_file.creat_file_from_map(store_file.path_tokenize,tokenized_corpus)
    # punctuation
    punctuation_corpus = punctuation.remove_punctuation(tokenized_corpus,language_code=language_code)
    #print(punctuation_corpus)
    print("Done remove punctuation")
    store_file.creat_file_from_map(store_file.path_punctuation,punctuation_corpus)
    # stemming
    stemming_corpus=stemming.stemming(punctuation_corpus,language_code=language_code)
    #print(stemming_corpus)
    print("Done stemming")
    store_file.creat_file_from_map(store_file.path_stemming,stemming_corpus)
    # lemmatize
    lemmatize_corpus = lemmatize.lemmatize(stemming_corpus,language_code=language_code)
    #print(lemmatize_corpus)
    print("Done lemmatize")
    store_file.creat_file_from_map(store_file.path_lemmatize,lemmatize_corpus)
    # stopwords
    stopwords_corpus = stop_words.remove_stopwords(lemmatize_corpus,language_code=language_code)
    #print(stopwords_corpus)
    print("Done remove stopwords")
    store_file.creat_file_from_map(store_file.path_stopwords, stopwords_corpus)

    # duplicated
    #duplicated_corpus = remove_duplicated.remove_duplicated(stopwords_corpus)
    # print(duplicated_corpus)
    #print("Done remove duplicated")
    #store_file.creat_file(store_file.path_duplicated, store_file.convert_map_to_text(duplicated_corpus, 10))
    print("******************* Done *********************\n")
    del tokenized_corpus,punctuation_corpus,stemming_corpus,lemmatize_corpus
    return stopwords_corpus

# data preprocessing
def data_preprocessing(corpus,language_code):
    return clean_dataset(corpus,language_code)









