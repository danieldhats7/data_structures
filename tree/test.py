from BST import *

tree = BST(4)
tree.root.left = Node(2)
tree.root.right = Node(7)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)


def recursive(node, val):
    if node.data == val:
        return node
    elif node.left is not None and val < node.data:
        recursive(node.left, val)
    elif node.right is not None and val > node.data:
        recursive(node.right, val)
    else:
        return

r = recursive(tree.root, 2)
