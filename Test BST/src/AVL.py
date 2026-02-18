from src.Node import Node
from BST import BST

class AVL(BST):
    def get_height(self, node):
        if node is None:
            return 0
        return node.h

    def update_height(self, node):
        node.h = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        if x is None: return y  # Protezione minima

        temp = x.right

        # Rotazione
        x.right = y
        y.left = temp

        # Aggiorna altezze (fondamentale farlo in quest'ordine)
        self.update_height(y)
        self.update_height(x)

        return x

    def left_rotate(self, x):
        y = x.right
        if y is None: return x  # Protezione minima

        temp = y.left

        # Rotazione
        y.left = x
        x.right = temp

        # Aggiorna altezze
        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
            node.left.p = node  # Mantieni il legame col padre
        else:
            node.right = self._insert_recursive(node.right, key)
            node.right.p = node

        self.update_height(node)
        balance = self.get_balance(node)

        # Caso Left Left
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Caso Right Right
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Caso Left Right
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Caso Right Left
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def reset(self):
        self.root = None

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