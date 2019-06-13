# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    """
    bfs
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return[]
        
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        
        return res
    
    """
    dfs
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        
        def dfs_helper(root, level):
            if root == None:
                return
            if len(res) < level:
                res.append([root.val])
            else:
                res[level - 1] += [root.val]
            
            dfs_helper(root.left, level + 1)
            dfs_helper(root.right, level + 1)
        
        dfs_helper(root, 1)
        return res