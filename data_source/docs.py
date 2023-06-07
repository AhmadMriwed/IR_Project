import ir_datasets
dataset = ir_datasets.load("beir/quora/dev")
#dataset = ir_datasets.load("beir/quora")
#dataset = ir_datasets.load("wikiclir/ar")
corpus={}
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