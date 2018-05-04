# -*- coding:utf-8 -*-  
'''
Created on 2018年3月29日

@author: Administrator
'''
from tools.OpenFile import getallfiles, open_file2
from tools.GetJson import get_json
from tools.OCR_Location import *
from tools.mprint import pretty_list
from tools.CutImage import cut_area
import os
import shutil
image_path = "../Result/CateImage/normal"
def mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print "%s not exist!"%(srcfile)
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.move(srcfile,dstfile)          #移动文件
        print "move %s -> %s"%( srcfile,dstfile)
def cut_twice(image_path):
    mymovefile(image_path,'../Result/TwiceCut/')
def main_cut_twice(max_pic_num,_path):
    images_path = getallfiles(_path,max_pic_num)
    for image_path in images_path:      
        main_cut_twice_each(image_path)       
def main_cut_twice_each(image_path):
    _tmp = image_path.split('/')
    _name = _tmp[-1].replace(".png","")
    _json = get_json(image_path)
    _type_num = get_cate(_json)
#     print _type_num
    if _type_num == 0:
        print _name + " is no words"
    elif _type_num == 3:
        print _name +" need cut twice"
        cut_twice(image_path)
    elif _type_num == 4:
        print _name +" is not complete"
    else:
        print _name +" is normal"
        _key = get_key(_json,_type_num)
#         f = open("../test_package/test.json","w+")
#         f.write(str(_key))
#         f.close()
        pretty_list(_key)
        area = get_brand_area(_key)
        img = open_file2(image_path)
        area[2]= img.size[0]-20
        cut_area(area,img,_name)
# main_cut_twice(50,"../Result/CateImage/normal/")
if __name__ == '__main__':
#     image_path = 'E:/eclipse_python/BrandAnalyse/Result/CateImage/normal/10_100_1.png'
#     main_cut_twice_each(image_path)
    main_cut_twice(20,"../Result/CateImage/normal/")
    
