# This script illustrates how to use tf-idf with gensim.
from nltk.tokenize import word_tokenize
from gensim.corpora.dictionary import Dictionary
from gensim.models.tfidfmodel import TfidfModel
corpus = ['Yao is a great basketball player',
          'Kobe is a great basketball player too',
            "I like basketball very much",
            "I like football very much",
            "I also play tennis"]
"""
myStr=""
for i in corpus:
    myStr+=i
print(myStr)
myCorpus=[myStr]
print(myCorpus)
tokenized_corpus = [word_tokenize(doc.lower()) for doc in myCorpus]
"""
numOfWeight=3 #在这里改每句话输出权重的最多数量

tokenized_corpus = [word_tokenize(doc.lower()) for doc in corpus]
d = Dictionary(tokenized_corpus)
#print(d)
bowcorpus = [d.doc2bow(doc) for doc in tokenized_corpus]
#print(bowcorpus)
# All the above steps are standard, but now it gets interesting:
tfidf = TfidfModel(bowcorpus) # Create new TfidfModel from BoW corpus.
#print(tfidf[bowcorpus[0]])
#tfidf_weights = tfidf[bowcorpus[0]] # Weights of first document.
for i in range(len(bowcorpus)):
    tfidf_weights = tfidf[bowcorpus[i]]
    #print(tfidf_weights)
    sorted_tfidf_weights = sorted(tfidf_weights, key=lambda x: x[1], reverse=True)
    #print(sorted_tfidf_weights)
    print("\n")
    for term_id, weight in sorted_tfidf_weights[:numOfWeight]:
        print(d.get(term_id), weight)
#tfidf_weights[:5]                   # First five weights (unordered).
 # Print top five weighted words.
#sorted_tfidf_weights = sorted(tfidf_weights, key=lambda x: x[1], reverse=True)
#for term_id, weight in sorted_tfidf_weights[:5]:
#    print(d.get(term_id), weight)
