# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode, left_max = float('-inf'), right_min = float('inf')) -> bool:
        if not root:
            return True
        if root.val <= left_max or root.val >= right_min:
            return False
        return self.isValidBST(root.left, left_max, min(right_min, root.val)) and self.isValidBST(root.right, max(left_max, root.val), right_min)