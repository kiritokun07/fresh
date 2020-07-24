---
layout: post
title:  "Python Ocr"
img: 
date:   2020-06-05 17:25:02 +0800
description: 用python进行验证码ocr识别
---

需求：用python识别验证码
环境：win10，python3.7.2 64位（需提前安装好并换源，换源方法见文末）
工具：tesseract python的tesserocr和pytesseract库

度盘链接：https://pan.baidu.com/s/1vDWRuNmpFgliOmWntYkWVg 提取码：4zxg

## 安装tesseract
在下面链接获得tesseract
https://digi.bib.uni-mannheim.de/tesseract/
tesseract-ocr-setup-3.05.01-20170602.exe（我用idm下载了好久）
tesseract是tesserocr和pytesseract的基础
安装时如果选择Chinese语言包需要在线下载文件，因为没有合适网络环境就跳过
默认安装在C:\Program Files (x86)\Tesseract-OCR下
这时参考文章：https://blog.csdn.net/zoujin6649/article/details/82697031
添加环境变量和系统变量：
此电脑右键-属性-高级系统设置-高级-环境变量
在用户变量的Path里添加环境变量C:\Program Files (x86)\Tesseract-OCR
添加系统变量：变量名为TESSDATA_PREFIX，值为C:\Program Files (x86)\Tesseract-OCR

此时下载image.png（文字截图：Python3WebSpider）到桌面
图片来自：https://blog.csdn.net/Nancyfish/article/details/105037665的https://img-blog.csdnimg.cn/20200322231827840.png
在桌面打开cmd（我用bandizip添加了右键打开命令提示符功能，也可以shift+右键打开，总之打开的黑框要把当前路径调到和图片一个路径下）
使用命令行测试tesseract image.png result 识别图片并将结果输出到result.txt
这时可以看到桌面多了一个result.txt文件，打开一看正是Python3WebSpider字样
表明tesseract.exe的路径的确写入了环境变量

## 接下来测试python的tesserocr和pytesseract（不推荐用tesserocr）
测试图片为validatecode.jpg，是国家自然基金上的测试验证码
可以不断刷新下面网址获得不同的验证码
https://isisn.nsfc.gov.cn/egrantindex/validatecode.jpg

## tesserocr
*tesserocr*库需要在https://github.com/simonflueckiger/tesserocr-windows_build/releases下载你的python版本对应的release版
我的环境是python3.7.2 64位，所以我下载了tesserocr-2.4.0-cp37-cp37m-win_amd64.whl
cmd控制台到本地，输入pip install tess...（后面直接tab键补全文件名，此为相对路径，或直接拖文件到黑框里得到绝对路径）
回车安装之，在ipython中测试：import tesserocr 没报错即导入成功
```
import tesserocr
print(tesserocr.file_to_text('image.png'))
```
import tesserocr
from PIL import Image
image = Image.open('image.png')
print(tesserocr.image_to_text(image))

出现错误,解决方法可以看这篇文章https://blog.csdn.net/killvoon/article/details/83473277
将C:\Program Files (x86)\Tesseract-OCR的tessdata文件夹
复制到python.exe同目录，这个目录可以在开始菜单找python3.7然后右键打开快捷方式对应目录
TESSDATA_PREFIX改为C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Scripts\tessdata
这篇文章说不推荐使用tesserocr https://www.cnblogs.com/zhangxinqi/p/9297292.html

## pytesseract
*pytesseract*安装可以直接`pip install pytesseract`在清华源获得下载
通过这篇文章提到的方法来测试https://www.jianshu.com/p/bc6774723003
代码如下：
简单版↓
```
import pytesseract
from PIL import Image
img = Image.open('image.png')
print(pytesseract.image_to_string(img))
```
复杂版↓
```
# Python 实现识别弱图片验证码
# https://www.jianshu.com/p/bc6774723003
from PIL import Image
'''
获取图片
'''
def getImage(fileName='validatecode.jpg'):
    fileName = fileName
    img = Image.open(fileName)
    # 打印当前图片的模式以及格式
    print('未转化前的: ', img.mode, img.format)
    # 使用系统默认工具打开图片
    # img.show()
    return img

'''
1) 将图片进行降噪处理, 通过二值化去掉后面的背景色并加深文字对比度
'''
def convert_Image(img, standard=127.5):
    '''
    【灰度转换】
    '''
    image = img.convert('L')

    '''
    【二值化】
    根据阈值 standard , 将所有像素都置为 0(黑色) 或 255(白色), 便于接下来的分割
    '''
    pixels = image.load()
    for x in range(image.width):
        for y in range(image.height):
            if pixels[x, y] > standard:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return image

import pytesseract
import re
'''
使用 pytesseract 库来识别图片中的字符
'''
def change_Image_to_text(img):
    '''
    如果出现找不到训练库的位置, 需要我们手动自动
    语法: tessdata_dir_config = '--tessdata-dir "<replace_with_your_tessdata_dir_path>"'
    '''
    #testdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    textCode = pytesseract.image_to_string(img)#, lang='eng', config=testdata_dir_config
    # 去掉非法字符，只保留字母数字
    textCode = re.sub("\W", "", textCode)
    return textCode

def main():
    img = convert_Image(getImage())
    print('识别的结果：', change_Image_to_text(img))

if __name__ == '__main__':
    main()

```
这段代码可以直接运行成功（文章里的有点小问题），前提是将这段代码保存成`xx*py`文件并与测试图片放在一个路径并在控制台输入`python xx*py`运行
复杂版测试的是validatecode.jpg，如果不二值化处理直接image_to_string()识别也是可以的，但如果验证码再复杂点可能识别率会下降
文章中还指出要手动指定本地 Tesseract 的路径
用everything搜索pytesseract.py文件
一般安装在C:\Program Files (x86)\Python35-32\Lib\site-packages\pytesseract\pytesseract.py
用notepad++打开之，搜索tesseract_cmd修改其值
```
tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
```
问题：ocr识别会把5识别成s，目前不清楚有什么更好的办法，可能要自己搭建cnn训练？

## PLUS

## python换源方法
安装好python设置好环境变量后
将下面这段文字保存成pip_source.py，双击之
```
#!/usr/bin/python
# coding: utf-8
# 给pip换清华源

import platform
import os

os_type = platform.system()
if "Linux" == os_type:
    fileDirPath = "%s/.pip" % os.path.expanduser('~')
    filePath = "%s/pip.conf" % fileDirPath
    if not os.path.isdir(fileDirPath):
        os.mkdir(fileDirPath)
    fo = open(filePath, "w")
    fo.write(
        "[global]\nindex-url=https://pypi.tuna.tsinghua.edu.cn/simple/\n[install]\ntrusted-host=pypi.tuna.tsinghua.edu.cn\n")
    fo.close()
    print ("Configuration is complete")
elif "Windows" == os_type:
    fileDirPath = "%s\\pip" % os.path.expanduser('~')
    filePath = "%s\\pip.ini" % fileDirPath
    if not os.path.isdir(fileDirPath):
        os.mkdir(fileDirPath)
    fo = open(filePath, "w")
    fo.write(
        "[global]\ntimeout = 6000\nindex-url=https://pypi.tuna.tsinghua.edu.cn/simple/\n[install]\ntrusted-host=pypi.tuna.tsinghua.edu.cn\n")
    fo.close()
    print ("Configuration is complete")
else:
    exit("Your platform is unknow!")

input()
```



