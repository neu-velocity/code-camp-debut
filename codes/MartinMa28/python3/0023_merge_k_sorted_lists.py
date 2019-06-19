import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.heap = []

    def mergeKLists(self, lists):
        def _recursive_merge():
            if self.heap == []:
                return None

            popped = heapq.heappop(self.heap)
            ind = popped[1]
            min_node = popped[2]
            merged_list = min_node
            if min_node.next:
                heapq.heappush(self.heap, (min_node.next.val, ind, min_node.next))
            
            merged_list.next = _recursive_merge()
            return merged_list
        
        # remove None
        lists = list(filter(lambda x: x, lists))
        
        for ind, l in enumerate(lists):
            heapq.heappush(self.heap, (l.val, ind, l))

        return _recursive_merge()

        

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)

    lists = [l1, l2, l3]

    solu = Solution()
    merged = solu.mergeKLists(lists)
    print(merged)