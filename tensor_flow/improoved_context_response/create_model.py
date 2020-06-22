

# things we need for Tensorflow
import numpy as np

import tensorflow as tf
from keras.layers import Dense
from keras.models import Sequential

# import our chat-bot intents file
import pickle
from pathlib import Path

# restore all of our data structures
TRAINING_DATA_PATH = (Path(__file__).parent / "training_data.pickle").absolute()
with open(TRAINING_DATA_PATH, "rb") as pickle_training_data:
    training_data = pickle.load(pickle_training_data)

in_binarizer = training_data['in_binarizer']
train_x = training_data['train_x']
train_y = training_data['train_y']
test_x = training_data['test_x']
test_y = training_data['test_y']

print ("Training data loaded:")
print ("In binarizer: ", in_binarizer)
print (len(train_x), "Training x. X example: ", train_x)
print (len(train_y), "Training y. Y example: ", train_y)
print (len(test_x), "Testing x. X example: ", test_x)
print (len(test_y), "Testing y. Y example: ", test_y)


############################################
####------- generate the RNN model ----#####
############################################

# reset underlying graph data
tf.compat.v1.reset_default_graph()

model = Sequential()
model.add( Dense( 40, input_shape=(len(train_x[0]),), activation="relu", name="Dense_input"))
model.add( Dense( 15, activation="relu", name="Dense_hidden"))
model.add( Dense( len(train_y[0]), activation="sigmoid", name="Dense_output" ))

# set the configuration of the learning process
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"]) 

#print the characteristics:
model.summary()

# train the model
# epochs No. of times the algoorithm will go through the entire dataset
#batch_size is the group used to calculate the 
model.fit(train_x, train_y, epochs=200, batch_size=20)

# test the results
print("Model testing results:")
print("test x set:", test_x)
print("test y set:", test_y)

loss, acc = model.evaluate(test_x, test_y, batch_size=20)
print('\nTesting loss: {}, acc: {}\n'.format(loss, acc))


# save the model to disk
MODEL_DATA_PATH = (Path(__file__).parent / "keras_model.h5").absolute()
model.save(MODEL_DATA_PATH)
