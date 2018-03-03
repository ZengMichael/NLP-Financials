''' Read Data with basic cleanning'''
import pickle

articles = pickle.load(open('articles.pickle', 'rb'))       # Read
corpus = [t for inner in articles for t in inner]           # Simple LIST
corpus = [document.replace('\n',' ') for document in corpus]# Remove '\n'



'''data cleaning processes 1'''
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords

def lemmatize(token, tag):
    if tag[0].lower() in ['n', 'v']:
        return WordNetLemmatizer().lemmatize(token, tag[0].lower())
    return token

corpus_tokens_lemmatization = []
for document in corpus:
    document_tokens = []
    for sentence in sent_tokenize(document)[1:]:# The first sentence is useless for analysis
        tagged_sentence = pos_tag(word_tokenize(sentence)) #1.tokenization 2.pos_tag:extremely useful
        sentence_tokens = [lemmatize(token.lower(), tag) for token, tag in tagged_sentence if token.isalpha()]#1.lemmatize 2.lower case 3.isalpha
        sentence_tokens = [term for term in sentence_tokens if term not in stopwords.words('english')]  # Remove Stop Words)
        document_tokens.extend(sentence_tokens)
    corpus_tokens_lemmatization.append(document_tokens)



'''data cleaning processes 2 - stemming'''
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize,word_tokenize
corpus_tokens_stemming = [  [PorterStemmer().stem(term) for term in document]
                             for document in corpus_tokens_lemmatization]






'''Below Codes for Saving'''
def Save_pickle(corpus_tokens_lemmatization,corpus_tokens_stemming):
    pickle.dump(corpus_tokens_lemmatization,open('corpus_tokens_lemmatization.pickle','wb'))
    pickle.dump(corpus_tokens_stemming,open('corpus_tokens_stemming.pickle','wb'))


