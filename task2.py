class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_min_value(root):
    if root is None:
        return None
    
    current = root
    while current.left is not None:
        current = current.left
    return current.key

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(12)
root.right.right = Node(20)

min_value = find_min_value(root)
print("Найменше значення в дереві:", min_value)
