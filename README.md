# dacaihua_2048

2048版合成大菜花

## 使用方法

直接运行run文件夹下Play.exe

或者运行play.cmd

## 二次开发

### 相关文件

venv文件夹-调用的py库 用于封包

images文件夹-美工资源

GameCalculation.py-游戏规则

GameImages.py-图片调用

GameRun.py-主程序

### 封包方法

pyinstaller -F GameRun.py -p GameImages.py -p GameCalculation.py

pyinstaller -F -i xxx.ico GameRun.py -p GameImages.py -p GameCalculation.py 封包图标

## 写在最后

二次开发请署名[原项目](https://blog.csdn.net/qq_45011837/article/details/105891020)

哔哩哔哩直播间7194086

19998 hurry up!