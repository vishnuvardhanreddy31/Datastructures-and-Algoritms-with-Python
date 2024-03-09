from binary_tree import BinaryTree


# Method to find the kth ancestor of a node
def kth_ancestor(root, n, k):
  if root is None:
    return -1
  if root.data==n:
    return 0
  leftDist=kth_ancestor(root.left,n,k)
  rightDist=kth_ancestor(root.right,n,k)
  if(leftDist==-1 and rightDist==-1):
    return -1
  maxi=max(leftDist,rightDist)
  if maxi+1==k:
    print(root.data,end=" ")
  return maxi+1


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
  n=5
  k=2
  print(f"{k}th ancestor of {n} is : ",end=" ")
  kth_ancestor(root, n, k)
  print()
  n=6
  k=1
  print(f"{k}th ancestor of {n} is : ",end=" ")
  kth_ancestor(root, n, k)
 