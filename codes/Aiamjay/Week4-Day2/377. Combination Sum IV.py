# encoding = utf-8


class Solution:
    # wjcnote 这个题目使用backtracking 时间复杂度太高了，特别是当target非常大的时候
    def __init__(self):
        self.nums = None
        self.target = None

    def combinationSum4_failed(self, nums, target: int):
        nums = sorted([num for num in nums if num <= target])
        self.target = target
        self.nums = nums
        result = []
        self.backtracking_v3(nums, 0, [], result)
        return result

    def combinationSum4(self, nums, target: int):
        return self.memory_search(target, nums)

    def backtracking_v1(self, index, sum, path: list, result: list):
        # wjcnote iterative
        if sum == self.target:
            result.append(path)
        if index < len(self.nums) and sum < self.target and sum + self.nums[index] <= self.target:
            for i in range(self.target // self.nums[index] + 1):
                self.backtracking_v1(index + 1,
                                     sum + self.nums[index] * i,
                                     path + [self.nums[index]] * i,
                                     result)

    def backtracking_v2(self, nums: list, sum, path: list, result: list):
        # wjcnote iterative
        print(nums, " ", path)
        if sum == self.target:
            result.append(path)
            return
        if sum > self.target:
            return
        for index in range(len(nums)):
            cur_num = nums[index]
            # 一个也不能用，由于是拍了序的，后面的也不能再用了
            if cur_num > self.target - sum:
                break
            # 用这个， question 还能不能再用这个？
            if cur_num * 2 <= self.target - sum:
                self.backtracking_v2(nums, sum + cur_num, path + [cur_num], result)
            else:
                self.backtracking_v2(nums[:index], sum + cur_num, path + [cur_num], result)
            # 不用这个
            self.backtracking_v2(nums[:index] + nums[index + 1:], sum, path, result)

    def backtracking_v3(self, nums: list, sum, path: list, result: list):
        # wjcnote iterative
        if sum == self.target:
            result.append(path)
            return
        if sum > self.target:
            return
        for index in range(len(nums)):
            cur_num = nums[index]
            if cur_num > self.target - sum:
                break
            if cur_num <= self.target - sum - cur_num:
                self.backtracking_v3(nums, sum + cur_num, path + [cur_num], result)
            else:
                self.backtracking_v3(nums[:index], sum + cur_num, path + [cur_num], result)

    def memory_search(self, target, nums: list):
        memos = [1] + [0] * target
        for index in range(len(memos)):
            for num in nums:
                if index < num:
                    break
                # wjcnote 使用之前的记录，来计算当前的
                memos[index] += memos[index - num]
        return memos[target]

    def test_solution(self):
        # nums = [1, 2, 3]
        # target = 4
        # for item in self.combinationSum4(nums, target):
        #     print(item)

        # case 2
        # nums = [3, 1, 2, 4]
        # target = 4
        # for item in self.combinationSum4(nums, target):
        #     print(item)

        # case 3
        print("case 3")
        nums = [4, 2, 1]
        target = 32
        result = self.combinationSum4(nums, target)
        print(result)



if __name__ == '__main__':
    s = Solution()
    s.test_solution()
