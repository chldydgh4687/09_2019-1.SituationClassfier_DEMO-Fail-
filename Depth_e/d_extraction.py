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

import os
import torch
from Depth_e.train_options import TrainOptions
from loaders import aligned_data_loader
from models import pix2pix_model
        
#from Depth_e import TrainOptions move options to Depth_e folder

BATCH_SIZE = 1

opt = TrainOptions().pars()

video_list = './images/data_list.txt'

eval_num_threads = 2
video_data_loader = aligned_data_loader.demoDataLoader(video_list, BATCH_SIZE)
video_dataset = video_data_loader.load_data()

print('=========video dataset #images = %d =========='% len(video_data_loader))

model = pix2pix_model.Pix2PixModel(opt)

torch.backends.cudnn.enabled = True
torch.backends.cudnn.benchmark = True
best_epoch = 0
global_step = 0

print('==================BEGIN VALIDATION========================')

print('TESTING ON VIDEO')

model.switch_to_eval()
save_path = 'test_data/viz_predictions/'
print('save_path %s' % save_path)

for i, data in enumerate(video_dataset):
    print(i)
    stacked_img = data[0]
    targets = data[1]
    model.run_and_save_demo(stacked_img, save_path)
    