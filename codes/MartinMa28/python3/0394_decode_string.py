class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        seg_stack = []
        seg = ''
        idx = 0

        while idx < len(s):
            if s[idx].isdigit():
                num = s[idx]
                while s[idx + 1].isdigit():
                    num += s[idx + 1]
                    idx += 1

                num_stack.append(int(num))
            elif s[idx] == '[':
                seg_stack.append(seg)
                seg = ''
            elif s[idx] == ']':
                repeated_str = num_stack.pop() * seg
                seg = seg_stack.pop() + repeated_str
            else:
                seg += s[idx]
            
            idx += 1
        
        return seg


if __name__ == "__main__":
    solu = Solution()
    print(solu.decodeString('3[a2[c]]'))