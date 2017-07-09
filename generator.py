
# 注意 变成generator的函数，在首次调用的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

def consumer():
    r = 'rrrrrrrr'
    print('lalalalalaal') # 只有第一次会执行(启动生成器), 之后再调用生成器就会从yield处执行
    while True:
        n = yield r       # 再次执行时从这里的yield继续,将produce传入的 m 赋给 n , 并把 r 返回
                          # 所以yield不但可以返回一个值，它还可以接收调用者发出的参数
        if not n:
            return
        print('[Consumer] Consuming %s...' % n)
        r = '200 OK'      # 因为yield r 所以这个r会在下一次循环被返回给produce函数 
        

def producer(c):
    #r2 = c.send(None)     #首次启动生成器，只能传None，consumer会把 r 返回
    #print(r2)
    next(c)                # 这句作用同 c.send(None)
    print('babababab\n')
    m = 1
    while m < 6:
        print('-'*40,m)
        print('[Producer] Producing %s...' % m)
        r2 = c.send(m*10) # 获取生成器consumer中由yield语句返回的下一个值
        print('[Producer] Consumer return: %s' % r2)
        m = m + 1
    c.close()             # 停止生成器，整个过程结束。

c = consumer()            # 并不会启动生成器, 只是将c变为一个生成器，所以下一句print先执行
print('AaAaAaAaAa')       
producer(c)

