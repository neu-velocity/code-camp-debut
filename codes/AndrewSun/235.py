class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # The initial node
        node = root
        while(node):
            # both p and q are in the left subtree
            if (p.val < node.val) and (q.val < node.val):
                node = node.left
            # both p and Q are in the right subtree
            elif (p.val > node.val) and (q.val > node.val):
                node = node.right
            # LCA is found
            else:
                return node