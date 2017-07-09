#coding:utf-8

#例5 利用yield from语句向生成器（协程）传送数据
#传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
#如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，换回生产者继续生产，效率极高：

import time

def  consumer_work():
    # 读取send传进的数据，并模拟进行处理数据
    print("consumer_work...")
    w=''
    while True:
        w = yield w       # w接收send传进的数据,同时也是返回的数据
        print('[CONSUMER] Consuming ----', w)
        w *= 100          # 将返回的数据乘以100
        time.sleep(2)     # 加入停顿时间，看输出节奏

def consumer(coro):
    print("consumer 1 ...")
    yield from coro             # 将数据传递到协程(生成器)对象中
    print("consumer 2 ...")     # 不会执行到这句

####### 类似于以下逻辑(实质怎样不知，所以只能说类似)
"""
def consumer(coro,):
    print("consumer 1 ...")
    w = ''
    coro.send(None)
    while True:
        i = yield w
        w = coro.send(i)  
    print("consumer 2 ...")    
"""
    
def produce(c):
    c.send(None)          # "prime" the coroutine
    for i in range(5):
        print('[Produce] Producing -----', i)
        w = c.send(i)     # 发送完成后进入协程中执行
        print('[Produce] receive -------', w)
    c.close()


    
cw = consumer_work()
print("begin 1....")
c = consumer(cw)
print("begin 2....")
produce(c)

"""
"""