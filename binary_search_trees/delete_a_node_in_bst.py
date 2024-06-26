from inorder_successor import inorder_successor
# The above line imports the inorder_successor function from the inorder_successor.py file
def delete_node(root,val):
  """ This function deletes a node with value val from the BST"""
  if root.data<val:
    root.right=delete_node(root.right,val)
  elif root.data>val:
    root.left=delete_node(root.left,val)
  else:
    # case 1: no child leaf node
    if root.left is None and root.right is None:
      return None
    # case 2: one child
    if root.left is None:
      return root.right
    elif root.right is None:
      return root.left
    # case 3: two children
    # find the inorder successor
    IS=inorder_successor(root.right)
    root.data=IS.data
    root.right=delete_node(root.right,IS.data)
  return root
    