class MyQueue:

    def __init__(self):
        self._stack1 = []
        self._stack2 = []
        

    def push(self, x: int) -> None:
        self._stack1.append(x)
        

    def pop(self) -> int:
        if not self._stack2:
            for _ in range(len(self._stack1)):
                self._stack2.append(self._stack1.pop())
        return self._stack2.pop()

        

    def peek(self) -> int:
        if not self._stack2:
            for _ in range(len(self._stack1)):
                self._stack2.append(self._stack1.pop())
        return self._stack2[-1]
        

    def empty(self) -> bool:
        if not self._stack1 and not self._stack2:
            return True
        else:
            return False

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()