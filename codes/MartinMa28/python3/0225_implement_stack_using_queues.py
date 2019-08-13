from copy import deepcopy

class MyStack:
    """
    Last in first out
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        new_queue = []
        while len(self.queue) > 1:
            new_queue.append(self.queue.pop(0))
        
        last_ele = self.queue.pop(0)
        self.queue = new_queue

        return last_ele


    def top(self) -> int:
        """
        Get the top element.
        """
        queue_copy = deepcopy(self.queue)
        while len(self.queue) > 1:
            self.queue.pop(0)
        
        last_ele = self.queue.pop(0)
        self.queue = queue_copy

        return last_ele
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()