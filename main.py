# -*- coding: utf-8 -*-
import cv2

#image capture class

vidcap = cv2.VideoCapture('test_data/demo.mp4')

count = 0

while(vidcap.isOpened()):

    ret, image = vidcap.read()

    cv2.imwrite("images/frame%d.jpg"% count, image)

    print('Saved frame%d.jpg' % count)
    count += 1

vidcap.release()
