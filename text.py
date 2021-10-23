# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 下午 08:14
# @Author  : Kdq_soldier
# @FileName: text.py
# @Software: PyCharm

import  re
import os
import requests


def open_(path):
    data_3 = list();
    data_4 = list();
    file=open(path,encoding='UTF-8');
    data=file.read();
    # print(data)
    obj_1=re.compile(r'"data":\[(.*?)\],',re.S)
    data_=obj_1.findall(data);
    obj_2=re.compile(r'\{(.*?)\}',re.S)
    data_[0]=str(data_[0])
    data_2=obj_2.findall(data_[0]);
    # print(data_2[len(data_2)-1])
    i=0;
    while i<len(data_2):
        data_3.append(re.split(',',str(data_2[i])))
        i=i+1;
    obj_15_0 = re.compile(r'\"unit\":\"(.*?)\"')
    obj_8_1=re.compile(r'\"needHandsUnit\":\"(.*?)\"')
    obj_6_2=re.compile(r'\"jobProperties\":\"(.*?)\"')
    obj_10_3=re.compile(r'\"post\":\"(.*?)\"')
    obj_2_4=re.compile(r'\"doJob\":\"(.*?)\"')
    obj_4_5 = re.compile(r'\"forceStation\":\"(.*?)\",')
    obj_3_6 = re.compile(r'\"educationBackground\":\"(.*?)\"')
    obj_13_7 = re.compile(r'\"subject\":\"(.*?)\"')
    j=0;
    bool_=True;
    while j<len(data_3):
        k = 0;
        while k<len(data_3[j]):
            if j==0:
                if k==1:
                    data_4.append(obj_2_4.findall(data_3[j][k]))
                    k = k + 1;
                elif k==2:
                    data_4.append(obj_3_6.findall(data_3[j][k]))
                    k = k + 1;
                elif k == 4:
                    data_4.append(obj_4_5.findall(data_3[j][k]))
                    k = k + 1;
                elif k == 5:
                    data_4.append(obj_6_2.findall(data_3[j][k]))
                    k=k+1;
                elif k == 7:
                    data_4.append(obj_8_1.findall(data_3[j][k]))
                    k = k + 1;
                elif k == 9:
                    data_4.append(obj_10_3.findall(data_3[j][k]))
                    k = k + 1;
                elif k == 12:
                    data_4.append(obj_13_7.findall(data_3[j][k]))
                    k = k + 1;
                elif k == 14:
                    data_4.append(obj_15_0.findall(data_3[j][k]))
                    k = k + 1;
                else:
                    k = k + 1;
            else:
                if k==1:
                    data_4[j].append(obj_2_4.findall(data_3[j][k]))
                    k = k + 1;
                elif k==2:
                    data_4[j].append(obj_3_6.findall(data_3[j][k]))
                    k = k + 1;
                elif k == 4:
                    data_4[j].append(obj_4_5.findall(data_3[j][k]))
                    k = k + 1;
                elif k == 5:
                    data_4[j].append(obj_6_2.findall(data_3[j][k]))
                    k=k+1;
                elif k == 7:
                    data_4[j].append(obj_8_1.findall(data_3[j][k]))
                    k = k + 1;
                elif k == 9:
                    data_4[j].append(obj_10_3.findall(data_3[j][k]))
                    k = k + 1;
                elif k == 12:
                    data_4[j].append(obj_13_7.findall(data_3[j][k]))
                    k = k + 1;
                elif k == 14:
                    data_4[j].append(obj_15_0.findall(data_3[j][k]))
                    k = k + 1;
                else:
                    k = k + 1;
        j=j+1;

    return  data_4


if __name__ == '__main__':
    data_4 = list();
    path=r'listVisitor.json';
    data_4.append(open_(path))
    # print(data_3)
    path = r'listVisitor1.json';
    data_4.append(open_(path))
    print('ok')
