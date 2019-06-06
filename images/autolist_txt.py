from os.path import *
import glob
import os

def autolist():
    print(os.getcwd()+'data_list.txt')
    f = open(os.getcwd()+'data_list.txt','w')
    print("1")
    folder=basename('./SituationClassfier_DEMO/images')
    print(basename('./SituationClassfier_DEMO/images'))
    print("1")
    for i in glob.iglob('*.jpg'):
        data = a+"/"+i+"\n"
        f.write(data)
    f.close()

    
