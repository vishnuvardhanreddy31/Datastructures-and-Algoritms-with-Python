from binary_tree import BinaryTree
from lowest_common_ancestor import lowest_common_ancestor


# Method to get the distance of a node from root
def lca_dist(root, n):
  if root is None:
    return -1
  if root.data==n:
    return 0
  leftDist=lca_dist(root.left,n)
  rightDist=lca_dist(root.right,n)
  if(leftDist==-1 and rightDist==-1):
    return -1
  elif leftDist==-1:
    return rightDist+1
  else:
    return leftDist+1
 
# Method to get the minimum distance between two nodes   
def min_dist_bet_nodes(root, p, q):
  lca_node=lowest_common_ancestor(root,p,q)
  dist1=lca_dist(lca_node,p)
  dist2=lca_dist(lca_node,q)
  return dist1+dist2
  
  
if __name__=='__main__':
  
  
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
  p=4
  q=3
  distance=min_dist_bet_nodes(root, p, q)
  print(f"minimum distance between {p} and {q} is : ",distance)
 