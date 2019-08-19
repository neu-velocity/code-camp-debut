class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #O(n^2) DP
        res = 0
        memo = [1 for i in range(len(nums))] #memo[i] indicates the length longest increasing subsequence from begining to nums[i]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    memo[i] = max(memo[i], memo[j] + 1)
                
            res = max(res, memo[i])
        
        return res