class TreeNode:
    def __init__(self, value, color='RED'):
        self.value = value      # The value stored in the node
        self.color = color      # The color of the node, can be 'RED' or 'BLACK'
        self.left = None        # Pointer to the left child
        self.right = None       # Pointer to the right child
        self.parent = None      # Pointer to the parent node


class RedBlackTree:
    def __init__(self):
        self.NIL = TreeNode(value=None, color='BLACK')  # Sentinel node (like a leaf, always black)
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right                     # define right child node y
        x.right = y.left                # assign y's left node to x(current) right child.
        if y.left != self.NIL:          # if y left does have node
            y.left.parent = x           # assing x as this node'parent
        y.parent = x.parent             # after rotate, assign x and y has the same parents????
        if x.parent == None:            # if x is root
            self.root = y               # set y as root
        elif x == x.parent.left:        # x is a left child node of its parent's node
            x.parent.left = y           # assign y as parents's left node
        else:                           #
            x.parent.right = y          # assign y as parent's right node 
        y.left = x                      # assign x as y's left node
        x.parent = y                    # assing y as x's parent

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    def insert(self, value):
        new_node = TreeNode(value)
        new_node.left = self.NIL
        new_node.right = self.NIL
        new_node.parent = None

        y = None
        x = self.root

        # Standard BST insert
        while x != self.NIL:
            y = x
            if new_node.value < x.value:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y == None:  # Tree was empty
            self.root = new_node
        elif new_node.value < y.value:
            y.left = new_node
        else:
            y.right = new_node

        # New node must be red
        new_node.color = 'RED'

        # Fix violations of red-black tree properties
        self.fix_insert(new_node)

    def fix_insert(self, k):
        while k.parent and k.parent.color == 'RED':
            if k.parent == k.parent.parent.left:  # k's parent is a left child
                uncle = k.parent.parent.right
                if uncle.color == 'RED':  # Case 1: Uncle is red, only color flip needed
                    k.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:  # Case 2: k is a right child, requires left rotation
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'BLACK'  # Case 3: k is a left child, requires right rotation
                    k.parent.parent.color = 'RED'
                    self.right_rotate(k.parent.parent)
            else:  # k's parent is a right child
                uncle = k.parent.parent.left
                if uncle.color == 'RED':  # Case 1: Uncle is red, only color flip needed
                    k.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:  # Case 2: k is a left child, requires right rotation
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'BLACK'  # Case 3: k is a right child, requires left rotation
                    k.parent.parent.color = 'RED'
                    self.left_rotate(k.parent.parent)

        # Ensure root is always black
        self.root.color = 'BLACK'
