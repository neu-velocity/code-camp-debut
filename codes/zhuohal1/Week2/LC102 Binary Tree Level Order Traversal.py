# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])    # add current parent
            tmp = []
            for node in level:
                tmp.extend([node.left, node.right])
            level = [node for node in tmp if node]
        return ans