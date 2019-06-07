#Fixxing gt
import os
import numpy as np
import cv2
from IPython.display import Image

# load a image

def detection():

## SSD
    
    os.chdir(os.path.commonprefix([os.getcwd(),os.path.dirname(os.path.realpath(__file__))])+"/images/")
    print(os.getcwd())
    rgbimg=cv2.imread('frame00000.jpg')
    Image('frame00000.jpg')
    
  ##  cv2.imshow('original',rgbimg)
  ##colab have not x-server, so ipython used
    
