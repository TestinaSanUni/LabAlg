from src.Node import Node

class BST:
    # costruttore
    def __init__(self):
        self.root = None

    # gestione altezza
    def get_height(self, node):
        if node is None:
            return 0
        return getattr(node, 'h', 1)

    # aggiornamento altezza
    def update_height(self, node):
        if node is not None:
            left_h = self.get_height(node.left)
            right_h = self.get_height(node.right)
            node.h = 1 + max(left_h, right_h)

    # inserimento
    def insert(self, key):
        z = Node(key)
        z.h = 1
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
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        temp = z
        while temp is not None:
            self.update_height(temp)
            temp = temp.p

    # ricerca
    def search(self, key):
        x = self.root
        while x is not None and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    # reset
    def reset(self):
        self.root = None

    # stampe
    def preorder_walk(self, x):
        if x is not None:
            print(f"K:{x.key} (H:{x.h})", end=" | ")
            self.preorder_walk(x.left)
            self.preorder_walk(x.right)

    def inorder_walk(self, x):
        if x is not None:
            self.inorder_walk(x.left)
            print(f"K:{x.key} (H:{x.h})", end=" | ")
            self.inorder_walk(x.right)

    def postorder_walk(self, x):
        if x is not None:
            self.postorder_walk(x.left)
            self.postorder_walk(x.right)
            print(f"K:{x.key} (H:{x.h})", end=" | ")