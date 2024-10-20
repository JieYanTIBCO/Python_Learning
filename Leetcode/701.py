# When try to add the value as a node, when need to travers the tree
# if val > root.value, go right
# if val < root.value, go left
# if non-duplicated value found, then we
# 1. create a leaf node
# 2. linked the parent treenode either left or right.

def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)

    current_node = root

    while True:
        if current_node.value == val:
            print("The value is duplicated in the tree")
            return root
        elif current_node.value > val:  # search left node since node value > val
            if not current_node.left:
                current_node.left = TreeNode(val)
                return root
            current_node = current_node.left
        else:
            if not current_node.right:
                current_node.right = TreeNode(val)
                return root
            current_node = current_node.right
