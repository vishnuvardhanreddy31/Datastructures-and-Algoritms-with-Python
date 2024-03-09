from collections import deque
from binary_tree import BinaryTree



# Tree Structure
    #      1
    #    /   \
    #   2     3
    #  / \   /  \
    # 4   5 6    7
    #       
    
    
# class to store the node and its horizontal distance from the root
class Info:
  def __init__(self,node,hd):
    self.node = node
    self.hd = hd
    

# Method to print the top view of the tree
def top_view(root):
  queue=deque()
  hash_map={}
  mini,maxi=0,0
  queue.append(Info(root,0))
  queue.append(None)
  while queue:
    curr=queue.popleft()
    if curr==None:
      if not queue:
        break
      else:
        queue.append(None)
    else:
      if curr.hd not in hash_map:
        hash_map[curr.hd]=curr.node
      if curr.node.left:
        queue.append(Info(curr.node.left,curr.hd-1))
        mini=min(mini,curr.hd-1)
      if curr.node.right:
        queue.append(Info(curr.node.right,curr.hd+1))
        maxi=max(maxi,curr.hd+1)
  for i in range(mini,maxi+1):
    print(hash_map[i].data,end=" ")
    

# Main function  
if __name__ == "__main__":
  nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, 6, -1, -1, 7,-1,-1]
  
  # Tree Structure
    #      1
    #    /   \
    #   2     3
    #  / \   /  \
    # 4   5 6    7
    #       
    
    
  tree = BinaryTree()
  root = tree.build_tree(nodes)
  top_view(root)
    
  
  
    
    