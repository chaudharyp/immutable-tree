from node import Node

class Tree:
	def __init__(self):
		self.__root = Node(0)

	@property
	def root(self):
	    return self.__root
	
	def insertNode(self, root, node):
		if root.data == 0 or root is None:
			root.addData(node.data)
		else:
			if root.data > node.data:
				if root.lchild is None:
					root.addLeftChild(node)
				else:
					self.insertNode(root.lchild, node)
			else:
				if root.rchild is None:
					root.addRightChild(node)
				else:
					self.insertNode(root.rchild, node)

	def insertData(self, data):
		root = self.__root
		node = Node(data)
		self.insertNode(root, node)

	def inorderPrint(self, root):
	    if root is None:
	        return
	    self.inorderPrint(root.lchild)
	    print(root.data)
	    self.inorderPrint(root.rchild)

	def isKeyPresent(self, root, key):
		if root is None:
			return False
		if root.data == key:
			return True
		if root.data > key:
			return self.isKeyPresent(root.lchild, key)
		else:
			return self.isKeyPresent(root.rchild, key)