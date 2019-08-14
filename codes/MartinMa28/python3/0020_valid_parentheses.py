class Solution:
    def __init__(self):
        self.stack = []
        self.opens = ('(', '[', '{')
        self.closes = (')', ']', '}')
        self.open_to_close = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

    def isValid(self, s: str) -> bool:
        for ch in s:
            if ch in self.opens:
                self.stack.append(ch)
            elif len(self.stack) == 0:
                return False
            elif self.open_to_close[self.stack[-1]] == ch:
                self.stack.pop()
            else:
                return False

        if len(self.stack) != 0:
            return False
        else:
            return True

