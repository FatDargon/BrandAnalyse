# -*- coding:utf-8 -*-  
'''
Created on 2018年3月22日

@author: Administrator
'''
import json
_ZhuCeHao = u'注册号'
_ShangBiao = u'商标'
_ShiYongShangPin =u'使用商品'
_QiYeMingCheng =u'企业名称'
_QiYeDiZhi =u'企业地址'
_ZhuCeRiQi = u'注册日期'
_ZhuanYongQiXian = u'专用期限'
_type1 = [_ZhuCeHao,_ShangBiao, _ShiYongShangPin,_QiYeMingCheng,_QiYeDiZhi,_ZhuCeRiQi]
_type2 = [_ZhuCeHao,_ShiYongShangPin,_QiYeMingCheng,_ZhuanYongQiXian]  
def get_key(_json):
    # print json.dumps(j,indent=4)
    global _ZhuCeHao,_ShangBiao, _ShiYongShangPin,_QiYeMingCheng,_QiYeDiZhi,_ZhuCeRiQi,_ZhuanYongQiXian
    _result = []
    num = int(_json['words_result_num'])

    if num <= 4:
        return None
    elif _ZhuanYongQiXian in _json['words_result'][num-1]['words']:
        _type = _type2
        _type_num = 2
    else:
        _type = _type1
        _type_num = 1
    for i in range(int(num)):
        _words = _json['words_result'][i]['words']
        _location = _json['words_result'][i]['location']
        for item in _type:
            if item in _words:
                _new = _words.replace(item,'')
                _result.append({'item':item,'content':_new,'location':_location,'type':_type_num})
                
    return _result
def get_brand_area(_result):
    global _ZhuCeHao,_ShangBiao, _ShiYongShangPin,_QiYeMingCheng,_QiYeDiZhi,_ZhuCeRiQi,_ZhuanYongQiXian
    _type_num = _result[0]['type']
    _area = [0,0,0,0]
    for i in _result:
        if _type_num == 1:
            if i['item'] == _ShangBiao:
                _area[0] = i['location']['left']
                _area[1] = i['location']['top']+i['location']['height']
            elif i['item'] == _ShiYongShangPin:
                _area[2] = 0
                _area[3] = i['location']['top']
        if _type_num == 2:
            if i['item'] == _ZhuCeHao:
                _area[0] = i['location']['left']
                _area[1] = i['location']['top']+i['location']['height']
            elif i['item'] == _ShiYongShangPin:
                _area[2] = 0
                _area[3] = i['location']['top']
    return _area