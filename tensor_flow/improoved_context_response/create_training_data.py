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


#######################################################################
####------ Add synonims to the word pool (english method) -------######
#######################################################################

# for english synonims:
import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')


intent_index = 0
sentence_no = 2

synonyms_tagged_sentences = [] # copy(documents)
synonyms_words = []
synonyms_clases = []

# iterate each sentence
prhase_no = 0
count = 1

# loop through each sentence in our intents patterns
for intent in intents['intents']:

    synonyms_clases.append(intent['tag'])

    for pattern in intent['patterns']:

        # separate the text as a list of words. like: ["this", "is", "a", "sentence"]
        sentence_list = nltk.word_tokenize(pattern)
        sentence_list = [word.lower() for word in sentence_list] # convert to lowercase

        prhase_no += 1
        synonyms_tagged_sentences.append((sentence_list, intent['tag']))
        synonyms_words.extend(sentence_list)

        # generate the tagged word list:
        tagged_phrase = nltk.pos_tag(sentence_list)

        # iterate each word
        for i, word in enumerate(sentence_list):
            
            # copy the frase to avoid overwriting of the original phrase:
            aux_phrase = copy(sentence_list)

            # get the synonim type (noun, adjective, etc...) of the word
            word_type = tagged_phrase[i][1][0].lower()
            synonym_list = []

            # Generate the synonyms list
            # avoid error with special kind of types such as "possessive wh-pronoun" identified with "w" character
            try:
                #iterate throug synonyms
                for syn in wordnet.synsets(word, word_type): # filter by word type j, n, i, c ,r ,v, u, p
                                
                    # process unique synonyms
                    for synonym in syn.lemmas():

                        #print("Synonyms: ", l.name())
                        synonym_list.append(synonym.name().lower())
                
                # remove duplicates!
                synonym_list = list(set(synonym_list))

            except Exception:
                print("Synonyms not found for that type of word")
            
            # Append the new synonyms for the current word:
            for synonym in synonym_list:

                aux_phrase[i] = synonym
                print("New phrase: ", aux_phrase, "Tag: ", intent['tag'], ", original No.", prhase_no )
                
                # add to the sentence list
                synonyms_tagged_sentences.append( (copy(aux_phrase), intent['tag'] ) ) # use copy to avoid duplicates 
                # add to the word list (for the dictionary)
                synonyms_words.extend(aux_phrase)
                
# lematize and lower each word
# synonyms_words = [lemmatizer.lemmatize(w.lower()) for w in synonyms_words if w not in ignore_words] # the bag of words keras method aleady filter
 
# remoove duplicates
synonyms_words = list(set(synonyms_words))
synonyms_clases = list(set(synonyms_clases))

print(">> ", len(synonyms_tagged_sentences), "Synonyms sencences. List secction: ", synonyms_tagged_sentences[:120])
print(">> ", len(synonyms_words), "Synonym words. List section: ", synonyms_words[:40])
print(">> ", len(synonyms_clases), "Synonym clases. List section: ", synonyms_clases)


"""
# optional add a permutation logic to the synonym generation (not working)

for frases in itertools.permutations(
    documents[sentence_no][intent_index],
    len(documents[sentence_no][intent_index])
    ):
    print("Frase: ", frases, "Sentence No. ", sentence_no, "intent index: ", intent_index) # [sentence as list][intent]
"""


#########################################################
####------ create our training numeric data -------######
#########################################################

from keras.preprocessing import text
from sklearn.utils import shuffle   
from sklearn.preprocessing import MultiLabelBinarizer
import pandas as pd


# Prepare the data for preprocessing (Create the pandas DataFrame and shuffle)
data = pd.DataFrame(synonyms_tagged_sentences, columns = ['Sentenece', 'tag',])  
data = shuffle(data, random_state=22)
print(data.head())

# create the binary data from th dataset
tag_encoder = MultiLabelBinarizer()
num_tags = tag_encoder.fit_transform(data["tag"].values)
print(num_tags)

# create a dataset with the data coded (ones and ceros)
word_tokenizer = text.Tokenizer(num_words=200)
word_tokenizer.fit_on_texts([])


"""
training = []
output = []
# create an empty array for our output
output_empty = [0] * len(synonyms_clases)

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

"""