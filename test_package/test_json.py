# -*- coding:utf-8 -*-  
'''
Created on 2018年3月22日

@author: Administrator
'''
import json
import re
from tools.OCR_Location import get_key, get_brand_area
from tools.OpenFile import open_file2
from tools.CutImage import cut_image, cut_area
image_path = '../Result/CateImage/normal/500good/1_3_0.98.png'
f = open('test.json','r')            
line = f.readline()
result_json = json.loads(line)        
key = get_key(result_json)
area = get_brand_area(key)
img = open_file2(image_path)
area[2]= img.size[1]
cut_area(area,img,'test')