class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[r]:#right of mid is in order
                if nums[mid] < target and nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] >= nums[r]:#left of mid is in order
                if nums[l] <= target and nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1