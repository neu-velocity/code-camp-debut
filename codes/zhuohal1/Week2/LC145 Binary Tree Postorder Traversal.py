# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## recursive

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        elif not root.left:
            return self.postorderTraversal(root.right) + [root.val]
        elif not root.right:
            return self.postorderTraversal(root.left) + [root.val]
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## iterative

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans, stack = [], [(0, root)]
        while stack:
            visited, node = stack.pop()
            if not node:
                continue
            if not visited:
                stack.extend([(1, node), (0, node.right), (0, node.left)])
            else:
                ans.append(node.val)
        return ans