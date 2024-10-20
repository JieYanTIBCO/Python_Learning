class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None  # 左子节点
        self.right = None  # 右子节点


class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    # 前序遍历
    def pre_order(self, node):
        if node:
            print(node.value, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    # 中序遍历
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value, end=" ")
            self.in_order(node.right)

    # 后序遍历
    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value, end=" ")


# 创建二叉树
tree = BinaryTree(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)

# 测试遍历
print("Pre-order Traversal:")
tree.pre_order(tree.root)  # 输出: 1 2 4 5 3
print("\nIn-order Traversal:")
tree.in_order(tree.root)   # 输出: 4 2 5 1 3
print("\nPost-order Traversal:")
tree.post_order(tree.root)  # 输出: 4 5 2 3 1
