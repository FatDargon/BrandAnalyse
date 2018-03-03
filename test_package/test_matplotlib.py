# -*- coding:utf-8 -*-  
'''
Created on 2018年2月28日

@author: Administrator
'''
from  matplotlib import pyplot as plt
import matplotlib.image as mping
import numpy as np

image_path = '../TestImage/1.png'
# img = Image.open(image_path).convert('L')
# img = ~np.array(img)
img = mping.imread(image_path,'gif')
print img

img = np.array(img)
print img.shape
# plt.imshow(img)
# plt.show()