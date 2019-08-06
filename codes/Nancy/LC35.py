 class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
            
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        if nums[start] < target < nums[end]:
            return start + 1
        elif target < nums[start]:
            return 0
        else:
            return len(nums)
        
        return start + 1