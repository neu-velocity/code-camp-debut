class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        search_path = []
        def _find_node(root, val):
            search_path.append(root)
            if root.val == val:
                return None
            elif root.val < val:
                _find_node(root.right, val)
            elif root.val > val:
                _find_node(root.left, val)

        _find_node(root, p.val)
        p_path = search_path
        
        search_path = []

        _find_node(root, q.val)
        q_path = search_path

        for i in range(min((len(p_path), len(q_path)))):
            if p_path[i] is not q_path[i]:
                i -= 1
                break


        return p_path[i]

        


