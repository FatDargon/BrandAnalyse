# -*- coding:utf-8 -*-  
'''
Created on 2018年3月12日

@author: Administrator
'''
from PIL import Image

import matplotlib.pyplot as plt
from tools.CutImage import check_image_white
image_path = 'E:\\eclipse_python\\BrandAnalyse\\Result\\CateImage\\long\\'
import os
for filename in os.listdir(image_path):
#     print filename
    image = Image.open(image_path+filename).convert('1')
#     print image.getpixel((0,0))
    print filename  
    flag = check_image_white(image)
    if flag:
        print "11111111111111111"
# #             plt.figure("long")
# #             plt.imshow(image)
# #             plt.show()
#     else:
#         print 'white'
# #         plt.figure("white")
# #         plt.imshow(image)
# #         plt.show() 