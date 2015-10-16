import unittest
from tree import Tree

class TestTree(unittest.TestCase):
  def setUp(self):
    self.tree = Tree()

  def tearDown(self):
    self.tree = None

  def testInsertData(self):
    root = self.tree.root
    self.tree.insertData(3)
    self.assertEqual(root.data, 3)
    self.tree.insertData(1)
    self.assertEqual(root.lchild.data, 1)
    self.tree.insertData(7)
    self.assertEqual(root.rchild.data, 7)
    self.tree.insertData(5)
    self.assertEqual(root.rchild.lchild.data, 5)

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestTree)
  unittest.TextTestRunner(verbosity=2).run(suite)