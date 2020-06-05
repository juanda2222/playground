# things we need for NLP
import nltk
nltk.download('punkt')
#from nltk.stem.lancaster import LancasterStemmer
#stemmer = LancasterStemmer()
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer() 

# import our chat-bot intents file
import json
import random
import pickle
import numpy as np
from os.path import abspath
from pathlib import Path, PureWindowsPath

# used to create our training pool using synonyms
import itertools
import time
from copy import copy


INTENTS_PATH = (Path(__file__).parent / "intents.json").absolute()
with open(INTENTS_PATH) as json_data:
    intents = json.load(json_data)


############################################
####------ format intents data -------######
############################################

words = []
classes = []
documents = []
ignore_words = list('!?+*~`[]{.}¿¡%&$#"-^<>/()')

# loop through each sentence in our intents patterns
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        w = nltk.word_tokenize(pattern)
        # add to our words list
        words.extend(w)
        # add to documents in our corpus
        documents.append((w, intent['tag']))
        # add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# lematize and lower each word
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
print(len(words), "Set of duplicated lemmed words!")

# remove duplicates
"""
words = list(set(words))
classes = list(set(classes))

print (len(documents), "documents (phrases)")
print (len(classes), "classes (context)", classes)
print (len(words), "unique lemmed words", words)
"""

#######################################################################
####------ Add synonims to the word pool (english method) -------######
#######################################################################

# for english synonims:
import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')


intent_index = 0
sentence_no = 2

#print(">>>>> all frases taged: ", documents)
synonyms_documents = [] # copy(documents)

# iterate each sentence
prhase_no = 0
count = 1

for phrase, tag in documents:

    prhase_no += 1
    synonyms_documents.append((phrase, tag))

    # iterate each word
    for i, word in enumerate(phrase):
        
        # copy the frase to avoid overwriting:
        aux_phrase = copy(phrase)

        #iterate throug synonyms
        for syn in wordnet.synsets(word):
                        
            # process unique synonyms
            for synonym in syn.lemmas():
                #print("Synonyms: ", l.name())
                aux_phrase[i] = synonym.name()
                print("New phrase: ", aux_phrase, "Tag: ", tag, ", original No.", prhase_no )
                synonyms_documents.append( (copy(aux_phrase), tag ) )
    
            
print(len(synonyms_documents), "Synonyms sencences. List secction: ", synonyms_documents[:120])

"""
for frases in itertools.permutations(
    documents[sentence_no][intent_index],
    len(documents[sentence_no][intent_index])
    ):
    print("Frase: ", frases, "Sentence No. ", sentence_no, "intent index: ", intent_index) # [sentence as list][intent]
"""
print(len(words), "Expanded set of lemmed words!")



#########################################################
####------ create our training numeric data -------######
#########################################################

training = []
output = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stem each word
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    # create our bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)

# create train and test lists
train_x = list(training[:,0])
train_y = list(training[:,1])

print (len(train_x), "training x. X example: ", train_x[0])
print (len(train_y), "training y. Y example: ", train_y[0])

# save all of our data structures
with open( "training_data.pickle", "wb" ) as pickle_data:
    pickle.dump( {'words':words, 'classes':classes, 'train_x':train_x, 'train_y':train_y},  pickle_data)
