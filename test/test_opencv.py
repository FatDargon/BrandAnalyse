# -*- coding:UTF-8 -*-
'''
Created on 2018-2-12

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
image_path = '../TestImage/1.png'
img = Image.open(image_path).convert('L')
img = ~np.array(img)
# hist = plt.hist(img11)
# plt.imshow(img11,"gray_r")
# plt.show()
# exit(0)
# img = mping.imread(image_path,'gif')
# img = np.array(img)
# print img.shape
# img1 = ImageEnhance.Contrast(img)
# img =img1.enhance(factor=1.5)
img =misc.imresize(img, size=0.3)
img = sm.closing(img,sm.square(5))
# img = sm.erosion(img,sm.square(5))

# img1 = img[:,:,0]
# plt.imshow(img1,"gray_r")
# plt.show()
_edges = feature.canny(img, sigma=1, \
    low_threshold=50, high_threshold=200)
# _edges =filters.sobel(img)
# markers = np.zeros_like(img)
# markers[img < 30] = 1
# markers[img > 150] = 2
# _edges = watershed(img,markers)
_lines = st.probabilistic_hough_line(_edges, \
    threshold=20, line_length=20, line_gap=10)


_lines = handle_lines(_lines)
fig,(ax0,ax1,ax2)=plt.subplots(1,3,figsize=(16,9))
plt.tight_layout()
ax0.imshow(img,"gray_r")
ax0.set_title("Input Image")
ax0.set_axis_off()

ax1.imshow(_edges,"gray_r")
ax1.set_title("Canny edages")
ax1.set_axis_off()

ax2.imshow(_edges*0)
for line in _lines:
    p0,p1=line
    ax2.plot((p0[0],p1[0]),(p0[1],p1[1]))
row2,col2 =img.shape
ax2.axis((0,col2,row2,0))
ax2.set_title("Lines")
ax2.set_axis_off()
plt.show()
# plt.imshow(img)
# print img.mode
# img.show()
# img2 = img.convert('RGB')
# plt.imshow(img2)
# plt.show()
# img2.show()