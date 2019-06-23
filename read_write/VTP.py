# -*- coding: utf-8 -*-
import argparse
import cv2

def video_to_picture(op,wp):
    vidcap = cv2.VideoCapture(op)
    success,image = vidcap.read()
    count = 0;
    while success:
        success,image = vidcap.read()
        if count % 1== 0:
            cv2.imwrite(wp+"/frame%05d.jpg"% count, image)
            print("frame%05d.jpg extract success"% count)
        # save frame as JPEG file
        if cv2.waitKey(10) == 27:
            # exit if Escape is hit
            break
        count +=0.1


#when we are possible real time, we must find new code.. 
