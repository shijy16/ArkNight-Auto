# ArkNight-Auto
基于opencv+python图像识别的明日方舟自动刷图小助手（反复刷代理）

## Dependency

+ python3
  + opencv-python==3.4.2.16
  + opencv-contrib-python==3.4.2.16
  + numpy
  + subprocess
  + PIL
  + easygui
+ adb

## Basic Idea

+ 实时截取手机图像
+ 通过opencv图像匹配检测当前状态（目前分为：`地图开始,选人开始,战斗中，战斗结束，理智耗尽`四个状态）并获取对应图标位置。
  + 若当前处于`地图开始、选人开始、战斗结束`状态中任一个，点击开始或者结束。
  + 若当前处于`战斗中`状态，小助手睡眠10s。
  + 若当前`理智耗尽`，弹窗警告并退出小助手。

## Usage

+ 手机连接到电脑，打开USB调试模式。

+ 启动明日方舟，进入到包含res文件夹下图片的任一界面
+ `python run.py`启动小助手

## Problem Solution

+ res文件夹下图片大小会影响到图像匹配结果。
+ 如果识别不出来图像，请在cur文件夹下截图结果cur.png中截取对应图标,替换掉res文件夹下对应图标。**注意在截图时不要进行任何缩放**。
+ 如果识别了出来但是点击位置不对，请翻转手机再次尝试。

## Development

+ 暑假可能会添加一些小功能，现在这个东西也很简单（没花什么时间...）,但基本够用了。

+ 因为在使用时还没遇到代理失误的情况，所以没有发生这种情况的图片，没有处理这种情况。

+ 图像识别部分直接搬运了 <https://github.com/Kur1su0/AutoArknights> 中的查找子图片位置函数。
+ 欢迎在本项目上开发更多功能。



>  本项目仅供学习交流
