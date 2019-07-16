class Solution:
    def subsets(self, nums):
        result = list()
        self.worker(result, [], nums)
        return [list(item) for item in result]

    def worker(self, result, path, nums):
        result.append(path)
        for i in range(len(nums)):
            self.worker(result, path + [nums[i]], nums[i + 1:])

    def test_solution(self):
        nums = [1, 2, 3]
        result = self.subsets(nums)
        print(len(result))
        for item in sorted(result):
            print(item)


if __name__ == '__main__':
    s = Solution()
    s.test_solution()
