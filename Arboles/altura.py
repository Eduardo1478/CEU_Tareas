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

def find_height(root):
    if root is None:
        return 0
    else:
        left_height = find_height(root.left)
        right_height = find_height(root.right)

        return max(left_height, right_height) + 1


tree = None
tree = insert(tree, 5)
tree = insert(tree, 3)
tree = insert(tree, 7)
tree = insert(tree, 2)
tree = insert(tree, 4)
tree = insert(tree, 6)
tree = insert(tree, 8)

height_of_tree = find_height(tree)
print(f"Altura del árbol: {height_of_tree}")