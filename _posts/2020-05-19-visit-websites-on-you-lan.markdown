---
layout: post
title:  "Visit Websites On You Lan"
img: 
date:   2020-05-19 13:33:51 +0800
description: 在局域网访问你的网站
---

在笔记本上无论是`bundle exec jekyll serve -w --host=0.0.0.0`搭建jekyll网站，

还是phpstudy创建服务器访问thinkphp（`在vhosts.conf添加ServerName 192.168.31.192`）。

在本地用ip访问都是没有问题的，但用手机连wifi总是无法访问，今天总算知道原因了。

<b>就是万恶的防火墙！</b>

方法：

控制面板-系统和安全-Windows Defender防火墙-启用或关闭防火墙-关闭专用网络设置和公用网络设置（后者我没关导致局域网不能访问笔记本的服务器）

如果还不行就百度一下怎么添加端口吧
