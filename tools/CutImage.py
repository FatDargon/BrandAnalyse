# -*- coding:utf-8 -*-  
'''
Created on 2018年3月3日

@author: Administrator
'''
from PIL import Image  
import os
import math
from PIL.Image import fromarray
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
    
    
    
    
def check_image_white(image):
#     print image.size[0],image.size[1]
    count  =0 
    for x in range(image.size[0]//4,image.size[0]*3//4):
        for y in range(image.size[1]//4,image.size[1]*3//4):
            if image.getpixel((x,y))==255:
                count = count+1
    k =(1-4.0*count/(image.size[1]*image.size[0]))*1000
    print count,k
#     print "white rate "+str(k)
    if k<1:
        return False           
    return True
def cate_image(img_small,x1,y1,x2,y2):
    
    _width = math.fabs(x1-x2)
    _height =math.fabs(y1-y2)
    if x1>x2:
        region =(x2,y1,x1,y2)
    else:
        region = (x1,y1,x2,y2)
    img_small = fromarray(img_small,'1')
#     print img_small.size
    cropImg =img_small.crop(region)
    k = _width*1.00/_height
    k = round( k , 2 )
    if 0.3<k and k<2:
#         print _width,_height,"normal",k
        return "normal",k
    elif 2<k and k<8:
        if check_image_white(cropImg):   
#             print _width,_height,"long",k
            return "long",k
        else:
#             print _width,_height,"white",k
            return "white",k        
    else:
#         print _width,_height,"wrong",k
        return "wrong",k
    
        
def cut_image_2(rest,image,img_small,size,image_name):
#     print image.size
   
    for i in range(len(rest)):
        x1 = rest[i][0]
        y1 = rest[i][1]
        x2 = rest[i][2]
        y2 = rest[i][3]
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
        image_cate,k = cate_image(img_small,x1,y1,x2,y2)
        result_path = '../Result/CateImage'+'/'+str(image_cate)
        if not os.path.exists(result_path):
            os.makedirs(result_path)  
        #保存裁切后的图片
        cropImg.save(result_path+'/'+str(i)+'_'+str(image_name)+'_'+str(k)+'.png')
    print "Done!"
def cut_area(area,image,image_name):
    x1 = area[0]
    y1 = area[1]
    x2 = area[2]
    y2 = area[3]
    if x1 > x2:
        region = (x2,y1,x1,y2)
    else:
        region = (x1,y1,x2,y2)
    cropImg = image.crop(region)  
    result_path = '../Result/Area'
    if not os.path.exists(result_path):
        os.makedirs(result_path)  
    cropImg.save(result_path+'/'+str(image_name)+'.png')