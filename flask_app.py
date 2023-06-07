from flask import Flask, render_template, request
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

app = Flask(__name__)

dataset1 = {
    1: 'This is document 1',
    2: 'Another document here',
    3: 'Some more text in document 3'
}

dataset2 = {
    4: 'Document number 4',
    5: 'Text in document 5',
    6: 'Yet another document',
    7:"yet lsnvlnlsndv",
    8:"yetasvsdvsdv",
    9:"yet svdlknlsdv",
    10:"yet aslvknapikanslcknalknSKNDVLNLKNSVD",
    11:"ahmad eat apple",
    12:"yetSDVSD;VKNSV",
    13:"welcome to damascus",
    14:"yet SALDVKNSV",
    15:"i play football",
    16:"yet SVDLM",
    17:"yet played",
    18:"i love swimming",
    100:"ahmad hello my name is ahmad ahmad",
    200:"ahmad hello my name is ahmad ahmad",
    114:"ahmad hello my name is ahmad ahmad",
    233:"ahmad hello my name is ahmad ahmad",
    242:"ahmad hello my name is ahmad ahmad",
    1129:"ahmad hello my name is ahmad ahmad",
    139:"ahmad hello my name is ahmad ahmad",
    149:"ahmad hello my name is ahmad ahmad",
    1669:"ahmad hello my name is ahmad ahmad",
    17759:"ahmad hello my name is ahmad ahmad",
    15569:"ahmad hello my name is ahmad ahmad",
    1789:"ahmad hello my name is ahmad ahmad",
    1999:"ahmad hello my name is ahmad ahmad",
    179:"ahmad hello my name is ahmad ahmad",
    20:"yet",
    21:"Flutter is Strong Technology in mobile app devlopment",
    22:"yet",
    23:"Kotlin is framework is build in java programming langiuage",
    24:"yet",
    25:"damascus university is complex system",
    26:"yet",
    27:"yestarday i eat meet",
    28:"my book is very expinsive",
    29:"ahmad alhariri",
    30:"hello can arrow yet",
    31:"batman is nice move yet",
    32:"iam strong man",
}

# بناء الفهرس
index = {}
for doc_id, document in dataset1.items():
    words = document.lower().split()
    for word in words:
        if word not in index:
            index[word] = set()
        index[word].add(doc_id)

for doc_id, document in dataset2.items():
    words = document.lower().split()
    for word in words:
        if word not in index:
            index[word] = set()
        index[word].add(doc_id)

# دالة البحث
def search(query, selected_dataset):
    query_words = query.lower().split()
    result = set()
    dataset = dataset1 if selected_dataset == 'dataset1' else dataset2
    for doc_id, document in dataset.items():
        words = document.lower().split()
        for word in query_words:
            if word in words:
                result.add(doc_id)
    return result

# تضليل الكلمة المبحوث عنها
def highlight_word(text, query):
    query_tokens = word_tokenize(query.lower())
    stemmed_query_tokens = [PorterStemmer().stem(token) for token in query_tokens]
    text_tokens = word_tokenize(text.lower())
    highlighted_tokens = []
    for token in text_tokens:
        stemmed_token = PorterStemmer().stem(token)
        if stemmed_token in stemmed_query_tokens:
            highlighted_tokens.append('<span class="highlight">' + token + '</span>')
        else:
            highlighted_tokens.append(token)
    highlighted_text = ' '.join(highlighted_tokens)
    return highlighted_text

# الصفحة الرئيسية للبحث
@app.route('/')
def home():
    return render_template('search.html')

# صفحة استرجاع النتائج
@app.route('/search', methods=['POST'])
def search_page():
    print('query')
    query = request.form['query']

    selected_dataset = request.form['dataset']

    matching_documents = search(query, selected_dataset)
    documents = []
    dataset = dataset1 if selected_dataset == 'dataset1' else dataset2

    for doc_id in matching_documents:
        if doc_id in dataset:
            document = dataset[doc_id]
            highlighted_document = highlight_word(document, query)
            documents.append(highlighted_document)
    # return render_template('results.html', query=query, documents= documents)
    return render_template('results.html')

if __name__ == '__main__':
    app.run()
