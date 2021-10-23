# -*- coding: utf-8 -*-
# @Time : 2021/4/21 17:59
# @Author : Kdq_Soldier！！
# @FileName: get.py
# @Software: PyCharm
#coding:UTF-8
import os
import xlwt

# def BCexcel(subfolderss,WpathName):
#     file=xlwt.Workbook();
#     new_sheet=file.add_sheet('方法表',cell_overwrite_ok=True);
#     # font={'name':'宋体','size':15}
#     style=xlwt.XFStyle();
#     font=xlwt.Font();
#     font.name='宋体';
#     font.height=250;
#     style.font=font;
#     i=0;
#     while i < len(subfolderss):
#         new_sheet.write(i, 1, subfolderss[i+1], style);
#         i=i+1;
#     file.save(WpathName)


def datawrite(pathname,filename_,WpathName):
    file_ = open(WpathName, 'a+',encoding='utf-8');  # encoding='utf-8'
    file_.seek(0.0);
    file_.truncate();
    for filename in filename_:
        i=1;j=1;
        file = open(pathname+'\\'+filename, 'r',errors='ignore',encoding='utf-8');
        data=file.read();
        file.close();
        while i <= 3:
            file_.write('\n')
            i = i + 1;
        file_.write('====   ====    ====    ====    ====    ====    ====   ====    ====    ====    ====    ====' + '\n')
        file_.write('   NAME:');
        while i<=10:
            file_.write( '      ')
            i=i+1;
        file_.write(filename + '\n');
        file_.write('====   ====    ====    ====    ====    ====    ====   ====    ====    ====    ====    ===='+'\n')
        while j<=3:
            # file_.write( '\n')
            j=j+1;
        file_.write(data);
    file_.close();

    return print('ok')

def dataget(pathName):
    subfolderss={};
    folderNames={};
    i = 1;
    for folderName, subfolders, filenames in os.walk(pathName):
        # print('\n-----------------------')
        # print('The current folder is ' + folderName)
        # for subfolder in subfolders:
        #     print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for subfolder in subfolders:
            # print("FILE INSIDE " + folderName + ': ' + filename)
            subfolderss[i]=subfolder;
            folderNames[i] =folderName;
            i=i+1;
    # return subfolderss;
    return  filenames;

if __name__ == '__main__':

         pathName =r'D:\Python_data\pl3' ;
         WpathName =r'D:\Python_data\pl3\zong3.f90';

         datawrite(pathName, dataget(pathName), WpathName);  # 合并文件


    # BCexcel(dataget(pathName),WpathName)


