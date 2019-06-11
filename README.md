# ArkNight-Auto
基于opencv+python图像识别的明日方舟自动刷图小助手（反复刷代理）

## Dependency

+ python3
  + opencv-python==3.4.2.16
  + opencv-contrib-python==3.4.2.16
  + numpy
  + subprocess
  + PIL
+ adb

## Basic Idea

+ 实时截取手机图像
+ 通过opencv图像匹配检测当前状态并获取对应图标位置
+ adb发送点击命令

## Usage

+ 手机连接到电脑，打开USB调试模式。

+ 启动明日方舟，进入到包含res文件夹下图片的任一界面
+ `python run.py`启动小助手

## Others

+ res文件夹下图片大小会影响到图像匹配结果。

+ 如果识别不出来图像，请在cur文件夹下截图结果cur.png中截取对应图标,替换掉res文件夹下对应图标。



