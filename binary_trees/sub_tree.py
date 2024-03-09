from binary_tree import BinaryTree
def is_subtree(root,subroot):
  if root==None:
    return False
  if root.data == subroot.data:
    if is_identical(root,subroot):
      return True
  left=is_subtree(root.left,subroot)
  right=is_subtree(root.right,subroot)
  return left or right

def is_identical(root,subroot):
  if root==None and subroot==None:
    return True
  if root==None or subroot==None:
    return False
  if root.data!=subroot.data:
    return False
  if not is_identical(root.left,subroot.left):
    return False
  if not is_identical(root.right,subroot.right):
    return False
  return True 

if __name__ == "__main__":
  
  # Tree Structure
    #      1
    #    /   \
    #   2     3
    #  / \   /  \
    # 4   5 6    7
    #       
    
  nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, 6, -1, -1, 7,-1,-1]
  tree = BinaryTree()
  root = tree.build_tree(nodes)
  sub_tree1=BinaryTree()
  subroot_nodes1 = [2, 4, -1, -1, 5, -1, -1]
  
#  Subtree Structure 
#       2
#      / \
#     4   5

  subroot1 = sub_tree1.build_tree(subroot_nodes1)
  print(is_subtree(root,subroot1))
  sub_tree2=BinaryTree()
  subroot_nodes2 = [3, 6,-1,-1, 7,-1,-1]
  
  
# Subtree Structure 
#        3
#      /  \
#     6    7


  subroot2 = sub_tree2.build_tree(subroot_nodes2)
  print(is_subtree(root,subroot2))
  