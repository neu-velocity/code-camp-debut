class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # trivial case
        if n <= 0:
            return []
        def recursion(left, right):
            # boundary condition
            if left > right:
                return [None] # None is very important
            ans = []
            # recursion part
            for i in range(left, right+1):
                for j in recursion(left, i-1):
                    for k in recursion(i+1, right):
                        new = TreeNode(i)
                        new.left = j
                        new.right = k
                        ans.append(new)
            return ans if ans else [None] # [None] is very important
        
        return recursion(1, n)