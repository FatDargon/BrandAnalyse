# -*- coding:utf-8 -*-  
'''
Created on 2018年3月23日

@author: Administrator
'''
from tools.OpenFile import getallfiles
max_pic_num=2
images_path = getallfiles(u"E:/eclipse_python/BrandAnalyse/Result/CateImage/normal/500good",max_pic_num)
print images_path