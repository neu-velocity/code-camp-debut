class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.queue = []
        self.level_traversal = []


    def levelOrder(self, root):
        if root is None:
            return []

        self.queue.append((root, 1))

        while len(self.queue) > 0:
            popped_node, popped_level = self.queue.pop(0)
            if popped_node.left:
                self.queue.append((popped_node.left, popped_level + 1))
            
            if popped_node.right:
                self.queue.append((popped_node.right, popped_level + 1))

            if len(self.level_traversal) < popped_level:
                self.level_traversal.append([])
            
            self.level_traversal[popped_level - 1].append(popped_node.val)

        return self.level_traversal

    @classmethod
    def _height(cls, root):
        if root is None:
            return 0
        
        l_h = cls._height(root.left) + 1
        r_h = cls._height(root.right) + 1

        return max((l_h, r_h))

    @classmethod
    def _nodes_in_give_level(cls, root, level):
        if root is None:
            return []

        if level == 1:
            return [root.val]

        if level > 1:
            return cls._nodes_in_give_level(root.left, level - 1) + 
            cls._nodes_in_give_level(root.right, level - 1)


    def levelOrder_recursively(self, root):
        h = Solution._height(root)
        for i in range(1, h + 1):
            self.level_traversal.append(Solution._nodes_in_give_level(root, i))
        
        return self.level_traversal