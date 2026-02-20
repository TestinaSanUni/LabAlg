from src.Node import Node
from BST import BST

class RBT(BST):
    # costruttore
    def __init__(self):
        self.nil = Node(None)
        self.nil.color = 'BLACK'
        self.nil.h = 0
        super().__init__()

    # metodi ausiliari
    def get_nil(self):
        return self.nil

    def is_nil(self, node):
        return node is None or node == self.nil

    # rotazione sinistra
    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.nil:
            y.left.p = x

        y.p = x.p

        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        y.left = x
        x.p = y

        # aggiornamento altezze
        self.update_height(x)
        self.update_height(y)

    # rotazione destra
    def right_rotate(self, x):
        y = x.left
        x.left = y.right

        if y.right != self.nil:
            y.right.p = x

        y.p = x.p

        if x.p == self.nil:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y

        y.right = x
        x.p = y

        # aggiornamento altezze
        self.update_height(x)
        self.update_height(y)

    # inserimento
    def insert(self, key):
        z = Node(key)
        z.h = 1
        y = self.nil
        x = self.root

        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.p = y

        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.left = self.nil
        z.right = self.nil
        z.color = 'RED'

        self.fixup(z)

        # aggiornamento altezze
        temp = z
        while temp != self.nil:
            self.update_height(temp)
            temp = temp.p

    # fixup
    def fixup(self, z):
        while z.p.color == 'RED':
            if z.p == z.p.p.left:
                y = z.p.p.right

                if y.color == 'RED':
                    z.p.color = 'BLACK'
                    y.color = 'BLACK'
                    z.p.p.color = 'RED'
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)

                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left

                if y.color == 'RED':
                    z.p.color = 'BLACK'
                    y.color = 'BLACK'
                    z.p.p.color = 'RED'
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self.left_rotate(z.p.p)
        self.root.color = 'BLACK'
