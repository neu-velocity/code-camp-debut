# encoding = utf-8


class Solution:
    # wjcnote 这个题目只是需要求出，有没有要求的分组，如果有，立即返回，不需要穷举所有分组
    def canPartition(self, nums):
        self.nums = sorted(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        return self.backtracking_v4(0, 0, [], total // 2, total)

    def backtracking_v4(self, index, total, path, target, left_total):
        if total == target:
            print(path)
            return True
        if index == len(self.nums):
            return False
        last = None
        left = left_total
        for i in range(index, len(self.nums)):
            cur_num = self.nums[i]
            left -= cur_num
            if last == cur_num:
                continue
            if total + cur_num > target:
                break
            print(cur_num, ' ', total + cur_num, " ", left)
            if self.backtracking_v4(i + 1, total + cur_num, path + [cur_num], target, left):
                return True
            last = cur_num
        return False

    def backtracking_v1(self, index, path, cur_total, left_total, result: list):
        if cur_total == left_total:
            result.append(path)
            return
        if index == len(self.nums) or cur_total > left_total:
            return
        for index in range(index, len(self.nums)):
            cur_num = self.nums[index]

    def backtracking_v2(self, index, path, cur_total, left_total, target, result: list):
        if index == len(self.nums):
            return
        total = left_total
        for index in range(index, len(self.nums)):
            cur_num = self.nums[index]
            total -= cur_num
            if self.bounding_condition(path + [cur_num], result, cur_num, cur_num + cur_total, total, target):
                self.backtracking_v2(index + 1, path + [cur_num], cur_total + cur_num, total, target, result)
        return

    def backtracking_v3(self, index, path, cur_total, left_total, target, result: list):
        if index == len(self.nums):
            return False
        total = left_total
        for index in range(index, len(self.nums)):
            cur_num = self.nums[index]
            total -= cur_num
            flag = self.bounding_condition_v3(path + [cur_num], result, cur_num, cur_num + cur_total, total, target)
            if flag == 1:
                return True
            elif flag == 3:
                if self.backtracking_v3(index + 1, path + [cur_num], cur_total + cur_num, total, target, result):
                    return True
        return False

    @staticmethod
    def bounding_condition_v3(path, result, cur_num, cur_total, left_total, target) -> int:
        if cur_total == target:
            result.append(path)
            return 1
        if cur_total > target or cur_total + left_total < target or target - cur_total < cur_num:
            return 2
        return 3

    @staticmethod
    def bounding_condition(path, result, cur_num, cur_total, left_total, target) -> bool:
        if cur_total == target:
            result.append(path)
            return False
        if cur_total > target or cur_total + left_total < target or target - cur_total < cur_num:
            return False
        return True

    def test_solution(self):
        nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
                100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
                100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
                100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
                100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        result = self.canPartition(nums)
        print(result)
        nums = [1, 2, 5]
        print(self.canPartition(nums))
        nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100]
        print(self.canPartition(nums))

    def test_solution_v4(self):
        nums = [1, 2, 5]
        print(self.canPartition(nums))
        nums = [1, 3, 5, 5, 5, 5]
        print(self.canPartition(nums))
        nums = [1, 2, 3, 4, 5, 6, 7]
        print(self.canPartition(nums))
        nums = [1, 5, 11, 5]
        print(self.canPartition(nums))
        nums = [1, 1, 1, 1, 1, 12, 13]
        print(len(nums))
        print(self.canPartition(nums))


if __name__ == '__main__':
    s = Solution()
    s.test_solution_v4()
    pass
