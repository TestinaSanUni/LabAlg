from src.Node import Node
from BST import BST

class AVL(BST):
    # costruttore
    def __init__(self):
        super().__init__()
        self.root = None

    # gestione altezza
    def get_height(self, node):
        if node is None:
            return 0
        return node.h

    def update_height(self, node):
        if node is not None:
            node.h = 1 + max(self.get_height(node.left), self.get_height(node.right))

    # controllo bilanciamento
    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # rotazione destra
    def right_rotate(self, y):
        x = y.left
        if x is None: return y

        temp = x.right
        x.right = y
        y.left = temp

        x.p = y.p
        y.p = x

        if temp is not None:
            temp.p = y

        # aggiornamento altezza
        self.update_height(y)
        self.update_height(x)
        return x

    # rotazione sinistra
    def left_rotate(self, x):
        y = x.right
        if y is None: return x

        temp = y.left
        y.left = x
        x.right = temp

        y.p = x.p
        x.p = y

        if temp is not None:
            temp.p = x

        # aggiornamento altezze
        self.update_height(x)
        self.update_height(y)

        return y

    # inserimento
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            self.root.h = 1
            return

        self.root = self.insert_recursive(self.root, key)

    # inserimento ricorsivo
    def insert_recursive(self, node, key):
        if node is None:
            new_node = Node(key)
            new_node.h = 1
            return new_node

        if key < node.key:
            node.left = self.insert_recursive(node.left, key)
            node.left.p = node
        else:
            node.right = self.insert_recursive(node.right, key)
            node.right.p = node

        self.update_height(node)
        balance = self.get_balance(node)

        # caso left left
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # caso right right
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # caso left right
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # caso right left
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    # reset
    def reset(self):
        self.root = None

    # stampa
    def preorder_walk(self, x):
        if x is not None:
            print(f"Key: {x.key}, H: {x.h}")
            self.preorder_walk(x.left)
            self.preorder_walk(x.right)

    def inorder_walk(self, x):
        if x is not None:
            self.inorder_walk(x.left)
            print(f"Key: {x.key}, H: {x.h}")
            self.inorder_walk(x.right)

    def postorder_walk(self, x):
        if x is not None:
            self.postorder_walk(x.left)
            self.postorder_walk(x.right)
            print(f"Key: {x.key}, H: {x.h}")