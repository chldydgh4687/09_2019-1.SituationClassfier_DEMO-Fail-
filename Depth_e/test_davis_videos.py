# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import torch
import cv2
from .options import train_options 
from .loaders import aligned_data_loader
from .models import pix2pix_model
import os

def td_Depth():
    BATCH_SIZE = 1
    opt = train_options.TrainOptions().parse()  # set CUDA_VISIBLE_DEVICES before import torch

    video_list = os.getcwd()+'/data_list.txt'
    print(os.getcwd()+'/data_list.txt')

    eval_num_threads = 2
    video_data_loader = aligned_data_loader.DAVISDataLoader(video_list, BATCH_SIZE)
    video_dataset = video_data_loader.load_data()
    print('========================= Video dataset #images = %d =========' %
          len(video_data_loader))
    model = pix2pix_model.Pix2PixModel(opt)
    print("nework s")
    torch.backends.cudnn.enabled = True
    torch.backends.cudnn.benchmark = True
    best_epoch = 0
    global_step = 0

    print('=================================  BEGIN VALIDATION =====================================')
    print('TESTING ON VIDEO')

    model.switch_to_eval()
    save_path = os.getcwd()+'/viz_predictions/'
    print('save_path %s' % save_path)

    for i, data in enumerate(video_dataset):
        print(i)
        stacked_img = data[0]
        targets = data[1]
        model.run_and_save_DAVIS(stacked_img, targets, save_path)
        
def D_mpointbox(rect, rect2):
    os.chdir(os.path.commonprefix([os.getcwd(),os.path.dirname(os.path.realpath(__file__))])+"Depth_e/viz_predictions/images")
    print('this path :'+os.getcwd())
    img = cv2.imread('frame00020.jpg')
    cv2.rectangle(img,(220,0),(320,300), (255,0,0), 3)

     cv2.imwrite('t_frame00020.jpg',img)
    
    img = cv2.imread('frame00040.jpg')
    cv2.rectangle(img,(rect[0],rect[1]),(rect[2],rect[3]), (255,0,0), 3)

    cv2.imwrite('t_frame00040.jpg',img)  
    
    img = cv2.imread('frame00060.jpg')
    cv2.rectangle(img,(rect2[0],rect2[1]),(rect2[2],rect2[3]), (255,0,0), 3)
    
    cv2.imwrite('t_frame00060.jpg',img)


def D_mpoint(rect,rect2):
    #rect=[x,y,w,h]
    os.chdir(os.path.commonprefix([os.getcwd(),os.path.dirname(os.path.realpath(__file__))])+"Depth_e/viz_predictions/images")
    img = cv2.imread('frame00020.jpg')
    cv2.circle(img,(270,150),1, (255,0,0), -1)
    cv2.imwrite('m_frame00020.jpg',img)

    img = cv2.imread('frame00040.jpg')
    cv2.circle(img,(rect[0]+(rect[2]-rect[0])/2,rect[1]+(rect[2]-rect[1])/2),1,(255,0,0),-1)
    cv2.imwrite('m_frame00040.jpg',img)

    img = cv2.imread('frame00060.jpg')
    cv2.circle(img,(rect2[0]+(rect2[2]-rect2[0])/2,rect2[1]+(rect2[2]-rect2[1])/2),1,(255,0,0),-1)
    cv2.imwrite('m_frame00060.jpg',img)
