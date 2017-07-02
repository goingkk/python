#coding:utf-8
import time

i = [str(x) for x in range(10000)]
print("i[:10]: ",i[:10])
print('len(i): ',len(i),'\n','-'*20)



######################### map 
r1 = i
start = time.clock()

for x in range(1000):     #耗时 0.02秒
    r1 = map(int,r1)
r11 = list(r1)            #耗时 1秒

print("map time: ",time.clock()-start,'\n','-'*20)



######################### Generator
r2 = i
start = time.clock()

for x in range(1000):     #耗时 1.4秒
    r2 = [int(x) for x in r2]
    
print("Generator time: ",time.clock()-start,'\n','-'*20)  



######################### While
r3 = i 
start = time.clock()

for x in range(1000):     #耗时 5.3秒
    n = 0
    while n<len(r3):
        r3[n] = int(r3[n])
        n = n+1 

print("While time: ",time.clock()-start,'\n','-'*20)   
