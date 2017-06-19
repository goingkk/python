#coding:utf-8

class Chain(object):

    def __init__(self, path='GET '):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self,path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
	

print( Chain().group('student').users('michael').repos )	

#print( Chain().group )    #这步只走 __getattr__()，注释 __call__()无报错。
#print( Chain().group() )  #这步先走 __getattr__()，再走 __call__()。看报错信息。


"""
链式调用：
	1. Chain().group，没有group，走 __getattr__()，得到 Chain('GET /group')，
	   即 Chain().group = Chain('GET /group')
	2. Chain().group('student')，即 Chain('GET /group')('student')，走 __call__()，得到 Chain('GET /group/student')，
	   即 Chain().group('student') = Chain('GET /group/student')
	3. 以此类推 .users('michael').repos 部分
"""
