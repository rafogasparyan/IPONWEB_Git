class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None


n = Node(5)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        break
                    else:
                        current = current.right

    def search(self, value):
        c = self.root
        return self.search2(c, value)

    def search2(self, root, value):
        if root is None:
            return False
        if value == root.value:
            return root
        elif value > root.value:
            return self.search2(root.left, value)
        else:
            return self.search2(root.left, value)

    def delete(self, value):
        if self.root is None:
            return False
        else:
            parent = None
            current = self.root
            while current and current.value != value:
                parent = current
                if value < current.value:
                    current = current.left
                else:
                    current = current.right
            if current is None:
                return False
            if current.left is None and current.right is None:
                if parent is None:
                    self.root = None
                elif parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            elif current.right is None:
                if parent is None:
                    self.root = current.left
                elif parent.left == current:
                    parent.left = current.left
                else:
                    parent.right = current.left
            elif current.left is None:
                if parent is None:
                    self.root = current.right
                elif parent.left == current:
                    parent.left = current.right
                else:
                    parent.right = current.right
            else:
                successor = current.right
                while successor.left:
                    successor = successor.left
                current.value = successor.value
                self.delete(successor.value)
            return True


"""
bst = BinarySearchTree()

bst.insert(5)
print(bst.root.value)

bst.insert(4)
bst.insert(2)
bst.delete(4)

print(bst.root.left.value)
"""
