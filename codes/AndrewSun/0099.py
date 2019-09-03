class Solution:
    # Morris In-order traverse解法
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur, change, prev = root,[], TreeNode(float('-inf'))
      
        while cur:
            if cur.left:
                tmp = cur.left
                # 找出左孩子的最右叶子节点
                while tmp.right and tmp.right!= cur: tmp = tmp.right
                # 第一次遍历左子树，将最右叶子节点连接到cur
                if not tmp.right:
                    tmp.right, cur = cur, cur.left #继续往左子树遍历
                    continue
                # 如果tmp.right不为None，说明左孩子已经遍历过
                tmp.right = None
            # print(cur.val) 直接访问cur    
            if cur.val <= prev.val: change.append([prev, cur])
            # 继续遍历cur的右孩子部分
            prev, cur = cur, cur.right
        # Recover the tree
        change[0][0].val, change[-1][1].val = change[-1][1].val, change[0][0].val
            