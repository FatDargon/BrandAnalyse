# -*- coding:utf-8 -*-  
'''
Created on 2018年2月28日

@author: Administrator
'''
import numpy as np
from PIL import Image
from skimage import data, feature
from skimage import io,transform 
from  matplotlib import pyplot as plt
from skimage.util.dtype import img_as_uint
from skimage.morphology.watershed import watershed


image_path = '../TestImage/11.png'
img = Image.open(image_path).convert('L')
img = ~np.array(img)
_edges = feature.canny(img, sigma=1, \
    low_threshold=20, high_threshold=230, mask=None, use_quantiles=False)
plt.imshow(_edges)
plt.show()