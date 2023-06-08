import gc


from online import rank_documents as rd, query_matching as qm, query_processing as qp, query_representation as qrp
from offline import data_representation as drp
from service import store_file
from cluster import search_cluster as sc
from cluster import cluster_app as ca
#procssing representation matching rank
def prmr(queries):

    query_processing = qp.query_processing(queries)
    print("Done queries processing")
    print("=============================================")
    print("==                Queries PRMR             ==")
    print("=============================================")
    #query_representation ={}
    # query_matching ={}
    rank_docs={}
    i=0
    for key in queries.keys():
        # query_representation[key] = qrp.query_representation({key:query_processing[key]})
        # query_matching[key] = qm.query_matching(query_processing[key], drp.inverted_index_corpus)
        # rank_docs[key] = rd.rank(qrp.tfidf_df, drp.tfidf_df, query_matching[key]['query'][qm.unique_docs_key], query_matching[key]['query'][qm.unique_words_key],[key])
        if(i<10):
            i+=1
            query_representation = qrp.query_representation({key: query_processing[key]})
            query_matching = qm.query_matching(query_representation, drp.inverted_index_corpus)
            rank_docs[key] = rd.rank(qrp.tfidf_df, drp.tfidf_df, query_matching['query'][qm.unique_docs_key],
                                      query_matching['query'][qm.unique_words_key], [key])
            del query_matching,query_representation
            gc.collect()


    # store_file.creat_file_from_map(store_file.path_inverted_index_q,query_representation)
    # print("Done queries representation")
    # store_file.creat_file_from_map(store_file.path_query_matching,query_matching)
    # print("Done queries matching")
    store_file.creat_file_from_map(store_file.path_query_rank,rank_docs)
    print("Done queries rank")
    print("*************** Done queries ***************")

    return  rank_docs


def prmr2(queries):
    print("=============================================")
    print("==                Queries PRMR             ==")
    print("=============================================")
    rank_docs={}
    i=0
    for key in queries.keys():
       if(i<10):
            i+=1
            query_processing = qp.query_processing({key: queries[key]})
            query_representation = qrp.query_representation({key: query_processing[key]})
            data_inverted_index = sc.search_cluster_by_s(
                drp.inverted_index_corpus,
                ca.clusters, query_processing)
            query_matching = qm.query_matching(query_representation, data_inverted_index)
            rank_docs[key] = rd.rank(qrp.tfidf_df, drp.tfidf_df, query_matching['query'][qm.unique_docs_key],
                                      query_matching['query'][qm.unique_words_key], [key])
            del query_matching,query_representation
            gc.collect()
            if(i%50 ==0):
                print("Done "+f"{i}")
    store_file.creat_file_from_map(store_file.path_query_rank,rank_docs)
    print("Done queries rank")
    print("*************** Done queries ***************")
    return  rank_docs