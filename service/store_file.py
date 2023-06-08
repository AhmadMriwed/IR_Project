import json
path_dir_out="../out/"
path_dir_out_preprocessing=path_dir_out+"out_preprocessing/"
path_dir_out_representation=path_dir_out+"out_representation/"
path_dir_out_query_processing=path_dir_out+"query_processing/"
path_dir_out_query_representation=path_dir_out+"query_representation/"
path_dir_out_query_matching=path_dir_out+"query_matching/"
path_dir_out_evaluation=path_dir_out+"out_evaluation/"
#out_preprocessing
path_tokenize=path_dir_out_preprocessing+"tokenize.txt"
path_punctuation=path_dir_out_preprocessing+"punctuation.txt"
path_stemming=path_dir_out_preprocessing+"stemming.txt"
path_lemmatize=path_dir_out_preprocessing+"lemmatize.txt"
path_stopwords=path_dir_out_preprocessing+"stopwords.txt"
path_duplicated=path_dir_out_preprocessing+"duplicated.txt"
path_cluster=path_dir_out_preprocessing+"cluster.txt"

#out_representation
path_inverted_index=path_dir_out_representation+"inverted_index.txt"
path_tf_df=path_dir_out_representation+"tf_df.txt"
path_tfidf_df=path_dir_out_representation+"tfidf_df.txt"

#query_processing
path_query=path_dir_out_query_processing+"query.txt"
path_tokenize_q=path_dir_out_query_processing+"tokenize.txt"
path_punctuation_q=path_dir_out_query_processing+"punctuation.txt"
path_stemming_q=path_dir_out_query_processing+"stemming.txt"
path_lemmatize_q=path_dir_out_query_processing+"lemmatize.txt"
path_stopwords_q=path_dir_out_query_processing+"stopwords.txt"
path_duplicated_q=path_dir_out_query_processing+"duplicated.txt"

#query_representation
path_inverted_index_q=path_dir_out_query_representation+"inverted_index.txt"
path_tf_df_q=path_dir_out_query_representation+"tf_df.txt"
path_tfidf_df_q=path_dir_out_query_representation+"tfidf_df.txt"

#query_matching
path_query_matching=path_dir_out_query_matching+"query_matching.txt"
path_query_rank=path_dir_out_query_matching+"query_rank.txt"

#evaluation
path_recall_queries=path_dir_out_evaluation+"recall_queries.txt"
path_precision_queries=path_dir_out_evaluation+"precision_queries.txt"
path_precision_at_k_queries=path_dir_out_evaluation+"precision@10_queries.txt"
path_average_precision_queries=path_dir_out_evaluation+"average_precision_queries.txt"
path_mean_average_precision_queries=path_dir_out_evaluation+"mean_average_precision_queries.txt"
path_mean_reciprocal_rank_queries=path_dir_out_evaluation+"mean_reciprocal_rank_queries.txt"





def creat_file_dataframe(file_path,df):
    with open(file_path, 'w', 1024, "utf-8") as file:
        for key, value in map.items():
            text = f"{key}:{value}, \n"
            file.writelines(text)
    df.to_csv('output.txt', '\t', False)
def creat_file(file_path,text):
    with open(file_path,'w',1024,"utf-8") as file:
        file.write(text)
def creat_file_from_map(file_path,map):
    with open(file_path,'w',1024,"utf-8") as file:
        for key, value in map.items():
            text = f"{key}:{value}, \n"
            file.writelines(text)
def creat_file_from_list(file_path,list):
    with open(file_path,'w',1024,"utf-8") as file:
        for value in list:
            text = f"{value} \n\n"
            file.writelines(text)





def convert_list_to_text(list):
    text = ""
    for item in list:
        text+=f"{item}, \n"
    return text

def convert_map_to_text(map):
    text = ""
    for key, value in map.items():
        text+=f"{key}:{value}, \n"
    return text

def convert_map_to_text_limit(map,limit):
    text = ""
    for value in list(map.items())[:limit]:
        text+=f"{value}, \n"
    return text


