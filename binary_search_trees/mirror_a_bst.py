from tree_node import Node
def create_mirror_bst(root):
    """ Function to create a mirror of a binary search tree"""
    if root is None:
        return None
    left_mirror = create_mirror_bst(root.left)
    right_mirror = create_mirror_bst(root.right)
    root.left = right_mirror
    root.right = left_mirror
    return root