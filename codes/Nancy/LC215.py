"""
SOLUTION1: sort the list,find the kth largest
time complexity would be O(nlogn)
"""

"""
SOLUTION2: Quickselect
reduces the expected complexity from O(n log n) to O(n), 
with a worst case of O(n^2)
"""
class Solution:    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums) - k
        pivot_index = self.partition(nums, 0 , len(nums) - 1)
        
        while pivot_index != n:
            if pivot_index < n:
                pivot_index = self.partition(nums, pivot_index + 1, len(nums) - 1)
            else:
                pivot_index = self.partition(nums, 0, pivot_index - 1)
        
        return nums[pivot_index]
    
    def partition(self, nums, start, end):
        slow = start - 1
        fast = start
        pivot_value = nums[end]
        
        while fast < end:
            if nums[fast] <= pivot_value:#move smaller value to the left
                slow += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]
            fast += 1
        
        slow += 1
        nums[slow], nums[end] = nums[end], nums[slow]
        
        return slow #return the index of pivot