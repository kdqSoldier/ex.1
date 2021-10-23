# -*- coding: utf-8 -*-
# @Time : 2021/9/27 11:14
# @Author : Kdq_Soldier！！
# @FileName: Trigdraw.py
# @Software: PyCharm

# 坐标系旋转
import math
import numpy as np
from numpy import arange

a0=np.array([43.0815,112.1701])
a1=np.array([[10,20],[10,-20],[-10,20],[-10,-20]])
a3=np.array([arange(1.0,3.0),arange(1.0,3.0),arange(1.0,3.0),arange(1.0,3.0)])
# a1=np.array([10,-20])
c0=(30/180)*math.pi
c=-(30/180)*math.pi
b0=np.array([[math.cos(c0),-math.sin(c0)],[math.sin(c0),math.cos(c0)]])
b1=np.array([[math.cos(c),-math.sin(c)],[math.sin(c),math.cos(c)]])
d0=a0.dot(b0)
i=0
for dat in a1:
    a3[i,1]=dat[1]+d0[1]
    a3[i,0]=dat[0]+d0[0]
    i=i+1
d=a3.dot(b1)
print(d)