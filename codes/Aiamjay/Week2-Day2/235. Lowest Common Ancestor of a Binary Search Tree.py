# encoding=utf-8
# 二叉搜索树


def solution1(root, p, q):
    head = root
    while head:
        # 不同的叉，返回当前叉
        if q.val < head.val < p.val \
                or p.val < head.val < q.val \
                or (p.val == head.val) \
                or (q.val == head.val):
            return head
        elif p.val < head.val and q.val < head.val:
            head = head.left
        else:
            head = head.right


def solution2(root, p, q):
    if q.val > root.val and p.val > root.val:
        return solution2(root.right, p, q)
    elif q.val < root.val and p.val < root.val:
        return solution2(root.left, p. q)
    else:
        return root
