from copy import deepcopy

class MyQueue:
    """
    First in first out
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        reverse_order = []
        while len(self.stack) > 1:
            reverse_order.append(self.stack.pop())

        first_ele = self.stack.pop()

        assert len(self.stack) == 0
        
        while len(reverse_order) > 0:
            self.stack.append(reverse_order.pop())
        
        return first_ele
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        stack_copy = deepcopy(self.stack)
        while len(self.stack) > 1:
            self.stack.pop()
        
        first_ele = self.stack.pop()
        self.stack = stack_copy
        return first_ele
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0