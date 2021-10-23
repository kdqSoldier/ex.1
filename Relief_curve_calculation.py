# -*- coding: utf-8 -*-
# @Time : 2021/7/20 8:03
# @Author : Kdq_Soldier！！
# @FileName: Relief_curve_calculation.py
# @Software: PyCharm
import math


def jiao_hu(O):
    O_pi = (O / 180) * math.pi
    return O_pi


def calculation(Ls, R, O_pi):
    # 缓和曲线曲线要素
    # 线路转向角
    # 切垂距
    m = Ls / 2 - math.pow(Ls, 3) / (240 * math.pow(R, 2))
    # 圆曲线内移量
    P = math.pow(Ls, 2) / (24 * R)
    # 缓和曲线角  弧度
    B0 = (Ls / (2 * R))

    # 曲线综合要素
    # 切线长
    TH = m + (R + P) * math.tan(O_pi / 2)
    #曲线长
    # LH=R*

if __name__ == '__main__':
    # 缓和曲线长
    Ls = 1000;
    # 圆曲线半径
    R = 1000;
    # 转向角
    O = 568;

    calculation(Ls, R, jiao_hu(O))
