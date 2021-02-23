#!/usr/bin/python3

import threading
import time

def job1():
    for i in range(15):
        print('Job1 program:', i)
        time.sleep(0.5)
    print('job1 is done')

def job2(num):
    for i in range(15):
        print('Job2 program:', num+i)
        time.sleep(1)
    print('job2 is done')

t1 = threading.Thread(target = job1)
t2 = threading.Thread(target = job2, args = (10,))

#t1.setDaemon(True)
#t2.setDaemon(True)
t1.start()
t2.start()
print('thread %s is running...' %threading.current_thread().name)
for i in range(2):
    print('Main program', i)
    time.sleep(0.1)
#t2.join()
#t1.join()
print('threading %s is running...' %threading.current_thread().name)
print('Main thread is done! Child thread: t1 & t2 are still running')
