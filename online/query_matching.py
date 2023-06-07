import gc

from service import store_file
doc_count_key="doc_count"
unique_words_key="unique_words"
unique_docs_key="unique_docs"
matched_docs_key="matched_docs"

def search_terms(terms, inverted_index):
    results = {}
    for term in terms:
        if term in inverted_index:
            results[term] = inverted_index[term]
    return results

def get_docs_from_inindex_by_query(query, inverted_index):
    terms = query
    results = []
    for term in terms:
        if term in inverted_index:
            results+=inverted_index[term]
    return results

get_terms={}
matched_docs=[]
unique_words=[]
unique_docs=[]
query_matching={}
def query_matching(query_processing,inverted_index):
    # global  get_terms
    # global  matched_docs
    # global  unique_words
    # global  query_matching
    get_terms = search_terms(query_processing, inverted_index)
    matched_docs =get_docs_from_inindex_by_query(query_processing,get_terms)
    unique_words = list(set(get_terms))  # الكلمات الفريدة في الوثيقة
    unique_docs= list(set(matched_docs))  # الكلمات الفريدة في الوثيقة
    doc_count = len(unique_docs)  # عدد الكلمات في الوثيقة

    query_matching={
        "query":{
            matched_docs_key:matched_docs,
            unique_words_key:unique_words,
            unique_docs_key:unique_docs,
            doc_count_key:doc_count,
        }
    }
    store_file.creat_file(store_file.path_query_matching,store_file.convert_map_to_text(query_matching))
    #print("Done query matching")
    # del doc_count,unique_docs,unique_words,matched_docs,get_terms
    # gc.collect()
    return query_matching