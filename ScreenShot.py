import subprocess
class Screenshot():#截取手机屏幕并保存到电脑
    def __init__(self):
        #查看连接的手机
        connect=subprocess.Popen("adb devices",stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        stdout,stderr=connect.communicate()   #获取返回命令

 
    def screen(self,cmd):#在手机上截图
        screenExecute=subprocess.Popen(str(cmd),stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        stdout, stderr = screenExecute.communicate()
 
 
    def saveComputer(self,cmd):#将截图保存到电脑
        screenExecute = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = screenExecute.communicate()

 
    def shot(self):
        cmd1=r"adb shell /system/bin/screencap -p /sdcard/3.png"       #命令1：在手机上截图3.png为图片名
        cmd2=r"adb pull /sdcard/3.png temp/cur.png"                        #命令2：将图片保存到电脑 d:/3.png为要保存到电脑的路径
        screen=Screenshot()
        screen.screen(cmd1)
        screen.saveComputer(cmd2)