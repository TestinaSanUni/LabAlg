class Node:
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None

        self.color = 'RED' # RED o BLACK

        self.h = 0