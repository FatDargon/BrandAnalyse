# -*- coding:utf-8 -*-  
'''
Created on 2018年3月21日

@author: Administrator
'''
from aip import AipOcr
import json
from tools.OCR_Location import *
from tools.OpenFile import *
from tools.CutImage import cut_area
""" 你的 APPID AK SK """
APP_ID = '10972927'
API_KEY = 'Gu1h92d0TY8z1IuqGSQRADZ0'
SECRET_KEY = 'B2AUtoSzf33gRYPE0zh0MtYO9P1Kn1u3'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
    
max_pic_num=50
images_path = getallfiles(u"E:/eclipse_python/BrandAnalyse/Result/CateImage/normal/500good",max_pic_num)
i =0 
for image_path in images_path:
    i=i+1
    image = get_file_content(image_path)
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "true"
    
    """ 带参数调用通用文字识别, 图片参数为本地图片 """
    result_json = client.general(image, options)
#     print result_json
    key = get_key(result_json)
    area = get_brand_area(key)
    img = open_file2(image_path)
    area[2]= img.size[0]
    cut_area(area,img,i)
