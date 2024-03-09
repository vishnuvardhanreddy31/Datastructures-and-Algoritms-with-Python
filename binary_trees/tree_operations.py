# tree_operations.py
from collections import deque
from binary_tree import BinaryTree


# Method to find the height of the tree
def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height, right_height) + 1


# Method to find the number of nodes in the tree
def count_of_nodes(root):
    if root is None:
        return 0
    left_nodes = count_of_nodes(root.left)
    right_nodes = count_of_nodes(root.right)
    return left_nodes + right_nodes + 1


# Method to find the sum of nodes in the tree
def sum_of_nodes(root):
    if root is None:
        return 0
    left_sum = sum_of_nodes(root.left)
    right_sum = sum_of_nodes(root.right)
    return left_sum + right_sum + root.data


# Method to find the diameter of the tree
def diameter(root):
    if root is None:
        return 0
    dia1 = height(root.left) + height(root.right) + 1
    dia2 = diameter(root.left)
    dia3 = diameter(root.right)
    return max(dia1, max(dia2, dia3))



# Method to find the diameter of the tree (approach 2)
class TreeInfo:
    def __init__(self, ht, diam):
        self.ht = ht
        self.diam = diam

def diameter1(root):
    if root is None:
        return TreeInfo(0, 0)
    left_ti = diameter1(root.left)
    right_ti = diameter1(root.right)
    my_height = max(left_ti.ht, right_ti.ht) + 1
    dia1 = left_ti.ht + right_ti.ht + 1
    dia2 = left_ti.diam
    dia3 = right_ti.diam
    my_diam = max(dia1, max(dia2, dia3))
    return TreeInfo(my_height, my_diam)
  
if __name__ == "__main__":
    nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
    tree = BinaryTree()
    root = tree.build_tree(nodes)

    print("Height of the tree is:", height(root))
    print("Number of nodes in the tree is:", count_of_nodes(root))
    print("Sum of nodes in the tree is:", sum_of_nodes(root))
    print("Diameter of the tree is:", diameter(root))
    print("Diameter (approach 2) of the tree is:", diameter1(root).diam)

