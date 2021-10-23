import re
import xlwt


def biaotou(new_sheet,row,style):
    new_sheet.write(row, 0, "value",style);
    new_sheet.write(row, 1, "event_pro",style);
    new_sheet.write(row, 2, "uname",style);
    new_sheet.col(0).width = 10000;
    new_sheet.col(1).width = 8000;
    new_sheet.col(2).width = 8000;

def BCexcel(date_EXCEL):
    file=xlwt.Workbook();
    # new_sheet=file.add_sheet('功能-文件对照表',cell_overwrite_ok=True);
    # font={'name':'宋体','size':15}
    style=xlwt.XFStyle();
    font=xlwt.Font();
    font.name='宋体';
    font.height=250;
    style.font=font;

    i=1;
    while i<= len(date_EXCEL):
        j=0;
        while j < len(date_EXCEL[i]):
            if len(date_EXCEL[i])==1:
                new_sheet = file.add_sheet(date_EXCEL[i][j], cell_overwrite_ok=True);
                biaotou(new_sheet,i-i,style)
                k=i-i;
            else:
                new_sheet.write(k,j,date_EXCEL[i][j],style);
            j=j+1;
        k = k + 1;
        i=i+1;
    file.save('功能-文件对照表.xls')


def RegularExpression(data_EX,Expression,Parameter):
    data_EX_={};
    dictionary={'split':1,'compile':2,'Two-D':3}
    i=999999;
    if Parameter in dictionary:
        i=dictionary[Parameter];
    if i==1:
        k=1;
        while k<= len(data_EX):
            # print(data_EX_[k])
            data_EX_[k]=re.split(Expression,str(data_EX[k]).replace('["','').replace('"]','').replace("['",'').replace("']",''));
            # print(data_EX_[k])
            k=k+1;
    elif i==2:
        k=1;
        for Temporary in data_EX:
            # print(data_EX[k])
            data_EX_[k] = re.findall(Expression, Temporary);
            # print(data_EX_[k])
            k=k+1;
    elif i == 3:
        # print(data_EX[1][0])
        k=1;
        while k <= len(data_EX):
            # print(data_EX[k])
            j = 0;
            while j < len(data_EX[k]):
                if len(data_EX[k])==1:
                    # print(data_EX[k][j])
                    data_EX[k][j] = data_EX[k][j];
                elif len(data_EX[k])==3:
                    if j==0:
                        # print(data_EX[k][j])
                        data_EX[k][j] = re.findall(Expression[1], data_EX[k][j]);
                    elif j==1:
                        # print(data_EX[k][j])
                        data_EX[k][j] = re.findall(Expression[2], data_EX[k][j]);
                    elif j==2:
                        # print(data_EX[k][j])
                        data_EX[k][j] = re.findall(Expression[3], data_EX[k][j]);
                elif data_EX[k][j]=='[]':
                    data_EX[k][j]='none';

                j=j+1;
            k=k+1;
        data_EX_=data_EX;
    elif i==999999:
        data_EX_='ERROR';
    # print('*********************************************')
    return data_EX_;

if __name__ == '__main__':
    expression_3={};
    i=1;
    file=open('代码.txt','r',encoding='utf-8')
    data=file.readlines()
    file.close();
    file=open('resout.txt','w+',encoding='utf-8')
    expression_1=re.compile(r"'(.*)'")
    expression_2 = re.compile(',')
    expression_3[1]=re.compile("(.*)'")
    expression_3[2] = re.compile("'(.*)'")
    expression_3[3] = re.compile('\'(.*)')
    result=RegularExpression(data,expression_1,'compile')
    result_1 = RegularExpression(result, expression_2, 'split')
    result_2=RegularExpression(result_1,expression_3,'Two-D')
    # print(result)
    # print(result_1)
    # print(result_2)
    while i <= len(result_2):
        # print(data_EX[k])
        j = 0;
        while j < len(result_2[i]):
            file.write(str(result_2[i][j]).replace('[\'','').replace('\']',','))
            j=j+1;
        file.write('\n')
        i=i+1;
    BCexcel(result_2)
    file.close();

