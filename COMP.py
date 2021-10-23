# -*- coding: utf-8 -*-
# @Time : 2021/4/5 15:15
# @Author : Kdq_Soldier！！
# @FileName: COMP.py
# @Software: PyCharm
#coding:utf-8
import os
import tkinter as tk
from tkinter import filedialog
import  re

'''打开选择文件夹对话框'''
def save(savename,data):
    file = open(savename, 'w', errors='ignore');
    high=[[9999999 for i in range(3)] for j in range(len(data))];
    len1=len(data);
    len2=len(data[0]);
    i=0;
    while i<len1:
        j=0;
        while j<len2:
            if data[i][j]!=0:
                high[i][0]=(i);
                high[i][1]=(j);
                high[i][2]=(data[i][j]);
            j=j+1;
        i=i+1;

    i = 0;    k=9999999;
    while i < len (high):
        if high[i][1]==9999999:
            i = i + 1;
        else:
            if high[i][0] != k-1:
                k=high[i][0]+1;
                file.write("---------------------第  "+str(high[i][0]) +"  列---------------------\n")
                file.write("行： "+str(high[i][1]) +"       "+str(high[i][2])+"\n")
            else:
                file.write("行： "+str(high[i][1]) +"       "+str(high[i][2])+"\n");
            i = i + 1;

    i = 0;
    while i < len1:
        j = 0;
        while j < len2:
            if data[i][j]==0:
                file.write('%5.2f'%float(data[i][j])+"  ")
            else:
                file.write('%10.15f'%float(data[i][j])+"   ")

            j = j + 1;
        i = i + 1;
        file.write('\n');

    file.close();

def compare_event(data1,data2):
    i=0;
    if len(data1)==len(data2)and len(data1[1])==len(data2[1]) :
        compare_=[[0 for i in range(len(data1[0]))] for j in range(len(data1))];
        while i<len(data1):
            j=0;
            while j<len(data1[1]):
                compare_[i][j]=float(data1[i][j])-float(data2[i][j]);
                j=j+1;
            i=i+1;

    return  compare_;

def read(filename):
    data_=list();
    file = open(filename, 'r', errors='ignore');
    data=file.readlines();
    for data1 in data:
        data1=data1.replace('         ',' ').replace('        ',' ').replace('       ',' ').replace('      ',' ').replace('     ',' ').replace('    ',' ');
        data1=data1.replace('   ',' ').replace('  ',' ').replace(' ',' ').replace('\n','');
        data_.append(re.split(' ',data1))
    data_1= [[0 for i in range(len(data_[0])-1)] for j in range(len(data_))];
    i = 0;
    while i<len(data_):
        j=1;
        while j<len(data_[0]) :
            data_1[i][j-1]=(data_[i][j]);
            j=j+1;
        i=i+1;
    return  data_1;
def getfile(cans):
    root = tk.Tk()
    if cans=='in1':
        root.title('差值文件1')
    elif cans=='in2':
        root.title('差值文件2')
    elif cans=='out':
        root.title('差值成果文件')
    root.withdraw()
    # Folderpath = filedialog.askdirectory()  # 获得选择好的文件夹
    Filepath = filedialog.askopenfilename()  # 获得选择好的文件
    return Filepath


if __name__ == '__main__':
    print('-------------差值计算-------------')
    ok='jhbvgfpinged'
    ok = input("按任意键开始选择文件计算！！！！！\n");
    if ok!="jhbvgfpinged":
        can='y';
        while 1:
            if can=="y"or can=="Y":
                print('  输入差值文件1\n')
                filename_1 = getfile('in1');
                print(filename_1 + '\n  输入差值文件2\n')
                filename_2 = getfile('in2');
                print(filename_2 + '\n  差值成果文件路径\n\n')
                save_ = getfile('out');
                save(save_,compare_event(read(filename_1),read(filename_2)));
                print('========计算完成！！！！！========\n')
                can=input("是否继续，退出！！！（Y,N）");
            elif can=="n"or can=="N":
                break;
            else:
                print('无法识别输入，请重新输入！！！！');
                can=input("是否继续，退出！！！（Y,N）");

        # BCexcel(dataget(pathName),WpathName)