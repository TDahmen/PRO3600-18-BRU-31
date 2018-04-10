import numpy as np
import tensorflow as tf

# Let's create some variables

board_size = 64
length = 8
num_classes = 8
num_channels1 = 1
num_channels2 = 64
filter_size1 = 4
num_filters1 = 64
filter_size2 = 2
num_filters2 = 64

# Labels and inputs initialization

X_placeholder = tf.placeholder(tf.float32, shape = [None, board_size], name="X")
# We need a 4-dim tensor for the convolution
X = tf.reshape(X_placeholder, [-1, length, length, 1])
y_placeholder = tf.placeholder(tf.float32, shape = [None, num_classes], name="y")
learningRate = tf.placeholder(tf.float32)


# Helper function to add a conv layer to TF's graph

def new_conv_layer(input, num_input_channels, filter_size, num_filters, use_pooling=True):
    # Define shape of the filters for the convolution
    shape = [filter_size, filter_size, num_input_channels, num_filters]
    # Create associated filters (weights) and biases
    weights = tf.Variable(tf.truncated_normal(shape, stddev=0.05))
    biases = tf.Variable(tf.constant(0.05, shape=[num_filters]))

    layer = tf.nn.conv2d(input=input, filter=weights, strides=[1, 1, 1, 1], padding='SAME')
    layer += biases

    if use_pooling:
        layer = tf.nn.max_pool(value=layer, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    layer = tf.nn.relu(layer)

    return layer


# Helper function to add a fully connected layer to the graph

def new_fc_layer(input, num_inputs, num_outputs, use_relu=True):
    weights = tf.Variable(tf.truncated_normal([num_inputs, num_outputs], stddev=0.05))
    biases = tf.Variable(tf.constant(0.05, shape=[num_outputs]))

    layer = tf.matmul(input, weights) + biases

    if use_relu:
        layer = tf.nn.relu(layer)

    return layer


# Helper function to split data into batches

def next_batch(features, labels, batch_size):
    nb_batches = int(lenGamesData / batch_size)

    for batch in range(nb_batches):
        start = batch * batch_size
        if start + batch_size < lenGamesData:
            end = start + batch_size
        else:
            end = lenGamesData - 1
        yield features[start:end], labels[start:end]

# def next_batch(num, data, labels):
#
#     '''
#     Return a total of `num` random samples and labels.
#     '''
#     idx = np.arange(0 , lenGamesData)
#     np.random.shuffle(idx)
#     idx = idx[:num]
#     data_shuffle = data[idx]
#     labels_shuffle = labels[idx]
#     labels_shuffle = np.asarray(labels_shuffle.values.reshape(len(labels_shuffle), 1))
#
#     return data_shuffle, labels_shuffle


# Let's build two convolutional layers

layer_conv1 = new_conv_layer(input=X,
                             num_input_channels=num_channels1,
                             filter_size=filter_size1,
                             num_filters=num_filters1,
                             use_pooling=True)

layer_conv2 = new_conv_layer(input=layer_conv1,
                             num_input_channels=num_channels2,
                             filter_size=filter_size2,
                             num_filters=num_filters2,
                             use_pooling=True)

# Convolution outputs 4-dim tensors, we need 2-dim tensors for the FC layer

layer_flat = tf.reshape(layer_conv2, [-1, board_size * 2 * 2])

layer_fc1 = new_fc_layer(layer_flat, board_size * 2 * 2, 1024, True)
layer_fc2 = new_fc_layer(layer_fc1, 1024, 8, False)

# Let's define the cost function and the optimization method

cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=layer_fc2, labels=y_placeholder)
cost = tf.reduce_mean(cross_entropy)

optimizer = tf.train.AdamOptimizer(learning_rate=learningRate).minimize(cost)

# We create a tensorflow session and run it

sess = tf.Session()
sess.run(tf.global_variables_initializer())
train_batch_size = 10


def optimize(epochs, features, labels):
    for epoch in range(epochs):
        for (x_batch, y_true_batch) in next_batch(features, labels, train_batch_size):
            feed_dict_train = {X: x_batch, y_placeholder: y_true_batch, learningRate: 0.01}
            _, loss_val = sess.run([optimizer, cross_entropy], feed_dict=feed_dict_train)
            # print(tf.reduce_mean(loss_val).eval(session=sess))

# gamesDataNumpy = np.load('data/gamesData.npy')
# lenGamesData = len(gamesDataNumpy)
# gamesData = tf.convert_to_tensor(gamesDataNumpy, np.float32)
# oneHotEncoded = tf.convert_to_tensor(np.load('data/oneHotEncoded.npy'), np.float32)

gamesDataImported = np.load('data/gamesData.npy')
gamesData = np.reshape(gamesDataImported, (-1, 8, 8, 1))
oneHotEncoded = np.load('data/oneHotEncoded.npy')
lenGamesData = len(gamesDataImported)

dataset = tf.data.Dataset.from_tensor_slices(X)
iter = dataset.make_initializable_iterator()
el = iter.get_next

optimize(30, gamesData, oneHotEncoded)
