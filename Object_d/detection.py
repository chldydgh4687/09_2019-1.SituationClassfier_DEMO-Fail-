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

    p1_d = [(int)(0.8*(p1[0]+((p1[2]-p1[0])/2))),(int)(0.6*(p1[1]+((p1[3]-p1[1])/2)))]
    p2_d = [(int)(0.8*(p2[0]+((p2[2]-p2[0])/2))),(int)(0.6*(p2[1]+((p2[3]-p2[1])/2)))]
    p3_d = [(int)(0.8*(p3[0]+((p3[2]-p3[0])/2))),(int)(0.6*(p3[1]+((p3[3]-p3[1])/2)))]

    P_list = [p1_d,p2_d,p3_d]
    ## 사진이 512x 288 로 변경됨. 비율 계산식이 필요 
    ## 세로 비율 0.6, 가로 비율 0.8

    os.chdir(os.path.commonprefix([os.getcwd(),os.path.dirname(os.path.realpath(__file__))])+"Depth_e/viz_predictions/images")
    # p1_d = [x.y] to rectangle 
    
    mse_prevent(P_list)

def mse_prevent(P_list):

    print(os.getcwd())
    img = cv2.imread('frame00020.jpg')
    print(img)





    ##guide_line

    #img = cv2.imread('frame00020.jpg')
    #cv2.circle(img,(p1_d[0],p1_d[1]),3,(255,0,0),-1)
    #cv2.rectangle(img,(p1_d[0]-25,p1_d[1]-25),(p1_d[0]+25,p1_d[1]+25),(255,0,0),3)
    #cv2.imwrite('m_frame00020.jpg',img)

    #img = cv2.imread('frame00040.jpg')
    #cv2.circle(img,(p2_d[0],p2_d[1]),3,(255,0,0),-1)
    #cv2.imwrite('m_frame00040.jpg',img)

    #img = cv2.imread('frame00060.jpg')
    #cv2.circle(img,(p3_d[0],p3_d[1]),3,(255,0,0),-1)
    #cv2.imwrite('m_frame00060.jpg',img)


### 일단 수동적임을 말씀드립니다...추후 recursive 로 짤생각..