def print_in_range(root,k1,k2):
  if root is None:
    return
  if root.data >= k1 and root.data <= k2:
    print_in_range(root.left,k1,k2)
    print(root.data)
    print_in_range(root.right,k1,k2)
  elif root.data < k1:
    print_in_range(root.left,k1,k2)
  else:
    print_in_range(root.right,k1,k2)