# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from math import inf


class Solution:
    # 如何简化这种复杂的if else判断
    def solution1(self, root: TreeNode) -> bool:
        def valid_tree(root, upper, lower):
            if not root:
                return True
            if root.left:
                if not lower < root.left.val < root.val:
                    return False
            if root.right:
                if not root.val < root.right.val < upper:
                    return False
            return valid_tree(root.left, root.val, lower) and valid_tree(root.right, upper, root.val)

        return valid_tree(root, inf, -inf)

    def solution2(self, root: TreeNode) -> bool:

        # 利用中序遍历的性质
        self.order = [-inf]

        def in_order(root):
            left = in_order(root.left) if root.left else True
            if not left or self.order[-1] >= root.val:
                return False
            self.order.append(root.val)
            return in_order(root.right) if root.right else True

        return in_order(root) if root else True
