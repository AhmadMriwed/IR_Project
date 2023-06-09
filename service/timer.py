import time

from nltk.tokenize import sent_tokenize, word_tokenize

#tokenized_corpus = {}

#rom farasa.segmenter import FarasaSegmenter
from configoration import configoration
start_time=time.time()
def st():
    global start_time
    start_time = time.time()
def ed():
    end_time = time.time()
    execution_time = end_time - start_time
    print("execution time :",  round(execution_time, 2), "s")
def timer(fun):
    start_time=time.time()
    fun
    end_time=time.time()
    execution_time = end_time - start_time
    print("execution time :", execution_time, "s")










 