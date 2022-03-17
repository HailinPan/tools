#!/usr/bin/env python

from multiprocessing import Manager,Process,Lock,Pool
import time
import numpy as np

def work(d,a,lock):
    time.sleep(5)
    with lock:  # 不加锁而操作共享的数据,肯定会出现数据错乱
        d['count'] -= 1

def work2(a,i,lock):
    #stime.sleep(5)
    d = {'count' : {}}
    d['count']['t'] = i
    return(d)


if __name__ == '__main__':
    # lock=Manager().Lock()
    # pool = Pool(3)
    # d = {'count': 110}
    # dic=Manager().dict(d)
    # a = list(np.random.rand(20000,20000))
    # a = Manager().list(a)
    # for i in range(10):
    #     pool.apply_async(work, (dic,a,lock))
    # pool.close()
    # pool.join()
    # print(dic)
    # print(a)
    # print("finish")

    lock=Manager().Lock()
    pool = Pool(3)
    result = []
    a = list(np.random.rand(10,10))
    a = Manager().list(a)
    for i in range(10):
        result.append(pool.apply_async(work2, (a,i,lock)))
    pool.close()
    pool.join()
    print(a)
    for res in result:
        print(res.get())
    print("finish")
