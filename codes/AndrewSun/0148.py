class Solution:
    def sortList(self, head: ListNode) -> ListNode:
				# Boundary Case
        if not head or not head.next:
            return head
				# dummy node is used for tracking mid_pre
        dummy = ListNode(0)
        dummy.next = head
        mid_pre = dummy
				# two pointers to divide the list from the middle
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            mid_pre = mid_pre.next
        # Cut down the first part
        mid = slow
        mid_pre.next = None
        
        # Sort the two parts recursively
        l = self.sortList(head)
        r = self.sortList(mid)
        return self.merge(l, r)
    
    def merge(self, l, r):
        if not l or not r:
            return l or r  # 学习这种python写法
        # Fix the head
        if l.val > r.val:
            l, r = r, l
        head = cur = l
        l = l.next
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return head