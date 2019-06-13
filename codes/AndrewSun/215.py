class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partion(left, right):
            # choose a random pivot
            pivot = random.randint(left, right)
            # exchange the pivot and right-most element
            nums[pivot], nums[right] = nums[right], nums[pivot]
            # traverse each element in the list
            for ind, val in enumerate(nums[left: right+1], left):
                # if the value >= pivot, exchange it with the first element
                # that smaller than the pivot
                if (val >= nums[right]):
                    nums[ind], nums[left] = nums[left], nums[ind]
                    # left also represents the first element that smaller
                    # than the pivot
                    left += 1
            return left - 1 # the position of the pivot
                
        left, right = 0, len(nums) - 1
        k = k - 1 # index starts from 0
        
        while (1):
            pos = partion(left, right)
            # the Kth element is in the left part
            if (pos > k):
                right = pos - 1
            # the Kth is in the right part
            elif (pos < k):
                left = pos + 1
            # find the Kth element exactly
            else:
                return nums[pos]