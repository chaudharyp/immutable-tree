class Node:
	def __init__(self, val):
		self.__lchild = None
		self.__rchild = None
		self.__data = val

	@property
	def data(self):
	    return self.__data

	@property
	def lchild(self):
	    return self.__lchild

	@property
	def rchild(self):
	    return self.__rchild

	def addLeftChild(self, node):
		self.__lchild = node

	def addRightChild(self, node):
		self.__rchild = node

	def addData(self, data):
		self.__data = data