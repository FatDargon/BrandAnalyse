# -*- coding:utf-8 -*-  
'''
Created on 2018年3月3日

@author: Administrator
'''
from PIL import Image  
import os
def cut_image(rest,image,size,image_name):
    print image.size
    result_path ='../Result/CutImage/'+str(image_name)
    if not os.path.exists(result_path):
        os.makedirs(result_path)  
    for i in range(len(rest)):
        x1 = rest[i][0]
        y1 = rest[i][1]
        x2 = rest[i][2]
        y2 = rest[i][3]
#         print x1,y1,x2,y2
        if x1 > x2:
            region = (x2//size-1,y1//size-1,x1//size,y2//size)

        #box = (left, top, left+width, top+height)
        #(2172, 3130)
        #1679.0 1932.0 1083.0 2800.0
        #1082.0 1932.0 2170.0 2800.0
        else:
            region = (x1//size-1,y1//size-1,x2//size,y2//size)
        #裁切图片
        cropImg = image.crop(region)  
        #保存裁切后的图片
        cropImg.save(result_path+'/'+str(image_name)+'_'+str(i)+'.png')
    print "Done!"