#!/usr/bin/python3

import threading
import time

def two_job():
    print('!thread %s is running...' %threading.current_thread().name)
    for i in range(5):
        print('My 2nd program:', i)
        time.sleep(0.5)

t = threading.Thread(target = two_job)

t.start()
print('thread %s is running...' %threading.current_thread().name)
for i in range(2):
    print('Main program', i)
    time.sleep(0.1)

t.join()
print('threading %s is running...' %threading.current_thread().name)
print('Done')
