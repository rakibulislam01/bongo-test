# Python program to find LCA of n1 and n2 using one
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def find_lca(root, n1, n2):
    if root is None:
        return None
    if root.key == n1 or root.key == n2:
        return root

    # keys in left and right subtrees
    left_lca = find_lca(root.left, n1, n2)
    right_lca = find_lca(root.right, n1, n2)

    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca


# Create a binary tree given
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
print("LCA(4,6) = ", find_lca(root, 4, 6).key)
print("LCA(3,4) = ", find_lca(root, 3, 4).key)
print("LCA(2,4) = ", find_lca(root, 2, 4).key)
print("LCA(8,9) = ", find_lca(root, 8, 9).key)
print("LCA(6,7) = ", find_lca(root, 6, 7).key)
