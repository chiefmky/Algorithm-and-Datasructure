class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        temp = Node(val)
        if self.root is None:
            self.root = temp
            return
        node = self.root

        while node:
            if val < node.data:
                if node.left is None:
                    node.left = temp
                    return
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = temp
                    return
                else:
                    node = node.right

    def find(selfkey):
        if node:
            if key < node.data:
                find(node.data.left, key)
            elif key > nodedata:
                find(node.data.right, key)
            else:
                return node.data