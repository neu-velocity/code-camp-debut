class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    
    def __init__(self):
        self.traversal = []

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None

        self.postorderTraversal(root.left)

        self.postorderTraversal(root.right)

        self.traversal.append(root.val)

        return self.traversal

    
    def preorderTraversal(self, root):
        if root is None:
            return None

        self.traversal.append(root.val)

        self.preorderTraversal(root.left)

        self.preorderTraversal(root.right)

        return self.traversal


    def inorderTraversal(self, root):
        if root is None:
            return None

        self.inorderTraversal(root.left)

        self.traversal.append(root.val)

        self.inorderTraversal(root.right)

        return self.traversal