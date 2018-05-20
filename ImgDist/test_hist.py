# -*- coding:utf-8 -*-  
'''
Created on 2018年5月9日

@author: Administrator
'''
from tools.OpenFile import getallfiles
from ImgDist.histsimilar import calc_similar_by_path, make_doc_data
def HistDist(max_pic_num,_pass,_path):
    images_path = getallfiles(_path,max_pic_num+_pass)
    image_path_1 = images_path[0]
    i =-1
    for image_path in images_path:
        i=i+1
        if i< _pass:
            continue
        else :
            make_doc_data(image_path_1,image_path)
            print image_path_1,image_path
            print calc_similar_by_path(image_path_1,image_path)
if __name__ == '__main__':
    HistDist(100,0,"../Result/Area/")