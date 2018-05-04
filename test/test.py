# -*- coding:utf-8 -*-  
'''
Created on 2018年3月23日

@author: Administrator
'''
# from tools.OpenFile import getallfiles
# max_pic_num=20
# # images_path = getallfiles(u"E:/eclipse_python/BrandAnalyse/Result/CateImage/normal/500good",max_pic_num)
# images_path = getallfiles(u"K:\商标\haotm",max_pic_num)
# for image_path in images_path:
#     _tmp = image_path.split('\\')
#     print _tmp[-2]+'_'+_tmp[-1].replace(".png","")
# from PIL import Image, ImageDraw
# img = Image.open("../Result/500good/1_3_0.98.png")
# draw = ImageDraw.Draw(img)
# width,height = img.size
# draw.line(((0,0),(width-1,height-1)),fill=0)
# draw.line(((0,height-1),(width-1,0)),fill=0)
# img.show()

s = u"注册号140936商标.狮猫牌hime"
import re
r = re.compile(u"号|商")
res = re.findall(r,s)
print res[0],res[1]