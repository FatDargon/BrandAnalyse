# -*- coding:utf-8 -*-  
'''
Created on 2018年3月3日

@author: Administrator
'''
global new_kh
global rest
def find_next(now):
    global new_kh
    kh = new_kh
    global rest
#     print now
    if now[0] == now[2]:
        return
    for i in range(len(kh)):
        if kh[i][1] <= now[1]:
            continue
        if (now[0] >= kh[i][2]) | (now[2] <= kh[i][0]):
            continue
        rest.append([max(now[0],kh[i][0]), now[1], min(now[2],kh[i][2]), kh[i][3]])
        find_next([now[0], now[1],max(now[0],kh[i][0]), now[3]])
        find_next([min(now[2],kh[i][2]),now[1], now[2], now[3]])
        break
    
def get_rect(ks,kh,width,height):
    global new_kh
    global rest 
    new_kh = kh
    rest =[]
    for i in range(len(new_kh)-1):
        if i != len(new_kh)-1:
            find_next(new_kh[i])
    return rest
    