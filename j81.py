# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 下午 07:29
# @Author  : Kdq_soldier
# @FileName: j81.py
# @Software: PyCharm

import  re
import  requests

i=1;
data=list();
obj_1=re.compile(r'"data":\[.*?\],',re.S)
while i<=50:
    url='http://211.166.76.109/enroll/post/listVisitor?page='+str(i)+'&limit=50&post=';
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'};
    data_=obj_1.findall(requests.get(url,headers=headers).text);
    # data_1=str(data_).replace('\n','').replace('\t','');
    data.append(data_);
    i=i+1;


