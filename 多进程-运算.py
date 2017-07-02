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
    start = time.clock()
    for i in range(15):  #增加运算量
        sum([x for x in range(2,n) if IsPrime(x)])
    """计算从2-n之间的所有素数之和"""
    l = [os.getpid(), sum([x for x in range(2,n) if IsPrime(x)]), time.clock()-start]
    print('Child process {}.  SumPrimes({})={}   time:{:.3f}'.format( l[0], n, l[1], l[2] ))
    


#################### Parallel #############################
if __name__=='__main__':
    print(u"输入数字：")
    inputs = tuple(input().split(','))
    print(inputs,'\n')
    print('Parent-process  {} . \n'.format(os.getpid()))
    p = Pool(4)
    for i in inputs:
        try:
            p.apply_async(SumPrimes, args=(int(i),))
        except:
            print("Err: Can't change {} to int \n".format(i))
    p.close()
    p.join()
    print('\nAll Child-processes done.')
    
print('*'*40,'process {}'.format(os.getpid()))


""" 注意点：
            Pool是进程池，进程数默认等于核心数。
			从p = Pool()开始产生多个进程，到p.close()关闭，p.join()是让父进程等待子进程出结果再进行.
            当用 apply_async() 执行一个函数时，会启动对应的进程数，但不一定均分任务给每个进程，
            可能有的进程没分配到任务，而有的进程执行了大部分任务甚至全部任务。
            
			在 if __name__=='__main__': 内的代码，是多进程并发处理，任务分配依运算量多少而定，
			在 if __name__=='__main__': 外的代码，每个进程都会去执行一遍，即 if外的运算量*进程数，
            也就是说，如果if外有代码，这些代码就会被n个进程执行了共 n+1 次，1 是指父进程。
            为提高可读性，可把if下代码放在一个函数里，然后if下调用此函数。
            
            例： 当SumPrimes()里的for被注释时，如果输入的值很小，例如(98,65,21)，
                 一个进程就完成了，另外的几个进程没做SumPrimes()的运算。
            从输出结果可看出，一个子进程执行完n次SumPrimes，但最后一句的print每个进程都执行了一遍，
            表明任务并非一定均分，但是进程一定开启。

"""



