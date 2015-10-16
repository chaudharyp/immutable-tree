from node import Node
from singleton import Singleton

# Tree class inherits from Singleton class for thread safety
class Tree(Singleton):
	# Used to make the tree immutable
	__slots__ = ["root"]

	def __init__(self):
		super(Tree, self).__setattr__("root", Node(0))

	# Used to make the tree immutable
	def __setattr__(self, name, value):
		msg = "'%s' has no attribute %s" % (self.__class__, name)
		raise AttributeError(msg)
	
	# Inserting a node into the tree
	def insertNode(self, root, node):
		# Inserting the 1st node into the tree
		if root.data == 0 or root is None:
			root.addData(node.data)
		else:
			# If node data is less than root data, insert in left subtree. Else, insert in right subtree
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

	# Inserting data into the tree. Wrapper around insertNode.
	def insertData(self, data):
		root = self.root
		node = Node(data)
		self.insertNode(root, node)

	# Inorder traversal of the tree.
	def inorderPrint(self, root):
	    if root is None:
	        return
	    self.inorderPrint(root.lchild)
	    print(root.data)
	    self.inorderPrint(root.rchild)

    # Check if a key is present in the tree
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

	# Delete a node from the tree
	def delete(self, root, key):
		parent = root
		while root is not None:
			# temp is used to keep a track of the parent node. Assigned to parent variable later.
			temp = root

			# If root data is greater than key, go to left subtree. If less than key, go to right subtree. Else, delete the node.
			if root.data > key:
				root = root.lchild
			elif root.data < key:
				root = root.rchild
			else:
				# Check if the node has any child or not. Depending on that replace the parent node's child.
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

				# If leaf node or one child node, replace the parent node's child immediately with replacementNode.
				if hasOneOrNoChild:
					if parent.lchild is not None and parent.lchild.data == root.data:
						parent.addLeftChild(replacementNode)
					else:
						parent.addRightChild(replacementNode)
					break
				else:
					# If not a leaf node or one child node, replace the node with inorder predecessor.
					largestInLeftSubtree = self.largest(root.lchild)
					root.addData(largestInLeftSubtree.data)
					# After replacing, delete the inorder predecessor.
					# We traverse the left subtree with the key to be deleted as inorder predecessor.
					root = root.lchild
					key = largestInLeftSubtree.data
			parent = temp

	# Finding the largest node in the tree
	def largest(self, root):
		if root.rchild is None:
			return root
		# Largest node will be the rightmost node in the tree.
		return self.largest(root.rchild)
