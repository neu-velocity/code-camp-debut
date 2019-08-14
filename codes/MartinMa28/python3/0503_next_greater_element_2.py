class Solution:
    # brute-force
    # def nextGreaterElements(self, nums: list) -> list:
    #     doubled_nums = nums + nums[:-1]
    #     num_length = len(nums)
    #     next_greater = [-1] * num_length

    #     for idx, n in enumerate(nums):
    #         for cir_next in doubled_nums[idx: idx + num_length]:
    #             if cir_next > n:
    #                 next_greater[idx] = cir_next
    #                 break
        
    #     return next_greater
    def nextGreaterElements(self, nums: list) -> list:
        stack = [len(nums) - 1]
        next_greater = [-1] * len(nums)

        # traverse from the second last to the first (right to left)
        for i in range(len(nums) - 2, -1, -1):
            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                # pop all of in the stack elements that are less than current nums[i]
                stack.pop()
            
            if len(stack) > 0 and nums[i] < nums[stack[-1]]:
                # If there is still a value in the stack greater than nums[i],
                # that value is the next greater value, because we push from right to left.
                next_greater[i] = nums[stack[-1]]
            
            # Otherwise, we leave -1 to the place where i points to
            stack.append(i)
        
        # At this point, we have checked the next greater value from the right hand side.
        # Index 0 is at the top of the stack. And, the maximum value is at the bottom of the stack.
        # So, the next greater value from the left hand side of the circular traversal must 
        # reside in the stack.
        for i, value in enumerate(next_greater):
            if value == -1:
                for idx in reversed(stack):
                    if nums[idx] > nums[i]:
                        next_greater[i] = nums[idx]

        return next_greater
            
            




if __name__ == "__main__":
    solu = Solution()
    print(solu.nextGreaterElements([1, 2, 3, 4, 3]))

            