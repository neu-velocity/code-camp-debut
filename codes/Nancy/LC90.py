class Solution:
    def backtracking(self, nums, res, temp, start):
        res.append(temp)
        
        for i in range(start, len(nums)):
            if i > start and nums[i -1] == nums[i]:
                continue
            self. backtracking(nums, res, temp + [nums[i]], i + 1)
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []
        self.backtracking(nums, res, temp, 0)
        
        return res