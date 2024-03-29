def search(root, val):
    if root == None:
        return False
    if root.data == val:
        return True
    if root.data > val:
        return search(root.left, val)
    return search(root.right, val)