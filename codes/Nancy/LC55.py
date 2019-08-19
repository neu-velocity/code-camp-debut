class Solution:
    #SOLUTOIN 1:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        memo = [0 for i in range(len(nums) - 1)] #memo[i] represents how far you can jump from current position by also considering the culmulative jumps from previous steps
        prev = 1
        for i in range(len(nums) - 1):
            memo[i] = max(prev - 1, nums[i]) #how far you can jump at current pos = max(steps left from previous step, steps you have at current pos)
            if memo[i] <= 0:
                return False
            prev = memo[i]#update the previous step left for next round
        
        return True
    
    #SOLUTOIN 2:
    def canJump(self, nums: List[int]) -> bool:
        #greedy
        farthest_index = 0
        for i in range(len(nums)):
            if i > farthest_index or farthest_index >= len(nums) - 1:
                #farthest_index < i implies that previous culmulative steps can't reach current i
                break
            farthest_index = max(farthest_index, i + nums[i])
        
        return farthest_index >= len(nums) - 1
            