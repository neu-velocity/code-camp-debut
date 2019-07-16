class Solution:
    def nextGreaterElements(self, nums):
        # auxiliary stack: store the index of the elements which have not found the Next Greater Element 
        stack = []
        # Initialize as -1s
        ans = [-1] * len(nums)
        # the first loop
        for i in range(len(nums)):
            # Since the loop is in traverse-order, nums[i] must be the first greater element of stack[-1] 
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
            # nums[i] haven't found the Next Greater Element; add its index 'i' to stack as well 
            stack.append(i)
        # the second loop
        # In loop 2, we only need to deal with the existed element in the stack (since all the indices have been added once in loop 1)
        # Thus, we don't need to 'stack.append(i)'
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
        return ans