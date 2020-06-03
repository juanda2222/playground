# things we need for NLP
import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()



# import our chat-bot intents file
import json
import random
import pickle
import numpy as np


with open('./intents.json') as json_data:
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

# stem and lower each word
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]

# remove duplicates
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

print (len(documents), "documents (phrases)")
print (len(classes), "classes (context)", classes)
print (len(words), "unique stemmed words", words)

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
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
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
