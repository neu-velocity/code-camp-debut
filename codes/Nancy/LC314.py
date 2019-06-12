# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        record = [(root, 0)]
        d = dict()
        res = []
        while record:
            node, num = record.pop(0)
            if num in d:
                d[num] += [node.val]
            else:
                d[num] = [node.val]
            
            if node.left:
                record.append((node.left, num - 1))
            if node.right:
                record.append((node.right, num + 1))
        
        for k,v in sorted(d.items()):
            res.append(v)
        return res