class Solution:
    def isValid(self, s: str) -> bool:        
        if not s:
            return True
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    tmp = stack.pop()
                    if not self.checkPair(tmp, i):
                        return False
        if stack:
            return False
        else:
            return True
            
    def checkPair(self, l, r):
            tmp = l + r
            if tmp == '()' or tmp == '[]' or tmp == '{}' :
                return True
            else:
                return False