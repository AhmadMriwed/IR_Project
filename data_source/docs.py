import csv
import json

import ir_datasets
dataset = ir_datasets.load("beir/quora/dev")
#dataset = ir_datasets.load("beir/quora")
#dataset = ir_datasets.load("wikiclir/ar")
corpus={}
corpus_ar={}
queries={}
qrels={}
def read_qrels(doc_ids,):
    #qrels={}
    for qrel in dataset.qrels_iter():
        doc = {"doc_id": qrel.doc_id, "relevance": qrel.relevance}
        if qrel.doc_id in doc_ids:
            if qrel.query_id in qrels:
                qrels[qrel.query_id].append(doc)
            else:
                qrels[qrel.query_id] = [doc]
    return  qrels

def read_dataset_ar():
    global corpus_ar

    with open('../data_set/wiki_ar.documents', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    # with open('../data_set/wiki_ar.documents', 'r') as file:
    #      lines= csv.reader(file)

    for line in lines:
        line = line.strip()
        parts = line.split(' ', 1)
        doc_id = int(parts[0])
        doc_text = parts[1]
        corpus_ar[doc_id]= doc_text
    # for row in corpus_ar:
    #         # تنفيذ العمليات المطلوبة على كل صف (row)
    #     print(row)  #
    print(corpus_ar)
    return corpus_ar

def read_dataset():
    global qrels
    global corpus
    global queries
    for doc in dataset.docs_iter():
        corpus[doc.doc_id]=doc.text
        #fetch limit from dataset
        #if(int(doc.doc_id)>110000):
        if(int(doc.doc_id)>60000):
        #if(int(doc.doc_id)>60):
            break
    for query in dataset.queries_iter():
        queries[query.query_id]=query.text
    for qrel in dataset.qrels_iter():
        doc={"doc_id": qrel.doc_id, "relevance": qrel.relevance}
        if qrel.query_id in qrels:
            qrels[qrel.query_id].append(doc)
        else:
            qrels[qrel.query_id]=[doc]
    return corpus    
   # doc # namedtuple<doc_id, text>