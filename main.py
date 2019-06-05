# -*- coding: utf-8 -*-
import cv2

#image capture class
print("1")
vidcap = cv2.VideoCapture('/test_data/demo.mp4')

count = 0

while(vidcap.isOpened()):

    ret, image = vidcap.read()
    print("2")
    cv2.imwrite("/images/frame%d.jpg"% count, image)
    print("3")
    print('Saved frame%d.jpg' % count)
    count += 1

vidcap.release()
