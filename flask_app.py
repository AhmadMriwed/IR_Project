from flask import Flask, render_template, request

from data_source.model import  corpus
from data_source.model import  corpus_ar
from data_source.model import  online
import configoration.configoration as conf

app = Flask(__name__)



# دالة البحث
def search(query,corpus):
    #doc_ids= ["1","2","3","4",'5','6','7','8','9','10','318','555','55']
    doc_ids= online({"query":query})
    result = [corpus[dco_id] for dco_id in doc_ids if dco_id in corpus]
    return result

# الصفحة الرئيسية للبحث
@app.route('/')
def home():
    return render_template('search.html')

# صفحة استرجاع النتائج
@app.route('/search', methods=['POST'])
def search_page():

    query = request.form['query']
    print('query : '+f"{query}")
    selected_dataset = request.form['dataset']
    conf.change_language(selected_dataset)

    documents = search(query, conf.get_by_language(corpus,corpus_ar))
    print(documents)
    return render_template('results.html',)
    return render_template('results.html')

def run():
    #if __name__ == '__main__':
        app.run()
