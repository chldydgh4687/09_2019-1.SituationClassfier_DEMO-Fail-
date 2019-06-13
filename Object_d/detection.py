#Fixxing gt
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

# load a image

def detection():

## SSD
    
    os.chdir(os.path.commonprefix([os.getcwd(),os.path.dirname(os.path.realpath(__file__))])+"/images/")
    print(os.getcwd())
    img = cv2.imread('frame00020.jpg')
    cv2.rectangle(img,(220,0),(320,300), (255,0,0), 3)
    cv2.imwrite('t_frame00020.jpg',img)
    
    img = cv2.imread('frame00040.jpg')
    cv2.rectangle(img,(150,0),(300,400), (255,0,0), 3)
    cv2.imwrite('t_frame00040.jpg',img)
    
    img = cv2.imread('frame00060.jpg')
    cv2.rectangle(img,(10,0),(280,480), (255,0,0), 3)
    cv2.imwrite('t_frame00060.jpg',img)
  ##cv2.imshow('original',rgbimg)
  ##colab have not x-server, so ipython used
    
