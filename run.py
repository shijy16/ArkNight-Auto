import autopress
import time

pic_dirs = ['start_map.png','start_charac.png','running.png','finish.png']
start_map = 0
start_charac = 1
finish = 3
running = 2

next_state = 0

while(True):
    flag = False
    if(next_state == running):
        flag = autopress.find_pos(pic_dirs[next_state],False)
    else:
        flag = autopress.find_pos(pic_dirs[next_state],True)
    if(flag):
        print("\tfound")
        time.sleep(5)
        if(next_state == running):
            time.sleep(10)
    next_state += 1
    if(next_state > 3):
        next_state = 0
