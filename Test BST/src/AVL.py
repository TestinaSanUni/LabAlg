from src.Node import Node
from BST import BST

class AVL(BST):
    # controllo bilanciamento
    def get_balance(self, node):
        if self.is_nil(node):
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # rotazione destra
    def right_rotate(self, y):
        x = y.left
        if self.is_nil(x): return y

        temp = x.right
        x.right = y
        y.left = temp

        x.p = y.p
        y.p = x

        if not self.is_nil(temp):
            temp.p = y

        # aggiornamento altezza
        self.update_height(y)
        self.update_height(x)
        return x

    # rotazione sinistra
    def left_rotate(self, x):
        y = x.right
        if self.is_nil(y): return x

        temp = y.left
        y.left = x
        x.right = temp

        y.p = x.p
        x.p = y

        if not self.is_nil(temp):
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
        if self.is_nil(node):
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
