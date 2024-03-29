def print_root_to_leaf_paths(root, path):
    if root is None:
        return
    path.append(root.data)
    if root.left is None and root.right is None:
        print(path)
    else:
        print_root_to_leaf_paths(root.left, path)
        print_root_to_leaf_paths(root.right, path)
    path.pop()