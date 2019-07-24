#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Pool
import os, time, random

"""
https://www.liaoxuefeng.com/wiki/1016959663602400/1017628290184064
https://www.cnblogs.com/kaituorensheng/p/4465768.html
"""
def long_time_task(name):

    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

    return 're'+str(name)

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    result = []

    for i in range(5):
        result.append(p.apply_async(long_time_task, args=(i,)))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done. result:',result)
    for res in result:
        print (":::", res.get())