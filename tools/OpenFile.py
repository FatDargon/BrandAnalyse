# -*- coding:utf-8 -*-  
'''
Created on 2018年3月3日

@author: Administrator
'''
from PIL import Image  
def open_file(image_name):
    '''
    return image in PIL
    '''
    image_path = '../TestImage/'+str(image_name)+'.png'
    try:
        image = Image.open(image_path).convert('L')
    except:
        print "open image fail : "+str(image_name)+'.png'
        return
    return image