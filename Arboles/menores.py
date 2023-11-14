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

def numbers_less_than(root, target):
    if root is None:
        return []
    
    result = []
    if root.value < target:
        result.append(root.value)
        result += numbers_less_than(root.left, target)
        result += numbers_less_than(root.right, target)
    elif root.value >= target:
        result += numbers_less_than(root.left, target)
    
    return result


tree = None
tree = insert(tree, 5)
tree = insert(tree, 3)
tree = insert(tree, 7)
tree = insert(tree, 2)
tree = insert(tree, 4)
tree = insert(tree, 6)
tree = insert(tree, 8)

# Encontrar los números menores
target_value = int(input("numero a comparar"))
result = numbers_less_than(tree, target_value)
print(f"Números menores que {target_value}: {result}")