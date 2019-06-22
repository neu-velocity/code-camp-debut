class Solution:
    def search(self, nums: list, target: int) -> int:
        if nums == []:
            return -1
        
        left = 0
        right = len(nums) - 1

        while True:
            mid = (left + right) // 2
            if mid == left:
                # in this case, right == left + 1
                if target == nums[left]:
                    return left
                elif target == nums[right]:
                    return right
                else:
                    return -1
            
            else:
                # at least has three numbers in current iteration
                if nums[mid] >= nums[left]:
                    if target >= nums[left] and target <= nums[mid]:
                        # target is in the monotonic range, get into it in the next iter
                        right = mid
                    else:
                        # get out of monotonic range
                        left = mid + 1
                else:
                    if target >= nums[mid] and target <= nums[right]:
                        # again, target is in the monotonic range, get into it
                        left = mid
                    else:
                        # get out of monotonic range
                        right = mid - 1
