from os.path import *
import glob

def autolist():
    f = open('./SituationClassfier_DEMO/data_list.txt','w')
    folder=basename('C:/Users/user/Desktop/autopath_txt/image')
    for i in glob.iglob('*.jpg'):
        data = a+"/"+i+"\n"
        f.write(data)
    f.close()

    
