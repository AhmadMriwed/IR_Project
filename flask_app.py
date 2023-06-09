from flask import Flask, render_template, request, jsonify
from data_source.model import corpus, online
from data_source.model import  corpus_ar
import configoration.configoration as conf

app = Flask(__name__)


result=[]
# دالة البحث
def search(query,corpus):
    global result
    #doc_ids= ["1","2","3","4",'5','6','7','8','9','10','318','555','55']
    doc_ids= online(query={"query":query},language_code=conf.language_code)
    result = [corpus[dco_id] for dco_id in doc_ids if dco_id in corpus]
    return result

# الصفحة الرئيسية للبحث
@app.route('/')
def home():
    return render_template('search.html')

# صفحة استرجاع النتائج
# @app.route('/search', methods=['POST'])
# def search_page():
#
#     query = request.form['query']
#     print('query : '+f"{query}")
#     selected_dataset = request.form['dataset']
#     conf.change_language(selected_dataset)
#     documents = search(query, conf.get_by_language(corpus,corpus_ar))
#     print(documents)
#     #return render_template('results.html',)
#     return render_template('results.html',documents=documents,selected_dataset=selected_dataset)

# صفحة استرجاع النتائج
@app.route('/search', methods=['POST'])
def search_page():

    query = request.form['query']
    #print('query : '+f"{query}")
    if('dataset' in request.form):
        selected_dataset = request.form['dataset']
    else:
        selected_dataset=conf.language_code
    conf.change_language(selected_dataset)
    documents = search(query, conf.get_by_language(corpus,corpus_ar))
    #print(documents)
    return render_template('results.html',query=query, my_list=documents,selected_dataset=selected_dataset)
    #return render_template('results.html',documents=documents,selected_dataset=selected_dataset)

@app.route('/data')
def data():
   # my_list = ['عنصر 1', 'عنصر 2', 'عنصر 3', 'عنصر 4', 'عنصر 5', 'عنصر 6', 'عنصر 7', 'عنصر 8', 'عنصر 9', 'عنصر 10']
    return jsonify(result)
def run():
    #if __name__ == '__main__':
        app.run()
