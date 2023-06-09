from sklearn.metrics.pairwise import cosine_similarity

#Example
#query = [query_doc]

# عيّن قائمة المجموعات وقائمة الاستعلامات
# clusters = [
#     [doc1, doc2, doc3],  # مجموعة 1
#     [doc4, doc5],  # مجموعة 2
#     [doc6, doc7, doc8, doc9]  # مجموعة 3
# ]
from configoration import configoration


def search_cluster_by_s(inverted_index,clusters,query,s=1):
    if not configoration.cluster_exc:
        return  inverted_index

    selected_cluster=select_cluster_by_s(clusters,query,s)
    for key,value in inverted_index.items():
        inverted_index[key]=list(set(value) & set(selected_cluster))
    return inverted_index


# s=1 :  select_cluster_by_size
# s=2 :  select_cluster_by_similarity_measure

def select_cluster_by_s(clusters,query,s=1):
    if s==1:
        return select_cluster_by_size(clusters)
    elif s==2:
        # for i in range(len(clusters)):
        #     clusters[i]=[corpus[key] for key in list(set(clusters[i]) & set(corpus.keys()))]
        return select_cluster_by_similarity_measure(clusters,query)
    else:
        return clusters[0]

def select_cluster_by_size(clusters):

    # حسب حجم المجموعة لاختيار المجموعة المناسبة
    selected_cluster = max(clusters, key=len)
    # # قم بطباعة المجموعة المناسبة
    # print("Selected Cluster:", selected_cluster)
    return selected_cluster


def select_cluster_by_similarity_measure(clusters,query):

    # حسب التشابه بين الاستعلام وكل مجموعة
    similarities = [cosine_similarity(query, cluster)[0][0] for cluster in clusters]

    # احصل على المجموعة التي تحقق أعلى درجة تشابه
    max_similarity_index = similarities.index(max(similarities))
    selected_cluster = clusters[max_similarity_index]

    # # قم بطباعة المجموعة المناسبة
    # print("Selected Cluster:", selected_cluster)
    return  selected_cluster