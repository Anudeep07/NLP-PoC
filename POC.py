from nltk import ne_chunk
from nltk.corpus import treebank

# Can be any sentence. tagged_sents() returns sentences which are already POS tagged
sentence = treebank.tagged_sents()[2]

#Print the sentence
for wordTag in sentence:
    word = wordTag[0]
    print(word, end=' ')

# NLTK provides a classifier that has already been trained to recognize named entities
chunkedSentence = ne_chunk(sentence)
print()
print(chunkedSentence)
#chunkedSentence.draw() # Shows tree structure