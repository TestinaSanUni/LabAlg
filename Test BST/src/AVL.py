from src.Node import Node
from src.BST import BST

class AVL(BST):
    # rotazione sinistra
    def left_rotate(self, old):
        new = old.right
        old.right = new.left

        old.h = max(old.left.h, old.right.h) + 1

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
        new.h = max(new.left.h, new.right.h) + 1
        old.p = new

    # rotazione destra
    def right_rotate(self, old):
        new = old.left
        old.left = new.right

        old.h = max(old.left.h, old.right.h) + 1

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
        new.h = max(new.left.h, new.right.h) + 1
        old.p = new

    # fixup
    def fixup(self, node):
        curr = node.p
        while curr != self.get_nil():
            curr.h = max(curr.left.h, curr.right.h) + 1

            balance = curr.left.h - curr.right.h

            if balance == 2:
                if (curr.left.left.h - curr.left.right.h) == -1:
                    self.left_rotate(curr.left)
                self.right_rotate(curr)
                curr = curr.p
            elif balance == -2:
                if (curr.right.left.h - curr.right.right.h) == 1:
                    self.right_rotate(curr.right)
                self.left_rotate(curr)
                curr = curr.p

            curr = curr.p

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
        node.h = 1

        self.fixup(node)
