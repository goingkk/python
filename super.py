#coding:utf-8

class A():
	def __init__(self):
		print("in A")
		print("out A")
	

	
#######
class B(A):
	def __init__(self):
		print("in B")
		super(B,self).__init__()
		print("out B")
	
class C(A):
	def __init__(self):
		print("in C")
		super(C,self).__init__()
		print("out C")
	
		
#######
class D(C,B):
	def __init__(self):
		print("in D")
		print("-------------------")
		super(B,self).__init__()      #     A A
		print("-------------------")
		super(C,self).__init__()      #   B A A B
		print("-------------------")
		super(D,self).__init__()      # C B A A B C
		print("-------------------")
		print("out D")
	
		
#######
D()
print(D.__mro__)

"""
	D 的 mro 执行顺序是 D > C > B > A > object，
	super(X,self) 是指在当前类的mro顺序里面，X的下一个，并不是指父类，
	所以，super(B,self).__init__() == A.__init__()
		  super(C,self).__init__() == B.__init__() > A.__init__()
		  super(D,self).__init__() == C.__init__() > B.__init__() > A.__init__()
		  
	super(D,self).__init__() 的执行实际是：
		print("in C")
			print("in B")
				print("in A")
				print("out A")
			print("out B")
		print("out C")
	
"""
	
