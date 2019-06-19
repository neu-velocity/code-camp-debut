import functools

class Solution:
    def __init__(self):
        self.stack = []
        self.traversal = []

    def _inorder_traversal(self, root):
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

    def isValidBST(self, root):
        """
        Get the inorder traversal,
        if it is BST, the traversal should be in ascending order.
        """
        if root is None:
            return True

        inorder_t = self._inorder_traversal(root)

        valid = True
        prev = inorder_t[0]
        for i in range(1, len(inorder_t)):
            if prev < inorder_t[i]:
                prev = inorder_t[i]
            else:
                valid = False

        return valid
