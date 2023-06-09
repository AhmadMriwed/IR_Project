
import ir_datasets
dataset = ir_datasets.load("beir/quora/dev")
#dataset = ir_datasets.load("beir/quora")
# with open('../data_set/topic.dev.tsv', 'r') as file:
#     topic = file.read()
# dataset1 = ir_datasets.create_dataset(topic)
corpus={}
corpus_ar={}
queries={}
qrels={}
#print(len( list(dataset.qrels_iter())))
# print(len( list(dataset1.docs_iter())))
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

    # with open('../data_set/topic.dev.tsv', 'r', encoding='utf-8') as file:
    #     lines = file.readlines()

    with open('../data_set/wiki_ar.documents', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    i=0
    for line in lines:
        if (i > 100000):
            break
        parts = line.split('\t', 1)
        if(len(parts)==2):
            i+=1
            doc_id = parts[0]
            doc_text = parts[1]
            corpus_ar[doc_id]= doc_text

    #print(f"data_set ar : {len(corpus_ar)}")
    return corpus_ar

def read_dataset():


    global qrels
    global corpus
    global queries
    for doc in dataset.docs_iter():
        corpus[doc.doc_id]=doc.text
        #fetch limit from dataset
        #if(int(doc.doc_id)>110000):
        if(int(doc.doc_id)>100000):
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