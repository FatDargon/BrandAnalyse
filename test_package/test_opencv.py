# -*- coding:utf-8 -*-  
'''
Created on 2018年2月28日

@author: Administrator
'''
import cv2
image_path = '../Result/test/BLUR.jpg'
im = cv2.imread(image_path)
cv2.imshow("123",im)
#出错 不支持gif格式