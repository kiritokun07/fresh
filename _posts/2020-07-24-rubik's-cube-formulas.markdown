---
layout: post
title:  "Rubik'S Cube Formulas"
img: 
date:   2020-07-24 16:34:55 +0800
description: 魔方字母公式转ABC公式python小工具
---

## 魔方字母公式转ABC公式python小工具

传统魔方公式用LRUDFB这样的字母表示当前面的顺时针，加'表示逆时针。

我一直不习惯用这样的表示方法，喜欢用A←3↑这样的表示，字母为面对我这一面的第一行，有ABCDE...，数字为列，有12345...。

所以我写了个python小工具帮我转换一下公式。代码如下：

```python
import tkinter as tk
window=tk.Tk()
window.title('魔方字母公式转换ABC公式')
window.geometry('400x400') # 宽高

t=tk.Text(window,height=4)
t.pack()

def insert_text(text): #这里闭包一下
    def insert_point():
        var=text
        t.insert('insert',var)
    return insert_point

# 用一个字典来解决，↶↷乱码不要紧
button_dic={"L":"1↓","R":"3↑","U":"A←","D":"C→","F":"↷","B":"前逆","L'":"1↑","R'":"3↓","U'":"A→","D'":"C←","F'":"↶","B'":"前顺","L2":"1↓↓","R2":"3↑↑","U2":"A←←","D2":"C→→","F2":"◯","B2":"前◯","L'2":"1↑↑","R'2":"3↓↓","U'2":"A→→","D'2":"C←←","F'2":"◯","B'2":"前◯","x":"上翻","y":"左翻","z":"顺翻","x'":"下翻","y'":"右翻","z'":"逆翻"}

# "":"","":"","":"","":"","":"","":""
count=0
# 用Frame管理button
# https://blog.csdn.net/yingshukun/article/details/53983812
fm1=tk.Frame(window)
button=lambda text1,text2:tk.Button(fm1,text=text1,width=4,height=2,command=insert_text(text2))
for k,v in button_dic.items():
    myrow=int(count/6)
    mycolumn=count-myrow*6
    button(k,v).grid(row=myrow+1,column=mycolumn) # 需要添加网格分布
    count+=1

fm1.pack()
window.mainloop()
```
保存为.pyw后双击运行效果如下：

![效果图](https://i0.hdslb.com/bfs/article/5a33e42321e1466184c66afae110d8cfd9e86112.png@802w_844h.webp)

