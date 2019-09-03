class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        # top-down recursion
        def recursion(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            if not recursion(node.left, lower, node.val):
                return False
            if not recursion(node.right, node.val, upper):
                return False
            return True
        return recursion(root)
