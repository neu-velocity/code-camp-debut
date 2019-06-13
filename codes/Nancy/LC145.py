# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def dfs_helper(root):
            if root == None:
                return None
            dfs_helper(root.left)
            dfs_helper(root.right)
            res.append(root.val)
        
        dfs_helper(root)
        return res
    
    """
    iterative
    """
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        stack = []
        stack.append(root)
        res = []
        while stack:
            temp = stack.pop()
            res.append(temp.val)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        
        return res[::-1]