def is_valid_bst(root,min,max):
    if root is None:
        return True
    if min is not None and root.data <= min.data:
        return False
    elif max is not None and root.data >= max.data:
        return False
    return is_valid_bst(root.left,min,root) and is_valid_bst(root.right,root,max)