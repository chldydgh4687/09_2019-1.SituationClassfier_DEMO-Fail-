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
<<<<<<< HEAD
    img2 = img(:,:,::-1)
    plt.imshow(img)
    
=======
    print(img)
    plt.figure(figsize=(1800,1800))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
>>>>>>> dafd35e6b1cb318c784c40b07558444c17d1be35
  ##  cv2.imshow('original',rgbimg)
  ##colab have not x-server, so ipython used
    
