class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        for ind, n in enumerate(nums):
            if n >= target:
                return ind
        
        return len(nums)

        