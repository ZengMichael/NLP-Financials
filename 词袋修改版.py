# Bag-of-words using gensim.
from gensim.corpora.dictionary import Dictionary
from nltk.tokenize import word_tokenize
# This is an example corpus consisting of movie reviews. You can think
# of each movie review as a separate text document.
mycorpus = ['My name is van',
            'I am an artist',
            'A performance artist',"I am hired for people to fulfill their fantasies, their deep dark fantasies"]

# Very basic preprocessing. Usually you would do more work here.
tokenized_corpus = [word_tokenize(doc.lower()) for doc in mycorpus]

# Pass to gensim `Dictionary` class. This assigns to each token
# (e.g. word) a unique integer ID. Later on we will just work with
# those IDs instead of the tokens directly because it is
# computationally easier to handle (there is a one-to-one mapping
# between both, so we are not losing any information). The reason why
# we use a dictionary is that it gives us a list of words we are
# interested in examining further. If a word is not in the dictionary
# but occurs in a document, it will be ignored by gensim.
d = Dictionary(tokenized_corpus)
d.token2id  # Like dict(d); show mapping between tokens and their IDs.
d.token2id.get('awesome')       # What's the ID for 'awesome'?
d.get(0)                        # What token has ID=0?
d.dfs # In how many documents does each token appear? (Document frequency).

for i in d:print(i,d[i])
# For a single document, we can now calculate the token frequencies
# using the dictionary we just created. "Calculating token
# frequencies" means we're counting words.
#d.doc2bow(tokenized_corpus[2])
#print(d.doc2bow(tokenized_corpus[2]))

# Next, using the dictionary we just created, we build a gensim
# corpus, which is just a bag-of-words representation of the original
# corpus. This is a nested list (a list of lists), where each list
# corresponds to a document. Inside each list we have tuples in the
# form (token_ID, token_frequency). So all we are really doing here is
# counting words.
gcorpus = [d.doc2bow(doc) for doc in tokenized_corpus]

# This gensim corpus can now be saved, updated, and reused using tools
# from gensim. The dictionary can also be saved and updaed as well,
# e.g. if we need to add more words later on.

# Print the first three token IDs and their frequency counts from the
# first document.
#gcorpus[0][:3]
#print(gcorpus)
# For the first document, sort the tokens according to their
# frequency with the most frequent tokens coming first.
#gcorpus[1]=sorted(gcorpus[1], key = lambda x: x[1], reverse = True)
for i in range(len(gcorpus)):
    gcorpus[i]=sorted(gcorpus[i], key = lambda x: x[1], reverse = True)

print(gcorpus)

