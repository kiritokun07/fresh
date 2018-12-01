---
layout: post
title:  "Git and Vscode settings"
img: bengbengbeng.jpg
date:   2018-12-01 22:30 +0800
description: 【git】设置初始工作路径以及在vscode的配置
---

>搬运自己的文章

git笔记——设置打开时的默认工作路径以及vscode的配置

情况有两种：

一种是git bash快捷方式控制路径

一种是自己惯用的编辑器，如vscode

首先git bash的设置，没啥说的，在快捷方式右键属性里面删除目录后的--cd-to-home字样，再设置起始位置如D:\git，打开git bash后发现默认工作路径已修改
<br>
![git bash属性设置](https://i0.hdslb.com/bfs/article/9583ffca3de989af3b203b023be028fb2ffe072a.png@816w_642h.webp)
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![git bash中的初始路径](https://i0.hdslb.com/bfs/article/8bbf2982ee3ea7d009b4fe1b192ad3062f983fab.png@690w_212h.webp)
<br>
接着是vscode，先打开vscode，在文件-首选项中添加相应代码。以下是我的配置（有些配置已自带，带git和terminal的应该要自己添加），可按需修改。注意斜杠需要两个相应代码可以在搜索框中搜索关键字。需要添加的代码可在左边“说明书”里搜索，将鼠标放置在代码左边点击复制到右边再进行修改~
```
{

"git.ignoreMissingGitWarning": true,

"files.autoGuessEncoding": true,

"workbench.statusBar.feedback.visible": false,

"python.pythonPath": "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe",

"window.closeWhenEmpty": true,

"git.path": "C:\\Program Files\\Git\\bin//git.exe",

"terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin//bash.exe",

"terminal.integrated.cursorBlinking": true,

"terminal.integrated.cursorStyle": "line",

"git.defaultCloneDirectory": "D:\\git",

"terminal.integrated.cwd": "D:\\git"

}
```
以下是配置情况截图，一些路径按照个人情况来。一些个人喜好配置的目录还请自行创建好。
<br>
![vscode首选项](https://i0.hdslb.com/bfs/article/44068685608b4c783206ac9fc70225dff347aa88.png@1166w_554h.webp)
说明：除最后一行的配置其余都是参照了别人的教程：
<br>
[VSCode配置Git随记](https://blog.csdn.net/weixin_40965293/article/details/80319982)
<br>
最后一行是搜索“终端”后在左边代码中碰运气找到的，之前在网上找了很久设置一大堆profile、.bashrc、config都没有用。不过这个网站的eclipse的配置给我带来一些灵感：
<br>
[修改git环境默认路径 (通过设置home环境变量来设置)](http://www.it610.com/article/2109060.htm)
<br>
如果一开始在默认路径“我的文档”有过配置，在设置新的默认初始路径后还要将.gitconfig移到自己配置的路径中来。
![vscode终端中的初始路径](https://i0.hdslb.com/bfs/article/4ac4a3f485cddf3abdd180b996d175ef3da55137.png@786w_272h.webp)
配置好了就可以使用“ctrl+~”在vscode中进行git啦~

至于git的教程可参考廖雪峰老师的官网，写的很详细，还有评论要看哦~
<br>
[廖雪峰：Git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
<br>
一边学习一边搜索其他资源补充就可以了。

本人在初学git中，如果有不对还请指教~
