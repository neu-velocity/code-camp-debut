class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        self.backtracking(nums, res, temp)
        return res
    
    def backtracking(self, nums, res, temp):
        if len(temp) == len(nums):
            res.append(temp)
            return
        
        else:
            for i in range(0, len(nums)):
                if nums[i] in temp:
                     continue
                self.backtracking(nums, res, temp+[nums[i]])