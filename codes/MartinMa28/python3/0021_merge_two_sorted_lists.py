class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # iterative
    def mergeTwoListsIterative(self, l1, l2):
        new_head = ListNode(-999)
        cur = new_head

        while True:
            if l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    cur = cur.next
                    l1 = l1.next
                else:
                    cur.next = l2
                    cur = cur.next
                    l2 = l2.next
            
            elif l1 is None:
                cur.next = l2
                return new_head.next
            
            elif l2 is None:
                cur.next = l1
                return new_head.next

    # recursive
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

        
            
