import os
import cv2
import sys
import os.path
import numpy as np
from read_write import VTP
from Depth_e import test_davis_videos
from Object_d import detection
from images import autolist_txt

#TEST VIDEO OPEN& JPG WRITE

print("==========Extracting VIDEO >>>> FRAME ===========\n")
VTP.video_to_picture('./test_data/demo.avi','./images')
print("\n")

###########################################################

print("========== auto data_list.txt ===========\n")
autolist_txt.autolist()
print("\n")

###########################################################

print("========== making Depth =================\n")
print(os.getcwd())
test_davis_videos.td_Depth()
print("\n")

image_folder = (os.getcwd())
video_name = 'd_demo.avi'

#이미지 파일형식 지정
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

#VideoWriter(video_name, 0, 프레임, (width,height)
video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

video.release()


###########################################################

print("=========== Detecting Object ==============\n")
p1,p2,p3 = detection.detection()  ### object dot

print("=============== Success =====================\n")

#######################################################################

print("================ Distance Estimation ==================\n")

rp1,rp2,rp3 = detection.de_ratio(p1,p2,p3)
detection.mse_prevent(rp1,rp2,rp3)
## accuracy upgrading : algorithm of depth dot by using reference before frame
 
print("================ Successs ===============================\n")

##########################################################################

print("================ Road_Detection Readying.. ======================\n")
## 
print("\n")


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
