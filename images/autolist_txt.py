from os.path import *
import glob
import os

def autolist():
    
    f = open(os.getcwd()+'/data_list.txt','w')
    folder=basename('/SituationClassfier_DEMO/images')
    print(basename('./SituationClassfier_DEMO/images'))
    print("1")
    for i in glob.iglob('*.jpg'):
        data = folder + "/" + i + "\n"
        f.write(data)
    f.close()

    
