# encoding= utf-8
import math

from codes.Aiamjay.utils.treenode import (
    TreeNode, create_tree_from_list,
    print_tree
)


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        def helper(root):
            if not root.left and not root.right:
                return 1
            return 1 + min(self.minDepth(root.left) if root.left else math.inf,
                           self.minDepth(root.right) if root.right else math.inf)

        if not root:
            return 0
        return helper(root)

    def test_solution(self):
        # case 1
        print("case1")
        a = [3, 9, 20, None, None, 15, 7]
        root = create_tree_from_list(a)
        print_tree(root)
        print(self.minDepth(root))

        # case 2
        print("case2")
        a = [3, None, None]
        root = create_tree_from_list(a)
        print_tree(root)
        print(self.minDepth(root))

        # case3
        print("case3")
        a = [None]
        root = create_tree_from_list(a)
        print_tree(root)
        print(self.minDepth(root))


if __name__ == '__main__':
    s = Solution()
    s.test_solution()
    pass
