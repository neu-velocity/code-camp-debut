# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue


class Solution1(object):
    def levelOrder(self, root):
        """
        Queue
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        cache = Queue()
        cache.put(root)
        result = []
        while not cache.empty():
            result.append([])
            for _ in range(cache.qsize()):
                node = cache.get()
                if node.left: cache.put(node.left)
                if node.right: cache.put(node.right)
                if node: result[-1].append(node.val)
        return result


class Solution2(object):
    def levelOrder(self, root):
        """
        List with slicing
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        cache = [root]
        result = []
        while cache:
            result.append([])
            l = len(cache)
            for index in range(l):
                node = cache[index]
                if node.left:
                    cache.append(node.left)
                if node.right:
                    cache.append(node.right)
                if node:
                    result[-1].append(node.val)
            cache = cache[l:]
        return result
