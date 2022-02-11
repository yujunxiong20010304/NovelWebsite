# <p align="center">使用vue+flask开发小说网站并部署在阿里云服务器<p>
  
# 环境
  * python
  * MYSQL
  * REDIS
  * Vue
# python 依赖库
  * flask
  * redis
  * pymysql
  * flask-cors
  * flask-session
  * opencv-python
  * pybase64
  * dlib
# 修改配置文件
  根据自己情况修改back_end/settings.py文件
  
  #### 适用环境
  * 前端：Vue 2.0
  * 后端：flask
# 部署阿里云服务器
  * 可参考：<a href="https://juejin.cn/post/6844904084680474637" style="font-size:12px;"> nginx部署 </a>
  ![部署](https://s3.bmp.ovh/imgs/2022/02/91b199305298dbaa.png "nginx配置")
  * 后端flask需要在阿里云服务器上启动/back_end/flasks.py文件
# 项目功能介绍
  整个项目前端采用Vue-cli脚手架搭建，后端由flask开放接口，实现前后端分离开发
# 项目功能：
  * 人脸识别登录
    ** 采用dlib调用训练集完成
