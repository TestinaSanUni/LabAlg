from src.Node import Node
from src.BST import BST

class RBT(BST):
    # costruttore
    def __init__(self):
        self.nil = Node(None)
        self.get_nil().color = 'BLACK'
        super().__init__()

    # metodi ausiliari
    def get_nil(self):
        return self.nil

    def is_nil(self, node):
        return node is None or node == self.nil

    # rotazione sinistra
    def left_rotate(self, old):
        new = old.right
        old.right = new.left

        if new.left != self.get_nil():
            new.left.p = old

        new.p = old.p

        if old.p == self.get_nil():
            self.root = new
        elif old == old.p.left:
            old.p.left = new
        else:
            old.p.right = new

        new.left = old
        old.p = new

    # rotazione destra
    def right_rotate(self, old):
        new = old.left
        old.left = new.right

        if new.right != self.get_nil():
            new.right.p = old

        new.p = old.p

        if old.p == self.get_nil():
            self.root = new
        elif old == old.p.right:
            old.p.right = new
        else:
            old.p.left = new

        new.right = old
        old.p = new

    # inserimento
    def insert(self, key):
        node = Node(key)
        p = self.get_nil()
        curr = self.root

        while curr != self.get_nil():
            p = curr
            if node.key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        node.p = p

        if p == self.get_nil():
            self.root = node
        elif node.key < p.key:
            p.left = node
        else:
            p.right = node

        node.left = self.get_nil()
        node.right = self.get_nil()
        node.color = 'RED'

        self.fixup(node)

    # fixup
    def fixup(self, curr):
        while curr.p.color == 'RED':
            if curr.p == curr.p.p.left:
                uncle = curr.p.p.right

                if uncle.color == 'RED':
                    curr.p.color = 'BLACK'
                    uncle.color = 'BLACK'
                    curr.p.p.color = 'RED'
                    curr = curr.p.p
                else:
                    if curr == curr.p.right:
                        curr = curr.p
                        self.left_rotate(curr)

                    curr.p.color = 'BLACK'
                    curr.p.p.color = 'RED'
                    self.right_rotate(curr.p.p)
            else:
                uncle = curr.p.p.left

                if uncle.color == 'RED':
                    curr.p.color = 'BLACK'
                    uncle.color = 'BLACK'
                    curr.p.p.color = 'RED'
                    curr = curr.p.p
                else:
                    if curr == curr.p.left:
                        curr = curr.p
                        self.right_rotate(curr)
                    curr.p.color = 'BLACK'
                    curr.p.p.color = 'RED'
                    self.left_rotate(curr.p.p)
        self.root.color = 'BLACK'
