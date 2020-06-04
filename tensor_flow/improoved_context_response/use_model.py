
import pickle
import json
import tflearn
import numpy as np
import random

# things we need for NLP
import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

##################################
## ------ load saved data ----- ##
##################################

# restore all of our data structures
with open('./training_data.pickle', "rb") as pickle_training_data:
    training_data = pickle.load(pickle_training_data)

words = training_data['words']
classes = training_data['classes']
train_x = training_data['train_x']
train_y = training_data['train_y']

# import our chat-bot intents file
with open('intents.json') as json_data:
    intents = json.load(json_data)


# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
print(">> Input tensor: ", net)
net = tflearn.fully_connected(net, 8)
print(">> Layer 1 tensor: ", net)
net = tflearn.fully_connected(net, 8)
print(">> Layer 2 tensor: ", net)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
print(">> Layer 3 tensor: ", net)
net = tflearn.regression(net)
print(">> Regresion layer tensor (softmax): ", net)

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
print(">> General model: ", model)

# load our saved model
model.load('./model.tflearn')


######################################################
## ------ define the input processing helpers ----- ##
######################################################


def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))


p = bow("is your shop open today?", words)
print("Testing input formatting with input:")
print("> is your shop open today?")
print(p)


###########################################
## ------ Start the text processor ----- ##
###########################################

ERROR_THRESHOLD = 0.60

# create a data structure to hold user context
context = {}

def classify(sentence):

    # generate probabilities from the model
    results = model.predict([bow(sentence, words)])
    print("Raw results: ", results)

    # filter out predictions below a threshold
    results = [[intent_index, probability] for intent_index, probability in enumerate(results[0]) if probability > ERROR_THRESHOLD]
    print("Filtered by Threshold: ", results)

    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    print("Filtered and sorted vec: ", results)

    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of intent and probability
    return return_list

def response(sentence, userID='123', show_details=False):
    results = classify(sentence)
    print("Final result list: ", results)

    # if we have a classification then find the matching intent tag
    if results:
        # loop as long as there are matches to process
        while results:
            for i in intents['intents']:

                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    
                    # set context for this intent if necessary
                    if 'context_set' in i:
                        if show_details: print ('context:', i['context_set'])
                        context[userID] = i['context_set']

                    # check if this intent is contextual and applies to this user's conversation
                    if not 'context_filter' in i or \
                        (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                        if show_details: print ('tag:', i['tag'])
                        # a random response from the intent
                        return print(random.choice(i['responses']))


            results.pop(0)

    # all parametters 
    else:
        default_responses = [
            "I didn't understand that",
            "Could you repeat that please",
            "Please repeat that"
        ]
        return print(random.choice(default_responses))

while True:
    user_text = input("")
    if user_text is not "":
        response(user_text, show_details=True)
