class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        used = [None]*len(nums)
        nums.sort()
        self.backtracking(nums,res, temp, used)
        return res
    def backtracking(self, nums, res, temp, used):
        if len(temp) == len(nums):
            res.append(temp)
            return
        else:
            for i in range(0, len(nums)):
                if used[i] == True or (i >= 1 and nums[i-1] == nums[i] and used[i-1] == False):
                    continue
                used[i] = True
                self.backtracking(nums, res, temp + [nums[i]], used)
                used[i] = False