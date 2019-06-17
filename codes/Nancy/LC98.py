# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def helper(root, lower, upper):
            if root == None:
                return True
            
            if root.val <= lower or root.val >= upper:
                return False
            
            left = helper(root.left, lower, root.val)
            right = helper(root.right, root.val, upper)
            
            # if left != True:
            #     return False
            # if right != True:
            #     return False
            
            # return True
            return left and right
        
        return helper(root, lower = float('-Inf'), upper = float('Inf'))