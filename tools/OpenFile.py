# -*- coding:utf-8 -*-  
'''
Created on 2018年3月3日

@author: Administrator
'''
from PIL import Image  
import os
def open_file(image_name):
    '''
    return image in PIL
    '''
    image_path = '../TestImage/'+str(image_name)+'.png'
    try:
        image = Image.open(image_path).convert('1')
    except:
        print "open image fail : "+str(image_name)+'.png'
        return
    return image


def getallfiles(path,max_pic_num):
    allfile=[]
    for dirpath,dirnames,filenames in os.walk(path): 
        for name in filenames:
            newDir =os.path.join(dirpath, name)
            if newDir and(os.path.splitext(newDir)[1] in ['.png']):
                allfile.append(newDir)
            if len(allfile) >max_pic_num:
                return allfile
    return allfile

def open_file2(image_path):
    try:
        image = Image.open(image_path).convert('1')
    except:
        print u"open image fail : "+image_path
        return
    return image
