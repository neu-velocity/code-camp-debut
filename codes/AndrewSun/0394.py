class Solution:
    def decodeString(self, s: str) -> str:
        stack = [['', 1]] #[str, k]
        num = ''
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(['', int(num)])
                num = ''
            elif ch == ']':
                tmpStr, tmpK = stack.pop()
                stack[-1][0] += tmpK * tmpStr
            else:
                stack[-1][0] += ch
        return stack[0][0]
s = Solution()
print(s.decodeString("3[a2[c]]"))