class Solution:
    def search(self, nums: list, target: int) -> bool:
        if nums == []:
            return False
            
        # remove duplicated numbers
        nums = list(set(nums))
        left = 0
        right = len(nums) - 1

        while True:
            mid = (left + right) // 2
            if mid == left:
                # right is right next to left
                if target == nums[left] or target == nums[right]:
                    return True
                else:
                    return False

            else:
                # has more than two numbers in this iteration
                if nums[mid] >= nums[left]:
                    if target >= nums[left] and target <= nums[mid]:
                        right = mid
                    else:
                        left = mid + 1
                else:
                    if target >= nums[mid] and target <= nums[right]:
                        left = mid
                    else:
                        right = mid - 1