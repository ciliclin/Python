#!/usr/bin/python3

import threading
import time

def job(num):
    print('Thread name:%s' %threading.current_thread().name)
    for i in range(1, 10):
        num += 1
        print('Thread', num)
        time.sleep(0.1)

x = 0
t = threading.Thread(target = job, args=(x, ))
t.start()
print('Thread name:%s' %threading.current_thread().name)

print(threading.active_count())
t.join()

print('Done')
