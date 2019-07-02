# encoding = utf-8
from collections import deque


class Solution:
    def combinationSum3(self, k: int, n: int):
        # return self.back_tracking_v1(k, n)
        result = []
        self.backtracking_v2(1, 0, n, k, [], result)
        return result

    def back_tracking_v1(self, length, target):
        # wjcnote iterative solution
        stack = deque()
        stack.append((1, 0, []))
        result = []
        while stack:
            cur_num, cur_sum, path = stack.pop()
            # wjcnote bounding condition
            if len(path) == length:
                if cur_sum == target:
                    result.append(path)
            else:
                if cur_num > 9:
                    continue
                if cur_sum + cur_num <= target and cur_num <= target:
                    stack.append((cur_num + 1,
                                  cur_sum + cur_num,
                                  path + [cur_num]))
                    stack.append((cur_num + 1,
                                  cur_sum,
                                  path))
        return result

    def backtracking_v2(self, num, sum, target, length, path: list, result: list):
        # wjcnote recursive solution
        if len(path) == length:
            if sum == target:
                result.append(path)
        else:
            if num < 10 and num <= target and num + sum <= target:
                self.backtracking_v2(num + 1, sum, target, length, path, result)
                self.backtracking_v2(num + 1, sum + num, target, length, path + [num], result)

    def test_sloution(self):
        # case 1
        print("case 1")
        k = 3
        n = 7
        for item in self.combinationSum3(k, n):
            print(item)

        # case 2
        print("case 2")
        k = 3
        n = 9
        for item in self.combinationSum3(k, n):
            print(item)


if __name__ == '__main__':
    s = Solution()
    s.test_sloution()
