from collections import defaultdict

def create_inverted_index(corpus):
    inverted_index = defaultdict(list)
    for doc_id, doc_content in corpus.items():
        terms=doc_content
        for term in terms:
            inverted_index[term].append(doc_id)
    return dict(inverted_index)
