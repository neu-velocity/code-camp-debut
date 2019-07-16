class Solution:
    def subsets(self, nums):
        nums = sorted(nums)
        result = list()
        self.worker(result, [], nums)
        return [list(item) for item in result]

    def worker(self, result, path, nums):
        result.append(path)
        last = None
        # wjcnote 重复部分的不需要递归
        for i in range(len(nums)):
            if last != nums[i]:
                self.worker(result, path + [nums[i]], nums[i + 1:])
            last = nums[i]

    def test_solution(self):
        nums = [1, 2, 2]
        result = self.subsets(nums)
        print(len(result))
        for item in sorted(result):
            print(item)
        assert sorted(result) == sorted([
            [2],
            [1],
            [1, 2, 2],
            [2, 2],
            [1, 2],
            []
        ])


if __name__ == '__main__':
    s = Solution()
    s.test_solution()
