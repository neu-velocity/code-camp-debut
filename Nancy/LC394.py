class Solution:
    def decodeString(self, s: str) -> str:
        currStr = ''
        currNum = 0
        stack = []
        
        for i in s:
            if i.isdigit():
                currNum = currNum*10 + int(i)
            elif i == '[': #indicating that we will expect a new currStr
                stack.append(currStr)
                stack.append(currNum)
                currStr = ''
                currNum = 0
            elif i == ']':
                num = stack.pop()
                prevStr = stack.pop()
                currStr = prevStr + num*currStr
            else: #meeting a letter
                currStr += i
        
        return currStr