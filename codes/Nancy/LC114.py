# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
DFS solution
For every treenode, we move its left branch to the right
and add its actual right branch after the movement
"""
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        if root == None:#if input root is None
            return None
        if root.left:
            self.flatten(root.left)
        if root.right:
            self.flatten(root.right)
        
        temp = root.right #record the actual right branch
        root.right = root.left #move left branch to the right
        root.left = None
        while root.right:#make sure we are at the end of right branch
            root = root.right
        root.right = temp #merge the actual right branch

 """
 Non recursive solution
 """   

    def flatten(self, root):

        curr = root
        while curr:
            if curr.left:
                temp = curr.right #record the actual right branch
                curr.right = curr.left
                curr.left = None #don't forget the set the left branch = None
                node = curr.right
                while node.right:
                    node = node.right
                node.right = temp
            
            curr = curr.right
        