# main_script.py
from binary_tree import BinaryTree
from tree_operations import preorder, levelorder, height, count_of_nodes, sum_of_nodes, diameter, diameter1

if __name__ == "__main__":
    nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
    tree = BinaryTree()
    root = tree.build_tree(nodes)

    print("Preorder Traversal:")
    preorder(root)

    print("\nLevelorder Traversal:")
    levelorder(root)

    print("\nHeight of the tree is:", height(root))
    print("Number of nodes in the tree is:", count_of_nodes(root))
    print("Sum of nodes in the tree is:", sum_of_nodes(root))
    print("Diameter of the tree is:", diameter(root))
    print("Diameter (approach 2) of the tree is:", diameter1(root).diam)
