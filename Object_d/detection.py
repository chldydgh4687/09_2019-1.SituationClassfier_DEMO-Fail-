#Fixxing gt
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2


# load a image

def detection():

## SSD
    
    os.chdir(os.path.commonprefix([os.getcwd(),os.path.dirname(os.path.realpath(__file__))])+"/images/")
    print(os.getcwd())
    img = cv2.imread('frame00000.jpg')
    print(img)
    plt.figure(figsize=(18,18))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
  ##  cv2.imshow('original',rgbimg)
  ##colab have not x-server, so ipython used
    
