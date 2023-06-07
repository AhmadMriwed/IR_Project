import gc

import numpy as np

rank_docs = {}

def rank(query_vector,docs_vector,target_documents, target_words,target_queries=["query"]):
    from service import store_file
    global  rank_docs

    sub_df=extract_sub_df(docs_vector,target_documents, target_words)

    sub_query_vector=extract_sub_df(query_vector,target_queries, target_words)
    query_matrix=np.array(sub_query_vector.values)
    if not any(query_matrix[0]):
        rank_list=[]
    else:
        rank_list=rank_documents_list(query_matrix, np.array(sub_df.values))
    #print(rank_list)
    # ترتيب العناصر وفقًا للقيمة
    rank_docs=[target_documents[item] for item in rank_list ]
    rank_docs.reverse()
    store_file.creat_file(store_file.path_query_rank,str(rank_docs))

    del sub_query_vector,sub_df,query_matrix,docs_vector,target_documents,target_words,rank_list
    gc.collect()
    #print("Done rank documents")
    return rank_docs

def rank_documents_list(query_vector, document_vectors):
    from sklearn.metrics.pairwise import cosine_similarity

    similarity_scores = cosine_similarity(query_vector, document_vectors)
    sorted_indices = np.argsort(similarity_scores)
    ranked_documents = sorted_indices.squeeze().tolist()
    if not isinstance(ranked_documents, list) :
        return [ranked_documents]
    del sorted_indices, similarity_scores,query_vector,document_vectors
    gc.collect()
    return ranked_documents


def extract_sub_df(tfidf_df, target_documents, target_words):
    target_words1 =[word for word in target_words if word in tfidf_df ]
    subset = tfidf_df.loc[target_documents, target_words1]
    del target_words1,tfidf_df,target_documents
    gc.collect()
    return subset

def sort_two_list(list1,list2):

    mapping = {rank: doc for doc, rank in zip(list1, list2)}
    list2.sort()
    list1_sort=[mapping[item] for item in list2]
    list2.reverse()
    list1_sort.reverse()
    mapping={doc:rank  for doc, rank in zip(list1_sort, list2)}
    del list1_sort
    return  mapping

