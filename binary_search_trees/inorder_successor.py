def inorder_successor(root):
  current=root
  while current.left is not None:
    current=current.left
  return current