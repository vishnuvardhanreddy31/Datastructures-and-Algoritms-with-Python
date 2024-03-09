from binary_tree import BinaryTree
from tree_traversals import TreeTraversals
def transform_to_sum_tree(root):
    if root is None:
        return 0
    left_child=transform_to_sum_tree(root.left)
    right_child=transform_to_sum_tree(root.right)
    data=root.data
    new_left=root.left.data if root.left else 0
    new_right=root.right.data if root.right else 0
    root.data=left_child+right_child+new_left+new_right
    return data
  
if __name__ == "__main__":
    nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, 6, -1, -1, 7, -1, -1]
    # Tree Structure
    #      1
    #    /   \
    #   2     3
    #  / \   /  \
    # 4   5 6    7    
    
    tree = BinaryTree()
    root = tree.build_tree(nodes)
    print("Before transformation:")
    t=TreeTraversals()
    t.levelorder(root)
    transform_to_sum_tree(root)
    
    #     27
    #    /  \
    #   9    13
    #  / \  / \
    # 0  0 0   0

    print("\nAfter transformation:")
    t.levelorder(root)