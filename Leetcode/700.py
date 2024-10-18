# 定义二叉树节点的类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 搜索二叉搜索树中的值


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:  # 如果节点为空，返回 None
            return None
        if root.val == val:  # 如果当前节点的值等于 val，返回当前节点
            return root
        elif val < root.val:  # 如果 val 小于当前节点的值，递归左子树
            return self.searchBST(root.left, val) # type: ignore
        else:  # 如果 val 大于当前节点的值，递归右子树
            return self.searchBST(root.right, val) # type: ignore

# 辅助函数，用于插入节点到 BST 中


def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

# 创建二叉搜索树的辅助函数


def create_bst_from_list(values):
    root = None
    for value in values:
        root = insert_into_bst(root, value)
    return root


# 测试程序
if __name__ == "__main__":
    # 构建测试用例 1
    bst_values = [4, 2, 7, 1, 3]  # 生成二叉搜索树
    root = create_bst_from_list(bst_values)

    solution = Solution()

    # 测试 1：查找值 2
    result = solution.searchBST(root, 2) # type: ignore
    if result:
        print(f"找到节点: {result.val}")
        print(f"子树: [{result.val}, {result.left.val if result.left else None}, {
              result.right.val if result.right else None}]")
    else:
        print("没有找到节点 2")

    # 测试 2：查找值 5
    result = solution.searchBST(root, 5) # type: ignore
    if result:
        print(f"找到节点: {result.val}")
    else:
        print("没有找到节点 5")
