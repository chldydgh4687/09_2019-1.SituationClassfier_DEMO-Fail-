from os.path import *
import glob
import os

def autolist():
    
    f = open(os.getcwd()+'/images/data_list.txt','w')
    folder=basename('/SituationClassfier_DEMO/images')
    count = 0

    #change path
    print(os.getcwd())
    os.chdir(os.getcwd()+'/images')    
    for i in glob.iglob('*.jpg'):
        data = folder + "/" + i + "\n"
        f.write(data)
        count=count+1
    f.close()
    print(count + "find .jpg files\n") 
    print("--------------Wrtiting Success------------")
    
