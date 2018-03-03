# -*- coding:utf-8 -*-  
'''
Created on 2018年3月3日

@author: Administrator
'''
import cv2  
from PIL import Image  
import numpy as np
from scipy import misc
from tools.HandleLines import handle_lines
from tools.GetRect import get_rect
from tools.CutImage import cut_image
from tools.OpenFile import open_file
import time


def HoughLinesP(minLINELENGTH,image,size):
    image = misc.imresize(image, size)
    cv_img = cv2.cvtColor(np.asarray(image),cv2.COLOR_GRAY2RGB)  
    edges = cv2.Canny(cv_img, 5,100, apertureSize = 3)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180,minLINELENGTH, 50)
    picH = cv_img.shape[1]
    picS = cv_img.shape[0]
    ks,kh = handle_lines(lines,picH,picS)
    rest = get_rect(ks,kh,picH,picS)
    return rest
def main(image_name):
    img = open_file(image_name)
    if img ==None:
        return
    rest = HoughLinesP(162,img,0.3) 

    cut_image(rest,img,0.3,image_name)
 
 
    
time_start=time.time()
for i in range(50):
    main(i)
time_end=time.time()
print('totally cost',time_end-time_start)