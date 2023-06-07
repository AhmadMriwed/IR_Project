recall =0.0
average_precision =0.0
precision =0.0
min_ir =0.0
mrr =0.0

# find true positive
def find_tp(result_docs,relevant_documents):
    tp=[doc for doc in result_docs if doc in relevant_documents]
    return tp
#relevant_documents=[1,2,3,4,5,6,7,8]
#result_docs=[1,3,4,9,10]
#tp=[1,3,4]
#recall= len(tp)/len(relevant_documents)
#recall= 3/8
def calculate_recall(result_docs,relevant_documents):
    global recall
    tp=find_tp(result_docs,relevant_documents)
    tp_count=len(tp)
    trd_count=len(relevant_documents)
    if trd_count == 0:
        trd_count=1
    recall=tp_count/trd_count
    return  recall

#relevant_documents=[1,2,3,4,5,6,7,8]
#result_docs=[1,3,4,9,10]
#tp=[1,3,4]
#average_precision=  0.3333333333333333
def calculate_average_precision(result_docs, relevant_documents,k=10):
    global average_precision
    precision_sum = 0.0
    relevant_count = 0
    sub_result_docs = result_docs
    if len(sub_result_docs) > k:
        sub_result_docs = result_docs[:k]

    for i, document in enumerate(sub_result_docs):
        if document in relevant_documents:
            relevant_count += 1
            precision_sum += relevant_count / (i + 1)

    if relevant_count == 0:
        return 0.0

    average_precision = precision_sum / relevant_count
    return average_precision
#relevant_documents=[1,2,3,4,5,6,7,8]
#result_docs=[1,3,4,9,10]
#tp=[1,3,4]
#precision= len(tp)/len(result_docs)
#precision= 3/5

def calculate_precision(result_docs, relevant_documents):
    global  precision
    retrieved_docs_count = len(result_docs)
    if  retrieved_docs_count == 0:
        retrieved_docs_count=1
    retrieved_relevant_docs_count = len(set(relevant_documents) & set(result_docs))
    precision = retrieved_relevant_docs_count / retrieved_docs_count
    return precision

def calculate_precision_at_k(result_docs, relevant_documents, k=10):
    sub_result_docs=result_docs
    if len(sub_result_docs) > k:
        sub_result_docs = result_docs[:k]
    correct = len(set(relevant_documents) & set(sub_result_docs))
    precision_at_k = correct / k
    return precision_at_k


def calculate_mean_average_precision(average_precisions):
    if(len(average_precisions)==0):
        mean_average_precision=0
    else:
        mean_average_precision = sum(average_precisions) / len(average_precisions)
    return mean_average_precision





# Example usage
#results = [2, 3, 1]
#mrr= 0.44444

#ranks = [1, 0, 3, 0, 2]
#reciprocal_ranks = [1 / 1, 1 / 3, 1 / 2] = [1.0, 0.3333333333333333, 0.5]
#mrr 0.611111111111111

#ranks = [3, 1, 1, 2, 1]
#reciprocal_ranks = [1 / 3, 1 / 1, 1 / 2, 1 / 1] = [0.3333333333333333, 1.0, 0.5, 1.0]
#mrr = (0.3333333333333333 + 1.0 + 0.5 + 1.0) / 4 = 0.7083333333333334


def calculate_reciprocal_rank(actual, predicted):
    for i, doc in enumerate(predicted):
        if doc in actual:
            return 1.0 / (i + 1)
    return 0.0

# Mean Reciprocal Rank
def calculate_mean_reciprocal_rank(results_docs, relevants_documents):
    reciprocal_ranks = []
    reciprocal_ranks_count= len(reciprocal_ranks)
    if(reciprocal_ranks_count==0):
        return 0
    for i in range(len(relevants_documents)):
        reciprocal_rank_value = calculate_reciprocal_rank(relevants_documents[i], results_docs[i])
        reciprocal_ranks.append(reciprocal_rank_value)
    mean_reciprocal_rank = sum(reciprocal_ranks) / len(reciprocal_ranks)
    return mean_reciprocal_rank

# Mean Reciprocal Rank
def calculate_mrr(results):
    global  mrr
    reciprocal_ranks = []
    for rank in results:
        reciprocal_rank = 1 / rank
        reciprocal_ranks.append(reciprocal_rank)
    mrr = sum(reciprocal_ranks) / len(reciprocal_ranks)
    return mrr

