class Solution:
    def backtracking(self, nums, res, temp, start):
        if start == len(nums):
            res.append(temp)
            return
        
        self. backtracking(nums, res, temp + [nums[start]], start + 1)
        self.backtracking(nums, res, temp, start + 1)
    def subsets(self, nums: List[int]) -> List[List[int]]:

        
        res = []
        temp = []
        self.backtracking(nums, res, temp, 0)
        return res