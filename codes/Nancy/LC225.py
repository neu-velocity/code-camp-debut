from collections import deque
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_1 = deque()
        self.queue_2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue_1.append(x)
        if len(self.queue_1) > 1:
            while len(self.queue_1) > 1:
                self.queue_2.append(self.queue_1.popleft())
        while len(self.queue_2) > 0:
            self.queue_1.append(self.queue_2.popleft())


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.queue_1) > 0:
            return self.queue_1.popleft()
        else:
            return False

    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.queue_1) > 0:
            return self.queue_1[0]
        else:
            return False

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue_1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()