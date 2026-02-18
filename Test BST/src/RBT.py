from src.Node import Node
from BST import BST

class RBT(BST):
    def __init__(self):
        super().__init__()
        self.nil = Node(None)
        self.nil.color = 'BLACK'
        self.root = self.nil

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

    def insert(self, key):
        z = Node(key)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            # print("chiave di z: ", z.key, ", chiave di x: ", x.key, ", chiave di y: ", y.key)
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

        # Setup finale specifico RB
        z.left = self.nil
        z.right = self.nil
        z.color = 'RED'
        self.rb_insert_fixup(z)

    def rb_insert_fixup(self, z):
        while z.p.color == 'RED':
            if z.p == z.p.p.left:
                y = z.p.p.right  # Lo zio
                if y.color == 'RED':  # Caso 1
                    z.p.color = 'BLACK'
                    y.color = 'BLACK'
                    z.p.p.color = 'RED'
                    z = z.p.p
                else:
                    if z == z.p.right:  # Caso 2
                        z = z.p
                        self.left_rotate(z)
                    # Caso 3
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self.right_rotate(z.p.p)
            else:  # Simmetrico (destra)
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

    # Per RB, la ricerca deve gestire self.nil invece di None
    def search(self, key):
        x = self.root
        while x != self.nil and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x if x != self.nil else None

    def reset(self):
        self.root = self.nil

    # === STAMPE ===
    def preorder_walk(self, x):
        if x is not None:
            print(x.key)
            self.inorder_walk(x.left)
            self.inorder_walk(x.right)

    def inorder_walk(self, x):
        if x is not None:
            self.inorder_walk(x.left)
            print(x.key)
            self.inorder_walk(x.right)

    def postorder_walk(self, x):
        if x is not None:
            self.inorder_walk(x.left)
            self.inorder_walk(x.right)
            print(x.key)