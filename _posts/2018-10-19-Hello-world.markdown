---
layout: post
title:  "Hello world!!"
img: example1.jpg
date:   2018-10-19 11:44:00 +0800
description: Hello world.
---
言叶之庭
<br>
$\sum_{i=0}^N\int_{a}^{b}g(t,i)\text{d}t$
<br>
$$f(x,y,z) = 3y^2z \left( 3+\frac{7x+5}{1+y^2} \right)$$

2019年9月2日21:59:00

通过修改**defaule.html**中的js为[www.calvinneo.com-数理统计复习](http://www.calvinneo.com/2017/10/11/%E6%95%B0%E7%90%86%E7%BB%9F%E8%AE%A1%E5%A4%8D%E4%B9%A0/)
源码中的脚本，使得在github上可以成功渲染**mathjax**

```
<script type="text/x-mathjax-config">
      MathJax.Hub.Config({
        tex2jax: {
          inlineMath: [ ['$','$'], ["\\(","\\)"]  ],
          processEscapes: true,
          skipTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
        }
      });
    </script>

    <script type="text/x-mathjax-config">
      MathJax.Hub.Queue(function() {
        var all = MathJax.Hub.getAllJax(), i;
        for (i=0; i < all.length; i += 1) {
          all[i].SourceElement().parentNode.className += ' has-jax';
        }
      });
    </script>
    <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```