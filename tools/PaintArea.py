# -*- coding:utf-8 -*-  
'''
Created on 2018年3月23日

@author: Administrator
'''
import matplotlib.pyplot as plt
from tools.OpenFile import open_file2
from PIL import ImageDraw 
def paint_area(area,image,image_name):
    x1 = area[0]
    y1 = area[1]
    x2 = area[2]
    y2 = area[3]
    if x1 > x2:
        region = (x2,y1,x1,y2)
    else:
        region = (x1,y1,x2,y2)
    print region
    drawObject = ImageDraw.Draw(image)  
    drawObject.rectangle(region,fill=0)
    return image
if __name__ == '__main__':   
    image_path = '../Result/500good/1_3_0.98.png'
    image = open_file2(image_path)
    img = paint_area((100,150,200,300),image,2)
    img.show()