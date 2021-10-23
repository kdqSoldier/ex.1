# -*- coding: utf-8 -*-
# @Time : 2021/8/17 8:17
# @Author : Kdq_Soldier！！
# @FileName: text2.py
# @Software: PyCharm

def read (path,path_w):
    data_all=list()
    data_oth = list()
    file= open(path,encoding='UTF-8')
    data=file.readlines();
    i=0;
    while i<len(data):
        data[i]=data[i].split("\t")
        i=i+1

    file_w = open(path_w,"w+")
    i=0;
    while i<len(data):
       if i==0:
           data_oth.append(data[i])
           i = i + 1
       elif data[i][0]==data[i-1][0]:
           data_oth.append(data[i])
           i=i+1
       else :
           da=list()
           da=data_oth
           data_all.append(data_oth)
           data_oth.clear()
           data_oth.append(data[i])
           i = i + 1
    w(data)
    file.close()
    file_w.close()

def w(file_w,dat):
    file_w.write("line")
    file_w.write("0,0")
    file_w.write("0,200")
    file_w.write("pline")

if __name__=="__main__":
    path=r"C:\Users\ThinkPad\Desktop\断面.txt"
    path_w=r"C:\Users\ThinkPad\Desktop\断面1.txt"

    read(path,path_w);

    # i=1
    # for i in range(1,10):
    #     j=1
    #     while j<=i:
    #         print(str(i),"X",str(j),"=",str(i*j),end="    ")
    #         j=j+1
    #     print()

