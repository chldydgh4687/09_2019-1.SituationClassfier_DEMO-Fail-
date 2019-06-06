import os
import sys
import os.path
import numpy as np
from read_write import VTP

#from Depth_e import test_davis_videos0

from images import autolist_txt

#TEST VIDEO OPEN& JPG WRITE

VTP.video_to_picture('./test_data/demo.mp4','./images')

###########################################################

autolist_txt.autolist()

##
##def test():
##    # Test model and check accuracy
##
## # if you have a OOM error, please refer to lab-11-X-mnist_deep_cnn_low_memory.py
##
##correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(Y, 1))
##accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
##print('Accuracy:', sess.run(accuracy, feed_dict={
##      X: resize_batch(mnist.test.images), Y: mnist.test.labels, keep_prob: 1}))
##
## # Get one and predict
##r = random.randint(0, mnist.test.num_examples - 1)
##print("Label: ", sess.run(tf.argmax(mnist.test.labels[r:r + 1], 1)))
##print("Prediction: ", sess.run(
##    tf.argmax(logits, 1), feed_dict={X: resize_batch(mnist.test.images[r:r + 1]), keep_prob: 1}))

