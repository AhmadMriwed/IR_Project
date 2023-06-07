from collections import defaultdict
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from  service import store_file
#str_corpus={}
def convert_str(corpus):
    str_corpus = {}
    for doc_id, words in corpus.items():
        str_words = " ".join(words)
        str_corpus[doc_id] = str_words
    return str_corpus
def find_max_len_list(list):
    max=""
    for item in list:
        if(len(str(max))<len(str(item))):
            max=str(item)
    return  max
def calculate_tf(corpus):
    # convert list to string
    str_corpus=convert_str(corpus)
    # Extract the document texts and IDs
    doc_texts = list(str_corpus.values())
    doc_ids = list(str_corpus.keys())
    # Create a list of documents
    documents = list(doc_texts)
    # Create a CountVectorizer object
    vectorizer =  CountVectorizer()
    # Fit the vectorizer on the document texts and transform them into a matrix
    tf_matrix = vectorizer.fit_transform(documents)

    # Convert the TF-IDF matrix to a Pandas DataFrame
    tf_df = pd.DataFrame(tf_matrix.toarray(),doc_ids, vectorizer.get_feature_names_out())





    return  tf_df
def calculate_tfidf(corpus):
    # convert list to string
    str_corpus=convert_str(corpus)
    # Extract the document texts and IDs
    doc_texts = list(str_corpus.values())
    doc_ids = list(str_corpus.keys())
    # Create a list of documents
    documents = list(doc_texts)
    # Create a TfidfVectorizer object
    vectorizer =  TfidfVectorizer()
    # Fit the vectorizer on the document texts and transform them into a matrix
    tf_matrix = vectorizer.fit_transform(documents)
    # Convert the TF-IDF matrix to a Pandas DataFrame
    tfidf_df = pd.DataFrame(tf_matrix.toarray(),doc_ids, vectorizer.get_feature_names_out())

    return  tfidf_df



def calculate_tf_doc(document):
    tf = {}
    terms = document
    term_count = len(terms)
    for term in terms:
        tf[term] = terms.count(term) / term_count
    return tf


def convert_datafarme_to_text(df):
    text=""
    # Get the longest element in the list
    longest_element = find_max_len_list(df.index.values)
    fixed_len=4
    # Get line rows
    line_indexes = "{:>{}}".format("", len(longest_element))
    for column in df.columns:
        line_indexes += "\t" +"{:>{}}".format(column, fixed_len)
    text+=line_indexes+"\n"
    # Get All lines
    for index, row in df.iterrows():
        # Get column
        line = f"{index}" + "{:>{}}".format("", len(longest_element) - len(index))
        # Get line
        for ind, value in zip(row.values, row.index):
            line += "\t"
            line += "{:>{}}".format(str(ind).ljust(fixed_len)[:fixed_len], max([len(value),fixed_len]))
        text+=line+"\n"
    return  text

