# -*- coding:utf-8 -*-  
'''
Created on 2018年3月23日

@author: Administrator
'''
from tools.OpenFile import getallfiles
max_pic_num=20
# images_path = getallfiles(u"E:/eclipse_python/BrandAnalyse/Result/CateImage/normal/500good",max_pic_num)
images_path = getallfiles(u"K:\商标\haotm",max_pic_num)
for image_path in images_path:
    _tmp = image_path.split('\\')
    print _tmp[-2]+'_'+_tmp[-1].replace(".png","")