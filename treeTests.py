import unittest
from tree import Tree

class TestTree(unittest.TestCase):
  def setUp(self):
    # Creating the tree
    self.tree = Tree()
    self.tree.insertData(3)
    self.tree.insertData(1)
    self.tree.insertData(7)
    self.tree.insertData(5)

  def tearDown(self):
    self.tree = None

  def testInsertData(self):
    root = self.tree.root
    self.assertEqual(root.data, 3)
    self.assertEqual(root.lchild.data, 1)
    self.assertEqual(root.rchild.data, 7)
    self.assertEqual(root.rchild.lchild.data, 5)

  def testDelete(self):
    root = self.tree.root
    # Testing deletion of node with 2 children.
    self.tree.delete(root, 3)
    self.assertEqual(root.data, 1)
    # Testing deletion of node with 1 child.
    self.tree.delete(root, 7)
    self.assertEqual(root.rchild.data, 5)
    # Testing deletion of leaf node.
    self.tree.delete(root, 5)
    self.assertEqual(root.rchild, None)

  def testIsKeyPresent(self):
    root = self.tree.root
    isKeyPresent = self.tree.isKeyPresent(root, 3)
    self.assertTrue(isKeyPresent)
    isKeyPresent = self.tree.isKeyPresent(root, 9)
    self.assertFalse(isKeyPresent)

  def testLargest(self):
    root = self.tree.root
    largest = self.tree.largest(root)
    self.assertEqual(largest.data, 7)

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestTree)
  unittest.TextTestRunner(verbosity=2).run(suite)