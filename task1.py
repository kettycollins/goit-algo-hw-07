class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_max_value(root):
    if root is None:
        return None
    
    current = root
    while current.right is not None:
        current = current.right
    return current.key

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(12)
root.right.right = Node(20)

max_value = find_max_value(root)
print("Найбільше значення в дереві:", max_value)
