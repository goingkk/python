#coding:utf-8

from multiprocessing import Pool
import math,time,os

def IsPrime(n):
    """返回n是否是素数"""
    if not isinstance(n, int):
        raise TypeError("argument passed to is_prime is not of 'int' type")
    if n < 2:
        return False
    if n == 2:
        return True
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= max:
        if n % i == 0:
            return False
        i += 1
    return True

def SumPrimes(n):
    for i in xrange(15):
        sum([x for x in xrange(2,n) if IsPrime(x)])
    """计算从2-n之间的所有素数之和"""
    return sum([x for x in xrange(2,n) if IsPrime(x)])

#inputs = (100000, 100100, 100200, 100300, 100400, 100500, 100600, 100700, 100800, 100900)


#################### Single #############################
#start_time = time.clock()
#for input in inputs:
#    print SumPrimes(input)
#print 'Single-times:', time.clock() - start_time, 's','\n'


#################### Parallel #############################
if __name__ == '__main__':  #在windows下需要这判断，linux不用。这句作用是判断是不是直接运行本脚本，而非当成模块被调用
    print u"输入数字，用逗号分隔和结尾："
    inputs = tuple(input())
    print inputs
    start_time = time.clock()
    pool = Pool()          #值视CPU而定，>CPU进程数 也不会有多少提升，不写则默认 =CPU进程数
    print pool.map(SumPrimes,inputs)
    pool.close()
    pool.join()
    print 'Parallel-times:', time.clock() - start_time, 's','\n'
    
print "\n**************** pid: ",os.getpid()  #这是if外的代码，每个子进程都会执行一次，最后父进程再执行一次

""" 注意点：
            从pool = Pool()开始产生多个进程，到pool.close()关闭，再pool.join()联合各进程结果，
            在if下的代码，是多进程并发处理，
            在if外的代码，每个进程都会去执行一遍，即 if外的运算量*进程数，
            也就是说，如果if外有代码，这些代码就会被n个进程执行了共n次。
            为提高可读性，可把if下代码放在一个函数里，然后if下调用此函数。
"""



