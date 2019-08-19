class Solution:
#SOLUTION1: Memoization
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = dict()
        def backtracking(remain):
            if remain in memo:
                return memo[remain]
            if remain < 0:
                return 0
            if remain == 0:
                return 1
            res = 0
            for i in range(0, len(nums)):
                res += backtracking(remain - nums[i])
            
            memo[remain] = res #there are res many combinations when remain == remain
            return res
        
        return backtracking(target)

#SOLUTION 2: Bottom-up
    def combinationSum4(self, nums: List[int], target: int) -> int:
        target_result = [0]*(target+1) #index represents each specific target value
        target_result[0] = 1
        for target_num in range(1, target+1):
            for x in nums:
                #current + remain = target, if we have n different combos of remain
                #then we have total # of resutls = current #of combos that adds up to target + this n different combos 
                #to get to the current target
                remain = target_num - x
                if remain >= 0:
                    target_result[target_num] += target_result[remain]
        return target_result[target]
                    