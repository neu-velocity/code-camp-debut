from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue, ans = deque([root]), []
        while(queue):
            curLevelVals = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left) 
                if cur.right:
                    queue.append(cur.right)
                curLevelVals.append(cur.val)
            ans.append(curLevelVals)
        return ans
                
            