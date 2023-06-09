from data_source import docs
from evaluation import evaluation as ev

from service import store_file
qrels={}


def get_result_queries(queries):
    from online import app_query
    # result_queries=app_query.prmr(queries)
    result_queries=app_query.prmr2(queries)
    return result_queries

def get_recall_queries(result_queries,qrels):
    recall_queries={}
    for key in result_queries.keys():
        if(key in qrels.keys()):
            relevant_documents = [item['doc_id'] for item in qrels[key]]
            recall_queries[key]=ev.calculate_recall(result_queries[key],relevant_documents)
    return  recall_queries

def get_precision_queries(result_queries,qrels):
    precision_queries={}
    for key in result_queries.keys():
        if(key in qrels.keys()):
            relevant_documents = [item['doc_id'] for item in qrels[key]]
            precision_queries[key]=ev.calculate_precision(result_queries[key],relevant_documents)
    return  precision_queries

def get_precision_at_10_queries(result_queries,qrels):
    precision_queries_at_k={}
    for key in result_queries.keys():
        if(key in qrels.keys()):
            relevant_documents = [item['doc_id'] for item in qrels[key]]
            precision_queries_at_k[key]=ev.calculate_precision_at_k(result_queries[key],relevant_documents)
    return  precision_queries_at_k

def get_average_precision_queries(result_queries,qrels):
    average_precision_queries={}
    for key in result_queries.keys():
        if(key in qrels.keys()):
            relevant_documents = [item['doc_id'] for item in qrels[key]]
            average_precision_queries[key]=ev.calculate_average_precision(result_queries[key],relevant_documents)
    return  average_precision_queries


def get_mean_average_precision(average_precision_queries):
    mean_average_precision=0.0
    average_precisions = [value for value in average_precision_queries.values()]
    mean_average_precision=ev.calculate_mean_average_precision(average_precisions)
    return  mean_average_precision

def get_mean_reciprocal_rank(result_queries,qrels):
    mean_reciprocal_rank=0.0
    results_queries=[]
    relevants_documents=[]
    for key in result_queries.keys():
        if(key in qrels.keys()):
            results_queries.append(result_queries[key])
            relevants_documents.append([item['doc_id'] for item in qrels[key]])

    mean_reciprocal_rank=ev.calculate_mean_reciprocal_rank(results_queries,relevants_documents)
    return  mean_reciprocal_rank



def get_evaluation(result_queries,qrels):
    print("=============================================")
    print("==                 Evaluation              ==")
    print("=============================================")
    recall_queries = get_recall_queries(result_queries, qrels)
    store_file.creat_file_from_map(store_file.path_recall_queries, recall_queries)
    print("Done recall queries")

    precision_queries = get_precision_queries(result_queries, qrels)
    store_file.creat_file_from_map(store_file.path_precision_queries, precision_queries)
    print("Done precision queries")

    path_precision_at_k_queries = get_precision_at_10_queries(result_queries, qrels)
    store_file.creat_file_from_map(store_file.path_precision_at_k_queries, path_precision_at_k_queries)
    print("Done precision@10 queries")

    average_precision_queries = get_average_precision_queries(result_queries, qrels)
    store_file.creat_file_from_map(store_file.path_average_precision_queries, average_precision_queries)
    print("Done average precision queries")

    mean_average_precision = get_mean_average_precision(average_precision_queries)
    store_file.creat_file(store_file.path_mean_average_precision_queries, str(mean_average_precision))
    print("Done mean average precision queries")

    mean_reciprocal_rank = get_mean_reciprocal_rank(result_queries, qrels)
    store_file.creat_file(store_file.path_mean_reciprocal_rank_queries, str(mean_reciprocal_rank))
    print("Done mean_reciprocal_rank queries")

def evaluation():
    global qrels
    qrels = docs.read_qrels(docs.corpus.keys())
    # get queries rank
    # (query_id)318 : (doc_ids)3[123,13,45,...]
    result_queries=get_result_queries(docs.queries)
    get_evaluation(result_queries,qrels)

# result_queries={'318':['11', '38', '12', '33', '45', '37', '55', '41', '34', '49'],
# '378':['61', '22'],
# '379':[],
# '399':[],
# '420':['35', '38', '37', '55', '41', '42', '7'],
# '540':['20'],
# '548':['43', '36', '45', '44', '38', '37'],
# '609':['58', '39', '57', '40'],
# '744':['43', '44'],
# '784':['35', '60', '38', '61', '9', '37', '41', '42', '7'],
# '858':['4', '10', '61', '31'],
# '975':['60', '51', '40', '52', '39', '59', '58', '57'],
# '1079':['61', '15'],
# '1088':['11', '61', '27', '36', '12', '33', '55', '34', '49'],
# '1164':['32', '31'],
# '1166':['26', '25'],
# '1248':['37', '38', '45'],
# '1350':[],
# '1453':[],
# '1578':[],
# '1803':['23', '24'],
# '1956':['37', '52', '38', '51'],
# '1992':['5', '17', '18', '21', '7'],
# '2004':['10', '61', '4', '43', '31'],
# '2145':['20'],
# '2254':[],
# '2429':['35', '36'],
# '2615':['30', '22', '51', '32', '8', '29', '52', '31'],
# '2658':['37', '38', '45'],
# '2661':[],
# '2678':['38'],
# '2757':[],
# '2785':[],
# '2791':[],
# '2822':[],
# '2824':[],
# '3017':['35', '38', '37', '41', '42', '7'],
# '3076':['11', '43', '12'],
# '3322':['52', '29', '30', '51'],
# '3459':['5', '18', '21', '17'],
# '3521':[],
# '3581':[],
# '3594':['58', '39', '57', '40'],
# '3612':['51', '60', '38', '37', '52', '59'],
# '3796':[],
# '3959':['51', '48', '8', '52', '23', '21'],
# '4105':[],
# '4298':[],
# '4356':[],
# '4584':['58', '5', '17', '18', '37', '21', '38', '45'],
# '4874':['55', '47'],
# '4974':['5', '18', '21', '17'],
# '5040':[],
# '5162':['4'],
# '5319':['14', '23'],
# '5498':['1', '38'],
# '5516':['35', '38', '37', '41', '42', '7'],
# '5647':[],
# '5799':[],
# '5851':['42'],
# '6021':['29', '30'],
# '6022':['4', '29', '30'],
# '6055':[],
# '6209':['1', '28', '27'],
# '6244':['58', '39', '57', '40'],
# '6253':['61', '27'],
# '6276':[],
# '6483':[],
# '6588':[],
# '6786':[],
# '6936':['35', '38', '36', '37', '41', '42', '7'],
# '6957':['11', '12', '33', '55', '34', '49'],
# '7105':[],
# '7222':[],
# '7301':['11', '12', '33', '55', '34', '49'],
# '7319':[],
# '7372':['32', '31'],
# '7396':['58', '39', '57', '40'],
# '7463':['5', '18', '21', '17'],
# '7614':[],
# '7616':['58', '26', '20', '57', '40', '25', '6', '19', '39'],
# '7822':['35', '11', '4', '12', '37', '41', '42', '7', '38'],
# '7841':['29', '30'],
# '7957':[],
# '7988':[],
# '8055':['11', '12', '33', '55', '34', '49'],
# '8306':['26', '58', '51', '25', '52', '57'],
# '8456':['38'],
# '8458':['61', '27'],
# '8482':[],
# '8808':['35', '41', '32', '61', '38', '1', '15', '37', '31', '42', '7'],
# '8810':['5', '28', '51', '47', '27', '6', '52', '55'],
# '8831':['26', '40', '25', '39', '58', '57'],
# '8950':['11', '12', '33', '31', '34', '49'],
# '9214':['14'],
# '9294':['11', '12', '33', '55', '34', '49'],
# '9312':['26', '51', '57', '25', '52', '23'],
# '9340':['35', '20', '5', '38', '6', '37', '41', '42', '7'],
# '9376':[],
# '9602':['58', '51', '37', '52', '38', '45'],
# '9615':['30', '29', '59', '32', '31'],
# '9658':['11', '60', '61', '9', '12', '33', '55', '34', '49'],
# '9733':['55'],
# '9889':['35', '11', '30', '38', '29', '12', '33', '49', '37', '41', '34', '42', '7', '55'],
# '9965':['39', '40', '58', '57'],
# '10024':[],
# '10113':[],
# '10155':['5', '18', '21', '17'],
# '10188':[],
# '10453':['35', '37', '41', '42', '7', '38'],
# '10648':[],
# '10722':['11', '1', '12', '33', '55', '34', '49'],
# '10810':['26', '51', '57', '25', '52'],
# '10889':['58', '39', '57', '40'],
# '10910':['28', '22', '61', '27', '4'],
# '11009':['10', '61', '38', '4', '31'],
# '11037':['1', '61', '15'],
# '11167':['4', '5', '6'], }
