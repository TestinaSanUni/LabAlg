from src.Node import Node

class BST:
    # costruttore
    def __init__(self):
        self.root = self.get_nil()

    # metodi ausiliari
    def get_nil(self):
        return None

    def is_nil(self, node):
        return node is None

    # gestione altezza
    def get_height(self, node):
        if node is None:
            return 0
        return getattr(node, 'h', 1)

    def update_height(self, node):
        if node is not None:
            left_h = self.get_height(node.left)
            right_h = self.get_height(node.right)
            node.h = 1 + max(left_h, right_h)

    # inserimento
    def insert(self, key):
        z = Node(key)
        z.h = 1
        y = self.get_nil()
        x = self.root

        while not self.is_nil(x):
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y

        if self.is_nil(y):
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        temp = z
        while not self.is_nil(temp):
            self.update_height(temp)
            temp = temp.p

    # ricerca
    def search(self, key):
        x = self.root
        while not self.is_nil(x) and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    # reset
    def reset(self):
        self.root = self.get_nil()
