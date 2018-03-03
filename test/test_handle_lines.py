# -*- coding:utf-8 -*-  
'''
Created on 2018年3月1日

@author: Administrator
'''
import cv2
from PIL import Image
from  matplotlib import pyplot as plt
import matplotlib.image as mping
import numpy as np
import skimage.transform as st
import skimage.feature
from skimage import feature,filters
from scipy import misc
from PIL import ImageEnhance
from skimage.exposure.exposure import histogram
import skimage.morphology as sm
from skimage.morphology.watershed import watershed
from tools.HandleLines import handle_lines
image_path = '../TestImage/10.png'
img = Image.open(image_path).convert('L')
img = ~np.array(img)
img =misc.imresize(img, size=0.5)
_width = img.shape[1]
_height = img.shape[0]
img = sm.closing(img,sm.square(5))
_edges = feature.canny(img, sigma=1, \
    low_threshold=50, high_threshold=200)
_lines = st.probabilistic_hough_line(_edges, \
    threshold=20, line_length=_width/4, line_gap=30)
_lines = handle_lines(_lines,_width,_height)
plt.imshow(_edges*0)
for x1,y1,x2,y2 in _lines:
    plt.plot((x1,x2),(y1,y2))
row2,col2 =img.shape
plt.axis((0,col2,row2,0))
plt.show()