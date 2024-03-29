from tree_node import Node
def insert(root,val):
    if root is None:
        return Node(val)
    if val < root.data:
        root.left = insert(root.left,val)
    else:
        root.right = insert(root.right,val)
    return root