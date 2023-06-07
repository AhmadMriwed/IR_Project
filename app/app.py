import gc

from offline import data_representation as drp, data_preprocessing as dpp
from online import query_representation as qrp, rank_documents as rd, query_matching as qm, query_processing as qp
from evaluation import app_evaluation as app_ev
import farasa

data_preprocessing={}
data_representation={}
query_processing={}
query_representation={}
query_matching={}
rank_docs=[]
def offline():
    global data_preprocessing
    global data_representation
    data_preprocessing = dpp.data_preprocessing()
    data_representation=drp.data_representation(data_preprocessing)
    del data_preprocessing
    gc.collect()

def online():
    global query_processing
    global query_representation
    global query_matching
    global rank_docs
    query_processing=qp.query_processing()
    query_representation=qrp.query_representation(query_processing)
    query_matching=qm.query_matching(query_representation,data_representation)
    rank_docs=rd.rank(qrp.tfidf_df,drp.tfidf_df,query_matching['query'][qm.unique_docs_key],query_matching['query'][qm.unique_words_key])

def evaluation() :
    app_ev.evaluation()






def  run():
    offline()
    #online()
    #evaluation()


run()








