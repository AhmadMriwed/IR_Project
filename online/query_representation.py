import pandas as pd

from service import inverted_index
from service import store_file
from service import remove_duplicated
from service import term_frequency

tf_df= pd.DataFrame
tfidf_df= pd.DataFrame
def query_representation(corpus):
    # print("=============================================")
    # print("==               Indexing Query            ==")
    # print("=============================================")
    global tf_df
    global tfidf_df
    # duplicated
    duplicated_corpus = remove_duplicated.remove_duplicated(corpus)
    # print(duplicated_corpus)
    # print("Done remove duplicated")
    store_file.creat_file_from_map(store_file.path_duplicated_q, duplicated_corpus)

    # inverted index
    inverted_index_corpus = inverted_index.create_inverted_index(duplicated_corpus)
    store_file.creat_file_from_map(store_file.path_inverted_index_q,inverted_index_corpus)
    # print('Done inverted index')

    # term frequency
    #tf_df=term_frequency.calculate_tf(corpus)
    # Store the DataFrame in a text file
    # tf_df.to_csv('output.csv','\t', False)
    #str_tf_df = convert_datafarme_to_text(tf_df)
    #store_file.creat_file(store_file.path_tf_df_q, str_tf_df)
    # print('Done term frequency')
    # term frequency idf
    tfidf_df=term_frequency.calculate_tfidf(corpus)
    # Store the DataFrame in a text file
    # tfidf_df.to_csv('output.csv','\t', False)
    #str_tfidf_df = convert_datafarme_to_text(tfidf_df)
    #store_file.creat_file(store_file.path_tfidf_df_q, str_tfidf_df)
    # print('Done term frequency idf')

    # print("******************* Done *********************\n")
    return inverted_index_corpus






