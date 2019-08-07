class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = start + (end - start)//2
            
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[start]: #nums[start: mid + 1] is sorted
                if target >= nums[start] and target <= nums[mid - 1]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < nums[start]:#nums[mid: end + 1] is sorted
                if target >= nums[mid + 1] and target <= nums[end]:
                    print('here')
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                start += 1
        return False
                