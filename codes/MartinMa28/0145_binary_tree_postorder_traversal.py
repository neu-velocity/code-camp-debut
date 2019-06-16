class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    
    def __init__(self):
        self.traversal = []
        self.stack = []

    def postorderTraversal_recursive(self, root):
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

    
    def preorderTraversal_recursive(self, root):
        if root is None:
            return None

        self.traversal.append(root.val)

        self.preorderTraversal(root.left)

        self.preorderTraversal(root.right)

        return self.traversal


    def inorderTraversal_recursive(self, root):
        if root is None:
            return None

        self.inorderTraversal(root.left)

        self.traversal.append(root.val)

        self.inorderTraversal(root.right)

        return self.traversal


    def preorderTraversal(self, root):
        if root is None:
            return []

        self.stack.append(root)

        while len(self.stack) > 0:
            stack_top = self.stack.pop()
            self.traversal.append(stack_top.val)

            # traverse the left child firstly, 
            # so push the right child before the left child
            if stack_top.right:
                self.stack.append(stack_top.right)

            if stack_top.left:
                self.stack.append(stack_top.left)

        return self.traversal


    def inorderTraversal(self, root):
        if root is None:
            return []

        current = root

        while True:
            if current:
                self.stack.append(current)
                current = current.left
                
            else:
                stack_top = self.stack.pop()
                self.traversal.append(stack_top.val)
                current = stack_top.right

            if len(self.stack) == 0 and current is None:
                break
        
        return self.traversal

            
    def postorderTraversal(self, root):
        """
        Get the reversed postorder traversal, which is root-right-left,
        using the variation of preorder traversal, then reverse it.
        """
        if root is None:
            return []

        self.stack.append(root)

        while len(self.stack) > 0:
            stack_top = self.stack.pop()
            self.traversal.append(stack_top.val)

            # push the left child firstly
            if stack_top.left:
                self.stack.append(stack_top.left)

            if stack_top.right:
                self.stack.append(stack_top.right)

        
        self.traversal.reverse()

        return self.traversal

