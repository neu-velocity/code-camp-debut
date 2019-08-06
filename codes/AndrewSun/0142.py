class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if not fast.next or not fast.next.next:
            return None
        else:
            while (head != slow):
                head = head.next
                slow = slow.next
            return slow  