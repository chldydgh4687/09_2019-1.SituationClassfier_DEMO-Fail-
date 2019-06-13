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
        
    xy =([220,0,320,300]) ##extraction x1y1,x2y2 dot
    
    cv2.imwrite('t_frame00020.jpg',img)  ## Saving detected picture 
    
    img = cv2.imread('frame00040.jpg')
    cv2.rectangle(img,(150,0),(300,400), (255,0,0), 3)
    
    xy1 =([150,0,300,400]) ##extraction x1y1,x2y2 dot
    
    cv2.imwrite('t_frame00040.jpg',img)  ## Saving detected picture 
    
    img = cv2.imread('frame00060.jpg')
    cv2.rectangle(img,(10,0),(280,480), (255,0,0), 3)
    
    xy2 =([10,0,280,480])  ##extraction x1y1,x2y2 dot
    
    cv2.imwrite('t_frame00060.jpg',img) ## Saving detected picture

    return xy, xy1, xy2

def de_box(p1,p2,p3):

    # p = [x,y,w,h] to half dot  p1_d = [x,y]

    p1_d = [(int)(p1[0]+((p1[2]-p1[0])/2)),(int)(p1[1]+((p1[3]-p1[1])/2))]
    p2_d = [(int)(p2[0]+((p2[2]-p2[0])/2)),(int)(p2[1]+((p2[3]-p2[1])/2))]
    p3_d = [(int)(p3[0]+((p3[2]-p3[0])/2)),(int)(p3[1]+((p3[3]-p3[1])/2))]
    
    os.chdir(os.path.commonprefix([os.getcwd(),os.path.dirname(os.path.realpath(__file__))])+"Depth_e/viz_predictions/images")
    # p1_d = [x.y] to rectangle 
    img = cv2.imread('frame00020.jpg')
    cv2.circle(img,(p1_d[0],p1_d[1]),3, (255,0,0), -1)
    cv2.imwrite('m_frame00020.jpg',img)

    img = cv2.imread('frame00040.jpg')
    cv2.circle(img,(p2_d[0],p2_d[1]),3,(255,0,0),-1)
    cv2.imwrite('m_frame00040.jpg',img)

    img = cv2.imread('frame00060.jpg')
    cv2.circle(img,(p3_d[0],p3_d[1]),3,(255,0,0),-1)
    cv2.imwrite('m_frame00060.jpg',img)



#fail code
#def movetoDep(p1,p2,p3):

#    # p = [x,y,w,h]
#  if(p1[0]>p2[0]+p2[2]):
#    return null
#  if(p1[0]+p1[2]<p2[0]):
#    return null
#  if(p1[1]>p2[1]+p2[3]):
#    return null
#  if(p1[1]+p1[3]<p2[1]):
#    return null
  
#  rect = [0,0,0,0]
#  rect[0] = max(p1[0],p2[0])
#  rect[1] = max(p1[1],p2[1])
#  rect[2] = min(p1[0]+p1[2],p2[0]+p2[2])-rect[0]
#  rect[3] = min(p1[1]+p1[3],p2[1]+p2[3])-rect[1]
  
#  if(p2[0]>p3[0]+p3[2]):
#    return null
#  if(p2[0]+p2[2]<p3[0]):
#    return null
#  if(p2[1]>p3[1]+p3[3]):
#    return null
#  if(p2[1]+p2[3]<p3[1]):
#    return null
  
#  rect2 = [0,0,0,0]
#  rect2[0] = max(p2[0],p3[0])
#  rect2[1] = max(p2[1],p3[1])
#  rect2[2] = min(p2[0]+p2[2],p3[0]+p3[2])-rect2[0]
#  rect2[3] = min(p2[1]+p2[3],p3[1]+p3[3])-rect2[1]

#  return rect, rect2

### 일단 수동적임을 말씀드립니다...추후 recursive 로 짤생각..
