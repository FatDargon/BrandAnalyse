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
from tools.mprint import *
from aip.ocr import AipOcr
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def get_json(image_path):
    """ 你的 APPID AK SK """
    APP_ID = '10972927'
    API_KEY = 'Gu1h92d0TY8z1IuqGSQRADZ0'
    SECRET_KEY = 'B2AUtoSzf33gRYPE0zh0MtYO9P1Kn1u3'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    image = get_file_content(image_path)
    if image:
        options = {}
        options["language_type"] = "CHN_ENG"     
        result_json = client.general(image, options)
        #     print result_json
        return result_json
    else:
        return None
def save_file(image_path):
    _json = get_json(image_path)
    _str = json.dumps(_json)
    print _str
    f = open("test.json","w")
    f.write(_str)
    f.close()
def main():   
    image_path = '../Result/CateImage/normal/1_3_4.png'#1_6_6.png
#     save_file(image_path)
    f = open('test.json','r')            
    line = f.readline()
    result_json = json.loads(line)        
    key = get_key(result_json)
    pretty_list(key)
#     print key
    area = get_brand_area(key)
    img = open_file2(image_path)
    area[2]= img.size[1]
    cut_area(area,img,'test')
main()