import gc

from configoration import configoration
from data_source import docs, doc
from offline import data_representation as drp, data_preprocessing as dpp
from online import query_representation as qrp, rank_documents as rd, query_matching as qm, query_processing as qp
from evaluation import app_evaluation as app_ev
from cluster import cluster_app as ca
from cluster import search_cluster as sc
from service import cluster
from service import store_file
import farasa

# read data set
corpus = docs.read_dataset()
#configoration.change_language(configoration.language_code_ar)
#configoration.cluster_exc=True

#corpus = doc.convert_data_to_corpous(doc.data_ar)
#corpus = doc.convert_data_to_corpous(doc.data)
print("count docs : " +f"{len(corpus)}")
print(store_file.convert_map_to_text_limit(corpus,10))

query ={"query":"what is step by india"}

data_preprocessing={}
data_representation={}
query_processing={}
query_representation={}
query_matching={}
rank_docs=[]
def offline():
    global data_preprocessing
    global data_representation
    data_preprocessing = dpp.data_preprocessing(corpus)
    # app cluster
    ca.cluster_app(corpus)
    data_representation=drp.data_representation(data_preprocessing)
    #del data_preprocessing
    #gc.collect()

def online():
    global query_processing
    global query_representation
    global query_matching
    global rank_docs
    query_processing=qp.query_processing(corpus=query)
    query_representation=qrp.query_representation(query_processing)
    data_inverted_index=sc.search_cluster_by_s(data_representation,ca.clusters,query_processing)
    query_matching=qm.query_matching(query_representation,data_inverted_index)
    rank_docs=rd.rank(qrp.tfidf_df,drp.tfidf_df,query_matching['query'][qm.unique_docs_key],query_matching['query'][qm.unique_words_key])

def evaluation() :
    app_ev.evaluation()






def  run():
#    docs.read_dataset_ar()
    offline()
    #online()
    evaluation()


run()








