from src.Node import Node
import sys
sys.setrecursionlimit(10**6)

class BST:
    # costruttore
    def __init__(self):
        self.root = self.get_nil()

    # metodi ausiliari
    def get_nil(self):
        return None

    def is_nil(self, node):
        return node is None

    # calcolo altezza
    def tree_height(self, node):
        if self.is_nil(node):
            return 0
        return 1 + max(self.tree_height(node.left), self.tree_height(node.right))

    # inserimento
    def insert(self, key):
        node = Node(key)
        p = self.get_nil()
        curr = self.root

        while not self.is_nil(curr):
            p = curr
            if node.key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        node.p = p

        if self.is_nil(p):
            self.root = node
        elif node.key < p.key:
            p.left = node
        else:
            p.right = node

    # ricerca
    def search(self, key):
        curr = self.root
        while not self.is_nil(curr) and key != curr.key:
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    # reset
    def reset(self):
        self.root = self.get_nil()
