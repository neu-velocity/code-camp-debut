# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return (self.postorderTraversal(root.left) if root.left else []) +\
               (self.postorderTraversal(root.right) if root.right else []) +\
               [root.val]
