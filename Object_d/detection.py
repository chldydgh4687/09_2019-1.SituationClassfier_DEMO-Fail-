#Fixxing gt
import os
import numpy as np
import cv2

# load a image

def detection():

## SSD
    
    npath=os.path.commonprefix(os.getchwd(),os.path.dirname(os.path.realpath(__file__)))
    os.chdir(npath)
    print(npath)
    rgbimg = cv2.imread('images/frame00000.jpg')
