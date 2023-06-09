import gc

from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

# في حال عدم وضع K عندها يأخذ عدد الوثائق ويقسم على 3
def cluster(documents,k=0):

    # # قم بتحضير المستندات
    # documents = {
    #    "1": "What is the step by step guide to invest in share market in india?",
    #    "2" :"What is the step by step guide to invest in share market?",
    #    "3": "What is the story of Kohinoor (Koh-i-Noor) Diamond?",
    #    "4":"What would happen if the Indian government stole the Kohinoor (Koh-i-Noor) diamond back?",
    #     "5":"How can I increase the speed of my internet connection while using a VPN?",
    #     "6": "How can Internet speed be increased by hacking through DNS?",
    #     "7": "Why am I mentally very lonely? How can I solve it?",
    #     "8": "Find the remainder when [math]23^{24}[/math] is divided by 24,23?",
    #     "9": "Which one dissolve in water quikly sugar, salt, methane and carbon di oxide?",
    #     "10": "Which fish would survive in salt water?"
    # }
  # عدد العناقيد المطلوبة
    if k <= 0:
        k = int(len(documents)/3)
    if k>5:
        k=5
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform( documents.values())
    # قم بتطبيق تقنية K-means لتجميع المستندات
    kmeans = KMeans(k)
    kmeans.fit(X)

    # استخراج المستندات في كل عنقود
    clusters = kmeans.labels_
    clusters_docs=[]
    for i in range(k):
        cluster_docs = [key for j,key in zip(range(len(documents.keys())),documents.keys()) if clusters[j] == i]
        clusters_docs.append(cluster_docs)
        # print(f"Cluster {i + 1}:")
        # print(cluster_docs)
        # print()
    del    vectorizer,X,kmeans
    gc.collect()
    return  clusters_docs


# def cluster():
#     # قم بتحضير المستندات
#     documents = {
#        "1": "What is the step by step guide to invest in share market in india?",
#        "2" :"What is the step by step guide to invest in share market?",
#        "3": "What is the story of Kohinoor (Koh-i-Noor) Diamond?",
#         "4":"What would happen if the Indian government stole the Kohinoor (Koh-i-Noor) diamond back?",
#         "5":"How can I increase the speed of my internet connection while using a VPN?",
#                     "6": "How can Internet speed be increased by hacking through DNS?",
#                     "7": "Why am I mentally very lonely? How can I solve it?",
#                     "8": "Find the remainder when [math]23^{24}[/math] is divided by 24,23?",
#         "9": "Which one dissolve in water quikly sugar, salt, methane and carbon di oxide?",
#         "10": "Which fish would survive in salt water?"
#     }
#     # documents=[
#     #     ['step', 'step', 'guid', 'invest', 'share', 'market', 'india'],
#     #  ['step', 'step', 'guid', 'invest', 'share', 'market'],
#     #  ['stori', 'kohinoor', 'koh-i-noor', 'diamond'],
#     #  ['would', 'happen', 'indian', 'govern', 'steal', 'kohinoor', 'koh-i-noor', 'diamond', 'back'],
#     #  ['increas', 'speed', 'internet', 'connect', 'use', 'vpn'],
#     #  ['internet', 'speed', 'increas', 'hack', 'dn'],
#     #  ['mental', 'veri', 'lone', 'solv'],
#     #  ['find', 'remaind', 'math', '23^', '24', '/math', 'divid', '24,23'],
#     #  ['one', 'dissolv', 'water', 'quikli', 'sugar', 'salt', 'methan', 'carbon', 'di', 'oxid'],
#     #     ['fish', 'would', 'surviv', 'salt', 'water']
#     # ]
#     # قم بتحويل المستندات إلى تمثيل رقمي باستخدام TfidfVectorizer
#     vectorizer = TfidfVectorizer()
#     X = vectorizer.fit_transform( documents.values())
#     print(X)
#     # قم بتطبيق تقنية K-means لتجميع المستندات
#     k = 3  # عدد العناقيد المطلوبة
#     kmeans = KMeans(n_clusters=k)
#     kmeans.fit(X)
#
#     # استخراج المستندات في كل عنقود
#     clusters = kmeans.labels_
#     for i in range(k):
#         cluster_docs = [documents[key] for j,key in zip(range(len(documents.keys())),documents.keys()) if clusters[j] == i]
#         print(f"Cluster {i + 1}:")
#         for doc in cluster_docs:
#             print(doc)
#         print()
