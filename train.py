## cnn quiz2 samling guide line

import tensorflow as tf
import random
from tensorflow.examples.tutorials.mnist import input_data

import numpy as np
from tensorflow.contrib.layers import flatten
from skimage import transform


def resize_batch(imgs):
    # A function to resize a batch of MNIST images to (32, 32)
    # Args:
    #   imgs: a numpy array of size [batch_size, 28 X 28].
    # Returns:
    #   a numpy array of size [batch_size, 32, 32].
    imgs = imgs.reshape((-1, 28, 28, 1))
    resized_imgs = np.zeros((imgs.shape[0], 32, 32, 1))
    for i in range(imgs.shape[0]):
        resized_imgs[i, ..., 0] = transform.resize(imgs[i, ..., 0], (32, 32))
    return resized_imgs





tf.set_random_seed(777)  # reproducibility
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


# hyper parameters
learning_rate = 0.001
training_epochs = 15
batch_size = 100

# dropout (keep_prob) rate  0.7~0.5 on training, but should be 1 for testing
keep_prob = tf.placeholder(tf.float32)

# input place holders
X = tf.placeholder(tf.float32, (None,32,32,1))
Y = tf.placeholder(tf.float32, [None, 10])

# LeNet5 Model (1)


# TODO: Layer 1: Convolutional. 
# Input = 32x32x1. Output = 28x28x6.
conv1_w = tf.Variable(tf.random_normal(shape = [5,5,1,6], stddev = 0.01))
conv1 = tf.nn.conv2d(X,conv1_w, strides = [1,1,1,1], padding = 'VALID')
conv1 = tf.nn.relu(conv1)

# TODO: Pooling. 
# Input = 28x28x6. Output = 14x14x6.
pool_1 = tf.nn.max_pool(conv1,ksize = [1,2,2,1], strides = [1,2,2,1], padding = 'VALID')

# TODO: Layer 2: Convolutional. 
# Output = 10x10x16.
conv2_w = tf.Variable(tf.random_normal(shape = [5,5,6,16], stddev = 0.01))
conv2 = tf.nn.conv2d(pool_1, conv2_w, strides = [1,1,1,1], padding = 'VALID') 
conv2 = tf.nn.relu(conv2)

# TODO: Pooling. 
# Input = 10x10x16. Output = 5x5x16 = 400
pool_2 = tf.nn.max_pool(conv2, ksize = [1,2,2,1], strides = [1,2,2,1], padding = 'VALID') 
fc1 = flatten(pool_2)

# TODO: Layer 3: Fully Connected. 
# Input = 400. Output = 120.
fc1_w = tf.Variable(tf.random_normal(shape = (400,120), stddev = 0.01))
fc1 = tf.matmul(fc1,fc1_w) 
fc1 = tf.nn.relu(fc1)

# TODO: Layer 4: Fully Connected. 
# Input = 120. Output = 84.
fc2_w = tf.Variable(tf.random_normal(shape = (120,84), stddev = 0.01))
fc2 = tf.matmul(fc1,fc2_w) 
fc2 = tf.nn.relu(fc2)

# TODO: Layer 5: Fully Connected. 
# Input = 84. Output = 10.
fc3_w = tf.Variable(tf.random_normal(shape = (84,10),  stddev = 0.01))
logits = tf.matmul(fc2, fc3_w) 

    
   

# define cost/loss & optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    logits=logits, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# initialize
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# train my model
print('Learning started. It takes sometime.')
for epoch in range(training_epochs):
    avg_cost = 0
    total_batch = int(mnist.train.num_examples / batch_size)

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        batch_xs = resize_batch(batch_xs)
        
        feed_dict = {X: batch_xs, Y: batch_ys, keep_prob: 0.7}
        c, _ = sess.run([cost, optimizer], feed_dict=feed_dict)
        avg_cost += c / total_batch

    print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))

print('Learning Finished!')
