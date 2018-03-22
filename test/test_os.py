# -*- coding:utf-8 -*-  
'''
Created on 2018年3月22日

@author: Administrator
'''
import os
  
# for (root, dirs, files) in os.walk(u"I:\商标\haotm\haotm\1"):#  列出windows目录下的所有文件和文件名
#     for filename in files:
#         print os.path.join(root,filename)
#     for dirc in dirs:
#         print os.path.join(root,dirc)
#                 
                
def getallfiles(path,num):
    allfile=[]
    for dirpath,dirnames,filenames in os.walk(path): 
        for name in filenames:
            newDir =os.path.join(dirpath, name)
            if newDir and(os.path.splitext(newDir)[1] in ['.png']):
                allfile.append(newDir)
            if len(allfile) >num:
                return allfile
    return allfile
print getallfiles(u"I:\商标\haotm",200)

# Const_Image_Format = [".jpg",".jpeg",".bmp",".png"]
# class FileFilt:
#     fileList = [""]
#     counter = 0
#     def __init__(self):
#         pass
#     def FindFile(self,dirr,filtrate = 1):
#         global Const_Image_Format
#         for s in os.listdir(dirr):
#             newDir = os.path.join(dirr,s)
#             if os.path.isfile(newDir):
#                 if filtrate:
#                         if newDir and(os.path.splitext(newDir)[1] in Const_Image_Format):
#                             self.fileList.append(newDir)
#                             self.counter+=1
#                 else:
#                     self.fileList.append(newDir)
#                     self.counter+=1
# 
# if __name__ == "__main__":
#         b = FileFilt()
#         b.FindFile(dirr = u"I:\商标\haotm\haotm")
#         print(b.counter)
#         for k in b.fileList:
#             print k