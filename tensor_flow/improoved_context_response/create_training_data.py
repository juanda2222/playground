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
import numpy as numpy
from pathlib import Path

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
        synonyms_tagged_sentences.append((sentence_list, (intent['tag'],) ))
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
                print("New phrase: ", aux_phrase, "Tag: ", (intent['tag']) , ", original No.", prhase_no )
                
                # add to the sentence list
                synonyms_tagged_sentences.append( (copy(aux_phrase), (intent['tag'],) ) ) # use copy to avoid duplicates 
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

# use 80% as training dataset
TRAINING_SIZE = int( len(synonyms_tagged_sentences) * 0.8 )

# Prepare the data for preprocessing (Create the pandas DataFrame and shuffle)
pandas_data = pd.DataFrame(synonyms_tagged_sentences, columns = ['Sentenece', 'Tag',])  
pandas_data = shuffle(pandas_data, random_state=22)
print(">> data head: ", pandas_data.head())

# create the output binary data from the dataset
#-----------------------------------------------
tag_encoder = MultiLabelBinarizer()
binarized_y_data = tag_encoder.fit_transform(pandas_data["Tag"].values) # this function filters !”#$%&()*+,-./:;<=>?@[\]^_{|}~\t\n. characters
#binarizer info:
#print(tag_encoder.classes_)

# separate the training y data from the testing one
y_training_data = binarized_y_data[:TRAINING_SIZE]
y_testing_data = binarized_y_data[TRAINING_SIZE:]

# Print for inspection
print(len(binarized_y_data), " Binnarized Taggs. Taggs: ", binarized_y_data)
print(len(binarized_y_data[0]), "Output size. Output example: ", binarized_y_data[0])


# create the input binary data from the dataset
#-----------------------------------------------
word_tokenizer = text.Tokenizer(num_words=200) # num_words is the size of the vocabulary
word_tokenizer.fit_on_texts(pandas_data["Sentenece"]) # use this to set up the bynary converter for the input

# about the tokenizer:
# print(word_tokenizer.word_counts)
# print(word_tokenizer.word_docs)
# print(word_tokenizer.word_index)
# print(word_tokenizer.document_count)

# separete the training x data to the testing one and convert it to binary matrix
binarized_x_data = word_tokenizer.texts_to_matrix(pandas_data["Sentenece"].values)
x_training_data = binarized_x_data[:TRAINING_SIZE]
x_testing_data = binarized_x_data[TRAINING_SIZE:]

# Print for inspection
print(len(binarized_x_data), " Binnarized sentences. Sentences: ", binarized_x_data)
print(len(binarized_x_data[0]), "Input size. Input example: ", binarized_x_data[0])


# save all of our data structures
TRAINING_DATA_PATH = (Path(__file__).parent / "training_data.pickle").absolute()
with open( TRAINING_DATA_PATH, "wb" ) as pickle_data:
    pickle.dump( {
        'in_binarizer':word_tokenizer, 
        'out_binarizer':tag_encoder, 
        'train_x':x_training_data, 
        'train_y':y_training_data, 
        'test_x':x_testing_data,
        'test_y':y_testing_data,
    },  pickle_data)
