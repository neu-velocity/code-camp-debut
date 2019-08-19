class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res = 0
        prev_end = 0
        curr_end = 0
        
        for i in range(len(nums) - 1):
            curr_end = max(curr_end, nums[i] + i)
            
            if i == prev_end:
                res += 1
                prev_end = curr_end
                if curr_end >= len(nums) - 1:
                    break
        return res
                