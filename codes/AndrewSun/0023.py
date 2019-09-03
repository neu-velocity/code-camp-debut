class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        counter = itertools.count()
        pq = []
        head = cur = ListNode(0)
        for i in lists:
            if i:
                count = next(counter)
                heapq.heappush(pq, (i.val, count, i))
        while pq:
            val, _, node = heapq.heappop(pq)
            new = ListNode(val)
            cur.next = new
            cur = cur.next
            node = node.next
            count = next(counter)
            if node:
               heapq.heappush(pq, (node.val, count, node))
        return head.next