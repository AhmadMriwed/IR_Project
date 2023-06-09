from configoration import  configoration
from service import  cluster
from service import store_file
clusters=[]
def cluster_app(documents):
    global clusters
    if not configoration.cluster_exc:
        return clusters
    clusters =cluster.cluster(documents)
    print("************** Done Clustering **************")
    store_file.creat_file_from_list(store_file.path_cluster,clusters)
    return clusters

