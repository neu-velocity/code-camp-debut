class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursive
    # def lowestCommonAncestor(self, root, p, q):
    #     """
    #     :type root: TreeNode
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: TreeNode
    #     """
    #     com_ances = None

    #     def recursive_tree(cur_node):
    #         if cur_node is None:
    #             return False

    #         sub_l = recursive_tree(cur_node.left)
    #         sub_r = recursive_tree(cur_node.right)
    #         cur = (cur_node is p) or (cur_node is q)

    #         if sub_l + sub_r + cur >= 2:
    #             nonlocal com_ances
    #             com_ances = cur_node

    #         return cur or sub_l or sub_r
        
    #     recursive_tree(root)

    #     return com_ances

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pass        

