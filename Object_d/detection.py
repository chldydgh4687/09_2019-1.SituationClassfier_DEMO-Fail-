#Fixxing gt
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
import json
# load a image

def detection(json_list):

## SSD

    print(os.getcwd())

# i = iter, data = list
    for i, data in enumerate(json_list):
        with open(data[i]) as json_file:
            json_data = json.load(json_file)

        json = json_data["detection_boxes"]
        for k, gt in enumerate(json):
            print(gt[k])






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

def de_ratio(p1,p2,p3):

    # p = [x,y,w,h] to half dot  p1_d = [x,y]

    p1_d = [(int)(0.8*(p1[0]+((p1[2]-p1[0])/2))),(int)(0.6*(p1[1]+((p1[3]-p1[1])/2)))]
    p2_d = [(int)(0.8*(p2[0]+((p2[2]-p2[0])/2))),(int)(0.6*(p2[1]+((p2[3]-p2[1])/2)))]
    p3_d = [(int)(0.8*(p3[0]+((p3[2]-p3[0])/2))),(int)(0.6*(p3[1]+((p3[3]-p3[1])/2)))]
    ## 사진이 512x 288 로 변경됨. 비율 계산식이 필요 
    ## 세로 비율 0.6, 가로 비율 0.8

    #guide_line_box
    #os.chdir(os.path.commonprefix([os.getcwd(),os.path.dirname(os.path.realpath(__file__))])+"Depth_e/viz_predictions/images")
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

    return p1_d, p2_d, p3_d

def mse_prevent(dp1,dp2,dp3):

    os.chdir(os.path.commonprefix([os.getcwd(),os.path.dirname(os.path.realpath(__file__))])+"Depth_e/viz_predictions/images")
    print(os.getcwd())

    #dp1 = [x,y] middle point
    #initial_dp1
    i_dp1 = ([dp1[0]-25,dp1[1]-25])
    img = cv2.imread('frame00020.jpg')

    dp1_max = []
    block_s = 50 
    #cv2로 불러들인 img 좌표는 y, x 순
    s = img[i_dp1[1],i_dp1[0]]
    e_s = sum(s,0.0)/len(s)

    for i in range (0,block_s): # y축
        for k in range (0,block_s): # x 축

            p = img[i_dp1[1]+i,i_dp1[0]+k]
            e_p = sum(p,0.0)/len(p)
            if(e_s < e_p):
                s_i,s_k = i,k
                s = p
                e_s = e_p

    print('max_xpoint',i_dp1[1]+s_i,'max_ypoint',i_dp1[0]+s_k)
    print(s)

    #confirm
    cv2.circle(img,(i_dp1[0]+s_k,i_dp1[1]+s_i),2,(255,0,0),-1)
    cv2.imwrite('m_frame00020.jpg',img)


    #dp2
    i_dp2 = ([dp2[0]-25,dp2[1]-25])
    img = cv2.imread('frame00040.jpg')

    dp1_max = []
    block_s = 50 
    #cv2로 불러들인 img 좌표는 y, x 순
    s = img[i_dp2[1],i_dp2[0]]
    e_s = sum(s,0.0)/len(s)

    for i in range (0,block_s): # y축
        for k in range (0,block_s): # x 축

            p = img[i_dp2[1]+i,i_dp2[0]+k]
            e_p = sum(p,0.0)/len(p)
            if(e_s < e_p):
                s_i,s_k = i,k
                s = p
                e_s = e_p

    print('max_xpoint',i_dp2[1]+s_i,'max_ypoint',i_dp2[0]+s_k)
    print(s)

    #confirm
    cv2.circle(img,(i_dp2[0]+s_k,i_dp2[1]+s_i),2,(255,0,0),-1)
    cv2.imwrite('m_frame00040.jpg',img)



    #dp3
    i_dp3 = ([dp3[0]-25,dp3[1]-25])
    img = cv2.imread('frame00060.jpg')

    dp1_max = []
    block_s = 50 
    #cv2로 불러들인 img 좌표는 y, x 순
    s = img[i_dp3[1],i_dp3[0]]
    e_s = sum(s,0.0)/len(s)

    for i in range (0,block_s): # y축
        for k in range (0,block_s): # x 축

            p = img[i_dp1[1]+i,i_dp1[0]+k]
            e_p = sum(p,0.0)/len(p)
            if(e_s < e_p):
                s_i,s_k = i,k
                s = p
                e_s = e_p

    print('max_xpoint',i_dp3[1]+s_i,'max_ypoint',i_dp3[0]+s_k)
    print(s)

    #confirm
    cv2.circle(img,(i_dp3[0]+s_k,i_dp3[1]+s_i),2,(255,0,0),-1)
    cv2.imwrite('m_frame00060.jpg',img)

### 일단 수동적임을 말씀드립니다...추후 recursive 로 짤생각..