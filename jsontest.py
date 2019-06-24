import os
import cv2
import sys
import os.path
import numpy as np
from read_write import VTP
from Depth_e import test_davis_videos
from Object_d import detection
from images import autolist_txt

autolist_txt.autolist_json()
json_list=autolist_txt.json_loader()
detection.detection(json_list)