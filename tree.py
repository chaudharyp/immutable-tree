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
		keyFound = False
		while root is not None:
			if root.data > key:
				root = root.lchild
			else if root.data < key:
				root = root.rchild
			else:
				keyFound = True
				break;
		return keyFound


	def delete(self, root, node):
		while root is not None:
			if root.data > key:
				root = root.lchild
			else if root.data < key:
				root = root.rchild
			else:
				if root.lchild is None:
					root.addData(root.rchild.data)
					root.rchild = None
				else if root.rchild is None:
					root.addData(root.lchild.data)
					root.lchild = None
				else:
					largestInLeftSubtree = largest(root.lchild)
					

	def largest(root):
		if root.rchild is None:
			return root
		largest(root.rchild)
