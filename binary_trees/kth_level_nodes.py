from binary_tree import BinaryTree



# Tree Structure
    #      1
    #    /   \
    #   2     3
    #  / \   /  \
    # 4   5 6    7
    #       
    

# Method to print the nodes at kth level
def kth_level_nodes(root, level,k):
  if root==None:
    return
  if level==k:
    print(root.data,end=" ")
    return
  kth_level_nodes(root.left,level+1,k)
  kth_level_nodes(root.right,level+1,k)
  
# Main METHOD  
if __name__ == "__main__":
  nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, 6, -1, -1, 7,-1,-1]
  tree = BinaryTree()
  root = tree.build_tree(nodes)
  kth_level_nodes(root,0 ,1)
  
  
    