from node import Node
from singleton import Singleton

class Tree(Singleton):
	__slots__ = ["root"]

	def __init__(self):
		super(Tree, self).__setattr__("root", Node(0))

	def __setattr__(self, name, value):
		msg = "'%s' has no attribute %s" % (self.__class__, name)
		raise AttributeError(msg)
	
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
		root = self.root
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
			elif root.data < key:
				root = root.rchild
			else:
				keyFound = True
				break;
		return keyFound


	def delete(self, root, key):
		parent = root
		while root is not None:
			temp = root
			if root.data > key:
				root = root.lchild
			elif root.data < key:
				root = root.rchild
			else:
				hasOneOrNoChild = False
				replacementNode = None
				if not root.hasChild():
					hasOneOrNoChild = True
					replacementNode = None
				elif root.lchild is None:
					hasOneOrNoChild = True
					replacementNode = root.rchild
				elif root.rchild is None:
					hasOneOrNoChild = True
					replacementNode = root.lchild

				if hasOneOrNoChild:
					if parent.lchild is not None and parent.lchild.data == root.data:
						parent.addLeftChild(replacementNode)
					else:
						parent.addRightChild(replacementNode)
					break
				else:
					largestInLeftSubtree = self.largest(root.lchild)
					root.addData(largestInLeftSubtree.data)
					root = root.lchild
					key = largestInLeftSubtree.data
			parent = temp

	def largest(self, root):
		if root.rchild is None:
			return root
		return self.largest(root.rchild)
