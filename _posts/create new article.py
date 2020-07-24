#coding=utf-8
# 安装好python3设置好环境后，可直接双击此脚本打开
# 运行脚本输入标题，可以带空格
import time,datetime

datetime0=datetime.datetime.now()
datetime1=datetime0.strftime('%Y-%m-%d')
datetime2=datetime0.strftime('%Y-%m-%d %H:%M:%S')


title1=input("please input title(文件名不支持中文): ")
title2=title1.split()
title3=('-'.join(title2))
name=str(datetime1)+"-"+title3.lower()

print("---")
print("layout: post")
print('title:  "'+title1.title()+'"')
print("img: ")
print("date:   ")
print("description: ")
print("---\n")
filename=name+'.markdown'
with open(filename,'w') as file_object:
    file_object.write("---\n")
    file_object.write("layout: post\n")
    file_object.write('title:  "'+title1.title()+'"\n')
    file_object.write("img: "+"\n")
    file_object.write("date:   "+datetime2+" +0800\n")
    file_object.write("description: "+"\n")
    file_object.write("---\n\n")

time.sleep(2)