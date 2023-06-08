# read data set
from data_source import docs, doc
from service import store_file
import pandas as pd
from configoration import configoration
from offline import data_representation as drp, data_preprocessing as dpp
from online import query_representation as qrp, rank_documents as rd, query_matching as qm, query_processing as qp
from cluster import cluster_app as ca
from cluster import search_cluster as sc


corpus = docs.read_dataset()
#corpus_ar = docs.read_dataset()
#configoration.change_language(configoration.language_code_ar)
configoration.cluster_exc=True

corpus_ar = doc.convert_data_to_corpous(doc.data_ar)
#corpus = doc.convert_data_to_corpous(doc.data)
print("count docs : " +f"{len(corpus)}")
print(store_file.convert_map_to_text_limit(corpus,10))

query ={"query":"what is step by india"}



data_preprocessing_en={}
data_preprocessing_ar={}
data_representation_en={}
data_representation_ar={}
query_processing={}
query_representation={}
query_matching={}
tfidf_df_en= pd.DataFrame
tfidf_df_ar= pd.DataFrame
rank_docs=[]
def offline(corpus,language_code):
    global data_preprocessing_en
    global data_preprocessing_ar
    global data_representation_en
    global data_representation_ar
    global tfidf_df_en
    global tfidf_df_ar
    data_preprocessing = dpp.data_preprocessing(corpus)
    # app cluster
    ca.cluster_app(corpus)
    data_representation=drp.data_representation(data_preprocessing)
    if(language_code==configoration.language_code_ar):
        data_preprocessing_ar=data_preprocessing
        data_representation_ar=data_representation
        tfidf_df_ar=drp.tfidf_df
    else:
        data_preprocessing_en = data_preprocessing
        data_representation_en = data_representation
        tfidf_df_en = drp.tfidf_df

    #del data_preprocessing
    #gc.collect()

def online(query=query):
    global query_processing
    global query_representation
    global query_matching
    global rank_docs
    query_processing=qp.query_processing(corpus=query)
    query_representation=qrp.query_representation(query_processing)
    data_inverted_index=sc.search_cluster_by_s(
        configoration.get_by_language(data_representation_en,data_representation_ar),
        ca.clusters,query_processing)
    query_matching=qm.query_matching(query_representation,data_inverted_index)
    rank_docs=rd.rank(qrp.tfidf_df,
                      configoration.get_by_language(tfidf_df_en,tfidf_df_ar),
                      query_matching['query'][qm.unique_docs_key],query_matching['query'][qm.unique_words_key])
    return rank_docs
