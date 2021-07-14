class Tree:
  
  class Node:

    def __init__(self, data, left=None, right=None):
      self.left = left
      self.right = right
      self.data = data
  
  def __init__(self):
    self.root = None
 
  def insert(self, data):
    """
    Insert
    """
    if self.root is None:
        self.root = Tree.Node(data)
    elif data in tree:
      return
    else:
        self._insert(data, self.root)

  def _insert(self, data, node):
    """
    Insert recursion
    """
    if data < node.data:
      if node.left is None:
        node.left = Tree.Node(data)
      else:
        self._insert(data, node.left)
    else:
      if node.right is None:
        node.right = Tree.Node(data)
      else:
        self._insert(data, node.right)
  

  def __iter__(self):
    """
    Perform a forward traversal
    """
    yield from self._traverse_forward(self.root)

  def _traverse_forward(self, node):
    if node is not None:
      yield from self._traverse_forward(node.left)
      yield node.data
      yield from self._traverse_forward(node.right)


  def __reversed__(self):
    """
    Perform a reversed forward traversal (reversed in-order traversal)

    """

  def _traverse_backward(self, node):
    """
    Does a backwards traversal (reverse in-order traversal).  
    """
  

tree = Tree()
tree.insert(5)
tree.insert(3)
tree.insert(7)

print("Forward (Left -> Right)")
for x in tree:
    print(x)

"""
This is the first step in the problem. 
Implement the reverse/traverse-backward functions.
"""
print("Forward (Right -> Left)")
for x in reversed(tree):
    print(x)

"""
After the traverse backward is implemented add this set to the existing tree.
After the values are inserted print the countdown.
"""
nlist = (4, 6, 2, 8, 1, 9)

# Insert the values of the list into the tree

# Print the Countdown
print("\nCountdown to Take-Off")