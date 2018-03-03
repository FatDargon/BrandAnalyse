# -*- coding:utf-8 -*-  
'''
Created on 2018年2月28日

@author: Administrator
'''
from skimage import io,transform 
from  matplotlib import pyplot as plt


image_path = '../TestImage/11.png'
img_file2 = io.imread(image_path)
from PIL import Image, ImageFilter

im = Image.open(image_path).convert('L')
# 高斯模糊
im.filter(ImageFilter.GaussianBlur).save(r'../Result/GaussianBlur.jpg')
# 普通模糊
im.filter(ImageFilter.BLUR).save(r'../Result/BLUR.jpg')
# 边缘增强
im.filter(ImageFilter.EDGE_ENHANCE).save(r'../Result/EDGE_ENHANCE.jpg')
# 找到边缘
im.filter(ImageFilter.FIND_EDGES).save(r'../Result/FIND_EDGES.jpg')
# 浮雕
im.filter(ImageFilter.EMBOSS).save(r'../Result/EMBOSS.jpg')
# 轮廓
im.filter(ImageFilter.CONTOUR).save(r'../Result/CONTOUR.jpg')
# 锐化
im.filter(ImageFilter.SHARPEN).save(r'../Result/SHARPEN.jpg')
# 平滑
im.filter(ImageFilter.SMOOTH).save(r'../Result/SMOOTH.jpg')
# 细节
im.filter(ImageFilter.DETAIL).save(r'../Result/DETAIL.jpg')