import autopress
import time
import easygui
import sys

pic_dirs = ['start_map.png','no_intellect.png','start_charac.png','running.png','level_up.png','finish.png']
start_map = 0
no_intellect = 1
start_charac = 2
running = 3
level_up = 4
finish = 5
next_state = 0

reverse = False
if(len(sys.argv) > 1 and sys.argv[1] == 'r'):
    print('reversed')
    reverse = True

while(True):
    flag = False
    # if(next_state == level_up):
    #     next_state += 1
    if(next_state == running or next_state == no_intellect):
        flag = autopress.find_pos(pic_dirs[next_state],False,reverse)
    else:
        flag = autopress.find_pos(pic_dirs[next_state],True,reverse)
    if(flag):
        print("\tfound")
        if(next_state == running):
            time.sleep(15)
            next_state -= 1
        elif(next_state == no_intellect):
            autopress.find_pos('cancel.png',True,reverse)
            easygui.msgbox("理智耗尽，小助手将退出", title="警告",ok_button="ok") 
            exit(0)
        time.sleep(1)
    next_state += 1
    if(next_state > 5):
        next_state = 0
