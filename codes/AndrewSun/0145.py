# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        cur = TreeNode(None)
        stack = []
        ans = []
        while(cur or stack):
            if cur:
                stack.append(cur)
                ans.insert(0, cur.val)
                cur = cur.right
            else:
                cur = stack.pop().left
        return ans
                