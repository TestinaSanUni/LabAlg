from src.Node import Node
from src.BST import BST

class AVL(BST):
    # gestione altezza
    def tree_height(self, node):
        if node is None:
            return 0
        return getattr(node, 'h', 1)

    def update_height(self, node):
        if node is not None:
            left_h = self.tree_height(node.left)
            right_h = self.tree_height(node.right)
            node.h = 1 + max(left_h, right_h)

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

        self.update_height(old)
        self.update_height(new)

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

        self.update_height(old)
        self.update_height(new)

    # fixup
    def fixup(self, node):
        curr = node.p
        while curr != self.get_nil():
            self.update_height(curr)
            balance = self.tree_height(curr.left) - self.tree_height(curr.right)

            if balance == 2:
                if (self.tree_height(curr.left.left) - self.tree_height(curr.left.right)) == -1:
                    self.left_rotate(curr.left)
                self.right_rotate(curr)
                curr = curr.p
            elif balance == -2:
                if (self.tree_height(curr.right.left) - self.tree_height(curr.right.right)) == 1:
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
