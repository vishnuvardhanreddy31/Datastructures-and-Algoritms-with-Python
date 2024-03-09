# binary_tree.py
from tree_node import Node

class BinaryTree:
    def __init__(self):
        self.idx = -1

    def build_tree(self, nodes):
        self.idx += 1
        if nodes[self.idx] == -1:
            return None
        new_node = Node(nodes[self.idx])
        new_node.left = self.build_tree(nodes)
        new_node.right = self.build_tree(nodes)
        return new_node
