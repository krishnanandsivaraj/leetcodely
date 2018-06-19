class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, item):
        self.root = self._insert(self.root, item)
        self.size += 1

    def _insert(self, root, item):
        if not root:
            root = TreeNode(item)
            return root
        if item < root.val:
            root.left = self._insert(root.left, item)
        else:
            root.right = self._insert(root.right, item)
        return root

    def find(self, item):
        return self._find(self.root, item)

    def _find(self, root, item):
        if not root:
            return False
        if item > root.val:
            return self._find(root.right, item)
        elif item < root.val:
            return self._find(root.left, item)
        else:
            return True


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(12)
    bst.insert(9)
    bst.insert(13)
    print(bst.size)
    print(bst.find(11))
