# -*- coding: utf-8 -*-
import argparse
import cv2

vidcap = cv2.VideoCapture('./test_data/demo.mp4')
success,image = vidcap.read()
count = 0;
while success:
    success,image = vidcap.read()
    cv2.imwrite("./images/frame%d.jpg"% count, image)     # save frame as JPEG file
    if cv2.waitKey(10) == 27:                     # exit if Escape is hit
        break
    count += 1
