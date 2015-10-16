from tree import Tree

# Creating a tree
tree = Tree()
tree.insertData(50)
tree.insertData(40)
tree.insertData(30)
tree.insertData(45)
tree.insertData(48)
tree.insertData(46)
tree.insertData(49)
tree.insertData(55)
tree.insertData(52)
tree.insertData(51)
tree.insertData(29)
tree.insertData(35)
tree.insertData(32)
tree.insertData(36)

# To test immutability. 
# The code below throws an error becuase the object is now immutable
#tree.newProp = "testing immutability"

# Inorder traversal of a tree
print("Inorder traversal:")
tree.inorderPrint(tree.root)

# Check if a particular key is present in a tree or not
key = 3
isKeyPresent = tree.isKeyPresent(tree.root, key)
print("Is Key Present: ", isKeyPresent)

# Deleting a few nodes from the tree
tree.delete(tree.root, 50)
tree.delete(tree.root, 36)
tree.delete(tree.root, 40)

# Inorder traversal after deleting the nodes
print("Inorder traversal:")
tree.inorderPrint(tree.root)