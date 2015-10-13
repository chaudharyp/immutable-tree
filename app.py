from tree import Tree

tree = Tree()
tree.insertData(3)
tree.insertData(7)
tree.insertData(1)
tree.insertData(5)

tree.inorderPrint(tree.root)

isKeyPresent = tree.isKeyPresent(tree.root, 3)
print(isKeyPresent)