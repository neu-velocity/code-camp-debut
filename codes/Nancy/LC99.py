# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        O(n) - inorder traversal: record the root and its val in lists
        sort val
        """
        def inorder(root, nodes, vals):
            if root == None:
                return
            inorder(root.left, nodes, vals)
            nodes.append(root)
            vals.append(root.val)
            inorder(root.right, nodes, vals)
        
        nodes = []
        vals = []
        inorder(root,nodes,vals)
        vals.sort()
        
        for i in range(len(vals)):
            nodes[i].val = vals[i]

        #Note: need to work on the O(1) solution later