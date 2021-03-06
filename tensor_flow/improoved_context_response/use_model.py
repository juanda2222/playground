
import pickle
import json
import tflearn
import numpy as np
import random
from keras.models import load_model
from pathlib import Path

# things we need for NLP
import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

##################################
## ------ load saved data ----- ##
##################################

# restore all of our data structure
MODEL_PATH = (Path(__file__).parent / 'keras_model.h5').absolute()
model = load_model(MODEL_PATH)

# restore all of our data structures
TRAINING_DATA_PATH = (Path(__file__).parent / "training_data.pickle").absolute()
with open(TRAINING_DATA_PATH, "rb") as pickle_training_data:
    training_data = pickle.load(pickle_training_data)
  
# import our chat-bot intents file
INTENTS_FILE_PATH = (Path(__file__).parent / "intents.json").absolute()
with open(INTENTS_FILE_PATH) as json_data:
    intents = json.load(json_data)

in_binarizer = training_data['in_binarizer']
out_binarizer = training_data['out_binarizer']
train_x = training_data['train_x']
train_y = training_data['train_y']
test_x = training_data['test_x']
test_y = training_data['test_y']



"""
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

"""

#################################################################
## ------ define the input and output processing helpers ----- ##
#################################################################


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def input_convert_text2binary(sentence:str, show_details=False):

    # ---- clean up the text: -----
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem and lowercase each word (not really that general)
    #sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]

    # convert to binary format:
    binarized_input = in_binarizer.texts_to_matrix([sentence_words])

    if show_details:
        print(
            "For the input: ", 
            sentence, 
            " converted to: ", 
            binarized_input, 
            "vec size: ", 
            len(binarized_input[0])
            )

    return binarized_input

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def output_convert_binary2text(probability_vec:list, show_details=False):

    tagged_vec = []

    # append to an output vec the corresponding tag to each probability:
    for i, prob in enumerate(probability_vec):
        tagged_vec.append( (prob, out_binarizer.classes_[i]) )

    if show_details:
        print(
            "For the input: ", 
            probability_vec, 
            " converted to the paired list: ", 
            tagged_vec, 
            "vec size: ", 
            len(tagged_vec)
            )
    return tagged_vec

# test the converters one at the time
print("Testing input formatting...")
binnary_input = input_convert_text2binary("Are you open?", show_details=True)
print("Testing output formatting...")
tagged_output = output_convert_binary2text([0,0.9,0,0,0,1,0,0.3,0], show_details=True)


###########################################
## ------ Start the text processor ----- ##
###########################################


ERROR_THRESHOLD = 0.60

# create a data structure to hold user context
context = {}

def classify(sentence):

    # generate probabilities from the model
    results = model.predict(input_convert_text2binary(sentence))
    print("Raw results: ", results)
    tagged_results = output_convert_binary2text(results[0])
    print("Tagged results: ", tagged_results)

    # filter out predictions below a threshold
    tagged_results = [ [probability, tag] for probability, tag in tagged_results if probability > ERROR_THRESHOLD ]
    print("Filtered by Threshold: ", tagged_results)

    # sort by strength of probability
    tagged_results.sort(key=lambda x: x[0], reverse=True)
    print("Filtered and sorted vec: ", tagged_results)

    return tagged_results
    

def response(sentence, userID='123', show_details=False):
    results = classify(sentence)
    print("Final result list: ", results)

    # if we have a classification then find the matching intent tag
    if results:
        # loop as long as there are matches to process
        while results:
            for i in intents['intents']:

                # find a tag matching the first result
                if i['tag'] == results[0][1]:
                    
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

