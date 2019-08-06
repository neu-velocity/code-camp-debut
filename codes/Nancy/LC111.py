# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    bfs
    """
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        queue = [root]
        res = 0
        
        while len(queue) != 0:
            res += 1
            for i in range(len(queue)):
                temp = queue.pop(0)
                if temp.left == None and temp.right == None:
                    return res
                if temp.left != None:
                    queue.append(temp.left)
                if temp.right != None:
                    queue.append(temp.right)
        return False
    
    """
    dfs
    """
    def minDepth(self, root: TreeNode) -> int:    
        if root == None:
            return 0
        
        if root.left == None and root.right != None:
            return self.minDepth(root.right) + 1
        elif root.right == None and root.left != None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1