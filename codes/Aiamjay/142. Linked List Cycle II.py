# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 这个是要返回环形结构的头节点，用双指针不一定能定位到头节点
        if not head:
            return None
        slow = fast = third = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                while third is not slow:
                    third = third.next
                    slow = slow.next
                return slow
        return None
