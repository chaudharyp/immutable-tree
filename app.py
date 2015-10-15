from tree import Tree

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

#tree.newProp = "testing immutability"	-- gives error because the object is now immutable

tree.inorderPrint(tree.root)

isKeyPresent = tree.isKeyPresent(tree.root, 3)
print(isKeyPresent)

tree.delete(tree.root, 50)
tree.delete(tree.root, 36)
tree.delete(tree.root, 40)
tree.inorderPrint(tree.root)