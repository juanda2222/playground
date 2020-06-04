

# things we need for Tensorflow
import numpy as np
import tflearn
import tensorflow as tf

# import our chat-bot intents file
import pickle

# restore all of our data structures
with open('./training_data.pickle', "rb") as pickle_training_data:
    training_data = pickle.load(pickle_training_data)


words = training_data['words']
classes = training_data['classes']
train_x = training_data['train_x']
train_y = training_data['train_y']

print ("Training data loaded:")
print (len(classes), "classes (context)", classes)
print (len(words), "unique stemmed words", words)
print (len(train_x), "training x. X example: ", train_x)
print (len(train_y), "training y. Y example: ", train_y)


############################################
####------- generate the RNN model ----#####
############################################

# reset underlying graph data
tf.reset_default_graph()

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

# Start training (apply gradient descent algorithm)
model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)

# Save model to file
model.save('model.tflearn')



