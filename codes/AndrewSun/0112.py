# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        if not root:
            return 

        ans = []
        # Use stack to iterate / Use set to replace the arguments in recursive function
        stack = [(root, sum, [root.val])]
        # Iterate begin:
        while (stack):
            curNode, target, curPath = stack.pop()
            # Found the leaf node which satisfied the target. Append the path to ans
            if (curNode.val == target) and not(curNode.left or curNode.right):
                ans.append(curPath)
            # Append the right node first, then left node, because stack is LIFO. Use this sequence to realize DFS
            if curNode.right:
                stack.append((curNode.right, target - curNode.val, curPath + [curNode.right.val]))
            if curNode.left:
                stack.append((curNode.left, target - curNode.val, curPath + [curNode.left.val]))
        return ans
        
        

# test case
root = TreeNode(5)
node1 = TreeNode(4)
node2 = TreeNode(8)
root.left = node1
root.right = node2
