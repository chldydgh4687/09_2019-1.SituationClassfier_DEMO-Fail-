import pandas
import os
import tensorflow as tf
import numpy as np

model = tf.global_variables_initializer()

data = pandas.read_csv('Virtual_Data'.csv,header=None)

X = tf.placeholder(tf.float32, [None, 3])
Y = tf.placeholder(tf.float32, [None, 1])

W = tf.Variable(tf.random_normal([3,1]), name = "weight")
b = tf.Variable(tf.random_normal([1]), name ='bias')
hypothesis = tf.nn.softmax(tf.matmul(X,W)+b)

cost = tf.reduce_mean(-tf.reduce_sum(Y*tf.log(hypothesis),axis=1))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initiallizer())

##learn  

print("------------")
print(' learn start ')
print("------------")

for step in range(101):
	cost_, hypo_, _ = sess.run([cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
	if step % 100 == 0:
		print("#",step, ":loss: ", cost_)
		print("-À§Çèµµ: ",hypo_[0])


print('-----------')
print('  learn end  ')
print('-----------')