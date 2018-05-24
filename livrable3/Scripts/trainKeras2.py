from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import InputLayer, Input
from tensorflow.python.keras.layers import Reshape, MaxPooling2D
from tensorflow.python.keras.layers import Conv2D, Dense, Flatten
from tensorflow.python.keras.layers import Dropout
from tensorflow.python.keras.optimizers import Adam, SGD, Adagrad
from tensorflow.python.keras.regularizers import l2
from time import time
from tensorflow.python.keras.callbacks import TensorBoard

import numpy as np

# Parameters for convolutional and fully-connected layers

board_size = 64
length = 8
num_classes = 6
num_channels1 = 1
num_channels2 = 64
filter_size1 = 4
num_filters1 = 64
filter_size2 = 2
num_filters2 = 64
l2l = 0.0001

# Start construction of the Keras Sequential model.
model = Sequential()

# Add an input layer which is similar to a feed_dict in TensorFlow.
# Note that the input-shape must be a tuple containing the image-size.
model.add(InputLayer(input_shape=(board_size,)))

# The input is a flattened array with 784 elements,
# but the convolutional layers expect data with shape (8, 8, 1)
model.add(Reshape((length, length, 1)))

# First convolutional layer with ReLU-activation and max-pooling.
model.add(Conv2D(kernel_size=filter_size1, strides=1, filters=num_filters1, padding='same',
                 activation='relu', name='layer_conv1', kernel_regularizer=l2(l2l)))
model.add(MaxPooling2D(pool_size=2, strides=2))

# Second convolutional layer with ReLU-activation and max-pooling.
model.add(Conv2D(kernel_size=filter_size2, strides=1, filters=num_filters2, padding='same',
                 activation='relu', name='layer_conv2', kernel_regularizer=l2(l2l)))
model.add(MaxPooling2D(pool_size=2, strides=2))

# Flatten the 4-rank output of the convolutional layers
# to 2-rank that can be input to a fully-connected layer.
model.add(Flatten())

# First fully-connected layer with ReLU-activation and dropout
model.add(Dense(2048, activation='relu', kernel_regularizer=l2(l2l)))
model.add(Dropout(0.8))

# Second fully-connected layer
model.add(Dense(2048, activation='relu'))

# Third fully-connected layer
model.add(Dense(2048, activation='relu'))

# Last fully-connected layer with softmax
model.add(Dense(num_classes, activation='softmax'))

optimizer = Adam(lr=1e-4) # learning rate is given as parameter

# We use cross entropy as loss function
model.compile(optimizer=optimizer,
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# loading data set of 4M games
trX = np.load('newGamesData.npy')[0:3000000]
teX = np.load('newGamesData.npy')[3000000:4000000]
trY = np.load('newOneHotEncoded.npy')[0:3000000]
teY = np.load('newOneHotEncoded.npy')[3000000:4000000]

# create a Tensorboard used to track learning parameters
tensorboard = TensorBoard(log_dir="logs/{}".format(time()))

def trainNN(nbEpochs, batchSize):
    """
        * Train the neural network with given parameters
        * A power of two batch size is known to be faster with GPU
        * Prints epochs and accuracy on training and testing set
        * Stores train neural network in the file "model"

        :param nbEpochs: number of epochs
        :type nbEpochs: integer
        :param batchSize: size of batch
        :type nbEpochs: integer
        :rtype: none
    """
    model.fit(x=trX,
            y=trY,
            epochs=nbEpochs, batch_size=batchSize, callbacks=[tensorboard])

    result = model.evaluate(x=teX,
                            y=teY)

    print("{0}: {1:.2%}".format(model.metrics_names[1], result[1]))

    model.save("model") # save trained model
