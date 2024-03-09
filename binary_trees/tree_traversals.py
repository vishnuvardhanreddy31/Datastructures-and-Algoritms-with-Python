from collections import deque
from binary_tree import BinaryTree  # Assuming you have the BinaryTree class defined somewhere

class TreeTraversals:
    def __init__(self):
        pass

    # Method to print the tree in preorder traversal
    def preorder(self, root):
        if root is None:
            print(-1, end=" ")
            return
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    # Method to print the tree in inorder traversal
    def inorder(self, root):
        if root is None:
            print(-1, end=" ")
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)

    # Method to print the tree in postorder traversal
    def postorder(self, root):
        if root is None:
            print(-1, end=" ")
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")

    # Method to print the tree in levelorder traversal
    def levelorder(self, root):
        if root is None:
            return
        q = deque()
        q.append(root)
        q.append(None)
        while q:
            curr = q.popleft()
            if curr is None:
                print()
                if not q:
                    break
                else:
                    q.append(None)
            else:
                print(curr.data, end=" ")
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

if __name__ == "__main__":
    nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, 6, -1, -1, 7, -1, -1]

    # Assuming you have the BinaryTree class defined somewhere
    tree = BinaryTree()
    root = tree.build_tree(nodes)

    traversals = TreeTraversals()

    print("Preorder Traversal:")
    traversals.preorder(root)
    print("\nInorder Traversal:")
    traversals.inorder(root)
    print("\nPostorder Traversal:")
    traversals.postorder(root)
    print("\nLevelorder Traversal:")
    traversals.levelorder(root)
