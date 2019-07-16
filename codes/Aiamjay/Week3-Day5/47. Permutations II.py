class Solution:
    def permuteUnique(self, nums):
        # wjcnote 首先排序
        nums = sorted(nums)
        result = []
        self.worker(nums, [], result)
        return result

    def worker(self, nums, path, result):
        if not nums:
            result.append(path)
        last = None
        for i in range(len(nums)):
            if last != nums[i]:
                self.worker(nums[:i] + nums[i + 1:], path + [nums[i]], result)
            last = nums[i]

    def quick_sort(self, nums):
        self.quick_partition(nums, 0, len(nums) - 1)

    def quick_partition(self, nums, b, e):
        if e <= b:
            return
        begin = b
        end = e
        pivot = nums[begin]
        while begin < end:
            while begin < end and nums[end] > pivot:
                end -= 1
            if begin < end:
                nums[begin] = nums[end]
                begin += 1
            while begin < end and nums[begin] <= pivot:
                begin += 1
            if begin < end:
                nums[end] = nums[begin]
                end -= 1
        nums[begin] = pivot
        self.quick_partition(nums, b, begin - 1)
        self.quick_partition(nums, begin + 1, e)

    def test_quick_sort(self):
        nums = [3, 2, 1, 6, 5, 8, 3, 2, 4]
        self.quick_sort(nums)
        print(nums)

    def test_solution(self):
        nums = [3, 3, 0, 3]
        result = self.permuteUnique(nums)
        print(len(result))
        for item in result:
            print(item)


if __name__ == '__main__':
    s = Solution()
    # s.test_quick_sort()
    s.test_solution()
