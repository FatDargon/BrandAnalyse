# -*- coding:UTF-8 -*-
'''
Created on 2018-2-12

@author: Administrator
'''
import cv2  
from PIL import Image  
import numpy as np
from scipy import misc
from tools.HandleLines import handle_lines
from tools.GetRect import get_rect
import random

global src
global img
global window_name
global window_name2
def HoughLinesP(minLINELENGTH):
    global src
    global img
    global window_name
    global window_name2
    edges = cv2.Canny(src, 5,100, apertureSize = 3)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180,minLINELENGTH, 50)
    tempIamge = src.copy()
    tempIamge2 = src.copy()
    picH = img.shape[1]
    picS = img.shape[0]
    ks,kh = handle_lines(lines,picH,picS)
    print "*"*20
    for x1,y1,x2,y2 in ks:
        print x1,y1,x2,y2
        cv2.circle(tempIamge,(x1,y1),5,(255,0,0),5)
        cv2.circle(tempIamge,(x2,y2),5,(255,0,0),5)
        cv2.line(tempIamge,(x1,y1),(x2,y2),(255,0,0),5)
    for x1,y1,x2,y2 in kh:
        print x1,y1,x2,y2
        cv2.circle(tempIamge,(x1,y1),5,(55,255,155),5)
        cv2.circle(tempIamge,(x2,y2),5,(55,255,155),5)
        cv2.line(tempIamge,(x1,y1),(x2,y2),(0,255,0),5)
    rest = get_rect(ks,kh,picH,picS)
    for z,x,c,v in rest:
        R = random.random()*256
        G = random.random()*256
        B = random.random()*256
        cv2.rectangle(tempIamge2,(z,x),(c,v),(R,G,B),-1)
    cv2.imshow(window_name,tempIamge)
    cv2.imshow(window_name2,tempIamge2)
# def main_show(i):
i=34
global src
global img
global window_name
global window_name2
window_name = "HoughLines"
window_name2 = "source"
cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
cv2.namedWindow(window_name2,cv2.WINDOW_NORMAL)
image_path = '../TestImage/'+str(i)+'.png'
image = Image.open(image_path).convert('1')
image = misc.imresize(image, size=0.3)
img = cv2.cvtColor(np.asarray(image),cv2.COLOR_GRAY2RGB)  
src =img
picH = img.shape[1]
picS = img.shape[0]
minLINELENGTH = picH/4
minLineLength = minLINELENGTH
trackbar_value =u'直线粒度'.encode('gbk')
max_value = picH
cv2.createTrackbar( trackbar_value, window_name, \
                    minLineLength, max_value, HoughLinesP)
HoughLinesP(22) 
if cv2.waitKey(0) == 27:  
    cv2.destroyAllWindows()