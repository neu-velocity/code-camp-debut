class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return self.minDepth(root.right) + 1
        elif root.right is None:
            return self.minDepth(root.left) + 1
        else:
            left_child = self.minDepth(root.left)
            right_child = self.minDepth(root.right)

            return min((left_child, right_child)) + 1