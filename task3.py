class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def tree_sum(root):
    if root is None:
        return 0
    
    return root.key + tree_sum(root.left) + tree_sum(root.right)

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(12)
root.right.right = Node(20)

total_sum = tree_sum(root)
print("Сума значень в дереві:", total_sum)
