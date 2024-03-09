from binary_tree import BinaryTree


# Tree Structure
    #      1
    #    /   \
    #   2     3
    #  / \   /  \
    # 4   5 6    7
    #       
    


# Method to get the path from root to a node
def getpath(root,node,path):
  if root==None:
    return False
  path.append(root)
  if root.data==node:
    return True
  if (root.left and getpath(root.left,node,path)) or (root.right and getpath(root.right,node,path)):
    return True
  path.pop()
  return False

# Method to get the path from root to a node
def lowest_common_ancestor(root, p, q):
  path1=[]
  path2=[]
  getpath(root,p,path1)
  getpath(root,q,path2)
  idx=0
  for i in range(min(len(path1),len(path2))):
    
    if path1[i]!=path2[i]:
      break
    idx+=1
  lca=path1[idx-1]
  return lca

# lowest common ancestor using recursion(approach 2)
def lca(root, p, q):
  if root==None:
    return None
  if root.data==p or root.data==q:
    return root
  left=lca(root.left,p,q)
  right=lca(root.right,p,q)
  if left and right:
    return root
  if left:
    return left
  else:
    return right
  


if __name__ == "__main__":
  nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, 6, -1, -1, 7,-1,-1]
  tree = BinaryTree()
  root = tree.build_tree(nodes)
  p=4
  q=5
  print(f'lowest common ancestor of {p},{q} is : ',lowest_common_ancestor(root,p,q).data)
  p=4
  q=6
  print(f'lowest common ancestor of {p},{q} is : ',lca(root,p,q).data)
 
 
    