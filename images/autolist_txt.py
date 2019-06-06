from os.path import *
import glob
import os

def autolist():
    f = open(os.getcwd()+'data_list.txt','w')
    folder=basename('./SituationClassfier_DEMO/images')
    for i in glob.iglob('*.jpg'):
        data = a+"/"+i+"\n"
        f.write(data)
    f.close()

    
