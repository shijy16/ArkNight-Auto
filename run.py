import autopress
import time
import easygui

pic_dirs = ['start_map.png','no_intellect.png','start_charac.png','running.png','finish.png']
start_map = 0
no_intellect = 1
start_charac = 2
finish = 4
running = 3

next_state = 0

while(True):
    flag = False
    if(next_state == running or next_state == no_intellect):
        flag = autopress.find_pos(pic_dirs[next_state],False)
    else:
        flag = autopress.find_pos(pic_dirs[next_state],True)
    if(flag):
        print("\tfound")
        if(next_state == running):
            time.sleep(10)
        if(next_state == no_intellect):
            autopress.find_pos('cancel.png',True)
            easygui.msgbox("理智耗尽，小助手将退出", title="警告",ok_button="ok") 
            exit(0)
        time.sleep(5)
    next_state += 1
    if(next_state > 4):
        next_state = 0
