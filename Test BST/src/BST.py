from src.Node import Node

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        z = Node(key)
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y

        if y is None:
            # albero vuoto
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def search(self, key):
        x = self.root
        while x is not None and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def reset(self):
        self.root = None

    # stampe
    def preorder_walk(self, x):
        if x is not None:
            print(x.key, sep = ", ")
            self.inorder_walk(x.left)
            self.inorder_walk(x.right)

    def inorder_walk(self, x):
        if x is not None:
            self.inorder_walk(x.left)
            print(x.key, sep = ", ")
            self.inorder_walk(x.right)

    def postorder_walk(self, x):
        if x is not None:
            self.inorder_walk(x.left)
            self.inorder_walk(x.right)
            print(x.key, sep = ", ")