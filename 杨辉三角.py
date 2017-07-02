def test():
    L=[1]
    while True:
        yield L
        L = [1] + [ L[x-1] + L[x] for x in range(1,len(L)) ] + [1]
        
n = 0
for t in test():
    print(t)
    n = n + 1
    if n == 10:
        break