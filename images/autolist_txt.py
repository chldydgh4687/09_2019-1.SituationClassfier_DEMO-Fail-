from os.path import *
import glob
import os

def autolist():
    
    f = open(os.getcwd()+'/images/data_list.txt','w')
    folder=basename('/SituationClassfier_DEMO/images')
    print(basename('./SituationClassfier_DEMO/images'))
    
    #change path
    print(os.getcwd())
    os.chdir(os.getcwd()+'/images')
    print(os.getcwd())
    
    for i in glob.iglob('*.jpg'):
        data = folder + "/" + i + "\n"
        print(data)
        f.write(data)
    f.close()

    
