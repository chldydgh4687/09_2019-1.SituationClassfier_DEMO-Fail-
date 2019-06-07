#Fixxing gt
import os
import numpy as np
import cv2

# load a image

def detection():

## SSD
    
    os.chdir(os.path.commonprefix([os.getcwd(),os.path.dirname(os.path.realpath(__file__))]))
    rgbimg=cv2.imread('images/frame00000.jpg')
