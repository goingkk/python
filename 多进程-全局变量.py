#coding:utf-8

from multiprocessing import Pool
import os, time

n = 0  #看看多进程对全局变量的影响
n += 1
  
def task(name):
    global n     
    print('Run task {} by Child-process {}  , n={}'.format(name, os.getpid(),n))
    n = n+1
    
    

if __name__=='__main__':
    print('Parent-process {}.'.format(os.getpid()))
    p = Pool(4)    #修改进程数，查看并发对 n 的影响
    for i in range(5):
        p.apply_async(time.sleep,args=(0.03,))
        p.apply_async(task, args=(i,))
    print('Waiting for all subprocesses done...  n={}'.format(n))
    p.close()
    p.join()
    print('All subprocesses done.  n={}'.format(n))
    print('inside n={}'.format(n))
    
print('outside n={}'.format(n))

    
"""
    写多进程时，注意像 n 这种全局存在，不要以为每个进程共用一个 n 。
    修改 sleep大小 或 进程池数量 可见，每个进程都私有一份 n ，只操作自己的 n（pid和n的对应）。
    即，多进程其实和启动多个脚本一样，代码上的全局变量，都是各进程的私有变量
"""

