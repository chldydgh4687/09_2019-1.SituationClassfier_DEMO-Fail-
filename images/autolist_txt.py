from os.path import *
import glob
import os

def autolist():


    f = open(os.getcwd()+'/images/data_list.txt','w')
    folder=basename('/SituationClassfier_DEMO/images')
    count = 0

    #change path
    print(os.getcwd()+"\n")
    os.chdir(os.getcwd()+'/images')
    print("changed path to"+os.getcwd()+"\n")
    
    for i in glob.iglob('*.jpg'):
        data = i + "\n"
        f.write(data)
        count=count+1
    f.close()
    print(count," found .jpg files\n") 

    print("--------------Wrtiting Success------------")

def autolist_json():

    f = open(os.getcwd() + '/images/json_data_list.txt', 'w')
    folder = basename('/SituationClassfier_DEMO/images')
    count = 0

    # change path
    print(os.getcwd() + "\n")
    os.chdir(os.getcwd() + '/images')
    print("changed path to" + os.getcwd() + "\n")

    for i in glob.iglob('*.json'):
        data = i + "\n"
        f.write(data)
        count = count + 1
    f.close()
    print(count, " found .json files\n")

    print("-------------.json Wrtiting Success-----------")

def json_loader():

    json_txt = os.getcwd() + '/json_data_list.txt'
    text_file = open(json_txt, 'r')
    json_list = text_file.readlines()
    text_file.close()
    json_list = [os.path.join(os.getcwd(), i) for i in json_list]
    return json_list