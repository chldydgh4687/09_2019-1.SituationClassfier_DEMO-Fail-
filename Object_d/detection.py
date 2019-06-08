#Fixxing gt
import os
import numpy as np
from google.colab.patches import cv2_imshow
import cv2


# load a image

def detection():

## SSD
    
    os.chdir(os.path.commonprefix([os.getcwd(),os.path.dirname(os.path.realpath(__file__))])+"/images/")
    print(os.getcwd())
    
    rgbimg=cv2.imread('frame00000.jpg')
    cv2_imshow(rgbimg)
    
  ##  cv2.imshow('original',rgbimg)
  ##colab have not x-server, so ipython used
    
