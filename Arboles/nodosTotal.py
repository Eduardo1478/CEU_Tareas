class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

def count_elements(root):
    if root is None:
        return 0
    else:
        return 1 + count_elements(root.left) + count_elements(root.right)


tree = None
tree = insert(tree, 5)
tree = insert(tree, 3)
tree = insert(tree, 7)
tree = insert(tree, 2)
tree = insert(tree, 4)
tree = insert(tree, 6)
tree = insert(tree, 8)

num_elements = count_elements(tree)
print(f"Number of elements in the tree: {num_elements}")