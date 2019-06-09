"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        using hashmap/dictionary to record the original node as the key 
        with copied node as the value
        creating the random pointer for each copied nodes by retrieving the corresponding
        copied node which random pointer points to
        """
        if head == None:
            return None
        
        d = dict()
        res = Node(head.val, None, None)
        d[head] = res
        copy = res
        curr = head.next
        
        while curr:
            node = Node(curr.val, None, None)
            copy.next = node
            d[curr] = node #record d[original] = copied node
            copy = copy.next
            curr = curr.next
        
        copy = res #move back to the starting node
        curr = head
        
        while curr:
            if curr.random != None:
                copy.random = d[curr.random]#retrieve corresponding copied node
            curr = curr.next
            copy = copy.next
        
        return res


    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        O(1) space
        creating copied of each node next to its original one
        A -> A' -> B -> B' etc.
        """
        if head == None:
            return head
        
        node = head
        while node:
            tmp = node.next
            copy = Node(node.val, None, None)
            node.next = copy
            copy.next = tmp
            
            node = node.next.next #move onto next original node
        
        
        pointer = head
        while pointer:
            pointer.next.random = pointer.random.next if pointer.random else None
            pointer = pointer.next.next #move onto next original node

        
        #break apart: A -> B and A' -> B'
        pointer_ori = head
        pointer_copy = head.next
        res = head.next
        while pointer_ori:
            pointer_ori.next = pointer_ori.next.next
            pointer_copy.next = pointer_copy.next.next if pointer_copy.next else None
            
            pointer_ori = pointer_ori.next
            pointer_copy = pointer_copy.next
        
        return res
       
            