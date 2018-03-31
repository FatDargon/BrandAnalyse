# -*- coding:utf-8 -*-  
'''
Created on 2018年3月29日

@author: Administrator
'''
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