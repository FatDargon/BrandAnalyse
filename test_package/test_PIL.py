# -*- coding:utf-8 -*-  
'''
Created on 2018年2月28日

@author: Administrator
'''
from PIL import Image
from PIL import ImageEnhance
from  matplotlib import pyplot as plt


image_path = '../TestImage/1.png'
img = Image.open(image_path).convert('L')
print img
# img = ~np.array(img)#
# plt.imshow(img)
# plt.show()