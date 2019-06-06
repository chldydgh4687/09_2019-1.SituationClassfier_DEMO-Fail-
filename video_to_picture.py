# -*- coding: utf-8 -*-
import argparse
import cv2

def video_to_picture(op,wp):
    vidcap = cv2.VideoCapture('./test_data/demo.mp4')
    success,image = vidcap.read()
    count = 0;
    while success:
        success,image = vidcap.read()
        cv2.imwrite(wp+"/frame%d.jpg"% count, image)
        print("frame%d.jpg extract success"% count)
        # save frame as JPEG file
        if cv2.waitKey(50) == 27:
            # exit if Escape is hit
            break
        count += 1


#when we are possible real time, we must find new code.. 
