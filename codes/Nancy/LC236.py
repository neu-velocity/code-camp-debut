# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        three cases:
        1. p and q locates at the left and right side of the parent node
        2. p and q both at the left children branch
        3. p and q both at the right children branch
        """
        if root == None or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        #case 1
        if left and right:
            return root
        
        #case 2 and 3
        return left or right