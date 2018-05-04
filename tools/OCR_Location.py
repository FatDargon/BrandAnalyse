# -*- coding:utf-8 -*-  
'''
Created on 2018年3月22日

@author: Administrator
'''
import json
import re
from tools.mprint import pretty_dict, pretty_list, pretty_un
_ZhuCeHao = u'注册号'
_ShangBiao = u'商标'
_ShiYongShangPin =u'使用商品'
_QiYeMingCheng =u'企业名称'
_QiYeDiZhi =u'企业地址'
_ZhuCeRiQi = u'注册日期'
_ZhuanYongQiXian = u'专用期限'
_type1 = [_ZhuCeHao,_ShangBiao, _ShiYongShangPin,_QiYeMingCheng,_QiYeDiZhi,_ZhuCeRiQi]
_type2 = [_ZhuCeHao,_ShiYongShangPin,_QiYeMingCheng,_ZhuanYongQiXian] 
def get_cate(_json):
    global _ZhuCeHao,_ShangBiao, _ShiYongShangPin,_QiYeMingCheng,_QiYeDiZhi,_ZhuCeRiQi,_ZhuanYongQiXian,_type2,_type1
    _list_words =[ item['words'] for item in _json['words_result']]
    _list_words_str = ''.join(_list_words)#     print _list_words
    tag_zch = re.findall(_ZhuCeHao, _list_words_str)#标志 记录是否有注册号  如果有 证明是正常的切分
#     print len(tag_zch)
#     print _list_words_str
    y_m_d = re.compile(u"年|月|日")
    tag_y_m_d = re.findall(y_m_d, _list_words_str)
    pretty_un( tag_y_m_d)
    if len(tag_y_m_d) < 3:
        return 4
    if len(tag_zch) >= 2:
        return 3# 多个  需要继续切分
    elif len(tag_zch)==0:
        return 0# 错误切分
    elif _ZhuanYongQiXian in _list_words_str:
        return 2
    elif _ShangBiao in _list_words_str:
        return 1
    
def get_key(_json,_type_num):
    # print json.dumps(j,indent=4)
    global _ZhuCeHao,_ShangBiao, _ShiYongShangPin,_QiYeMingCheng,_QiYeDiZhi,_ZhuCeRiQi,_ZhuanYongQiXian
    _result = []
    _num = int(_json['words_result_num'])
    if _type_num == 1:
        _type = _type1
    else:
        _type = _type2
        
    _tmp = u''
    init = 0
    _new = u''
    for i in range(int(_num)):
        _words = _json['words_result'][i]['words']
        _location = _json['words_result'][i]['location']
        item = _type[init]
        if item in _words:
            if item == _ZhuCeHao or item == _ShangBiao:
                _new = _words.replace(item,'')
                _result.append({'item':_type[init],'content':_new,'location':_location,'type':_type_num})
            elif init ==1:
                pass
            elif _type[init-1] == _ShangBiao:
                pass
            else:
                _result.append({'item':_type[init-1],'content':_new,'location':_location,'type':_type_num})
            _new = _words.replace(item,'')
            init = init + 1
        else:
            _new = _new + _words
    _result.append({'item':_type[init-1],'content':_new,'location':_location,'type':_type_num})         
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
                _area[3] = i['location']['top']-i['location']['height']-20
        if _type_num == 2:
            if i['item'] == _ZhuCeHao:
                _area[0] = i['location']['left']
                _area[1] = i['location']['top']+i['location']['height']
            elif i['item'] == _ShiYongShangPin:
                pretty_dict(i)
                _area[2] = 0
                _area[3] = i['location']['top']-i['location']['height']-20
    return _area