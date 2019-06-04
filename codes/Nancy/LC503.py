class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #using stack
        #record the element's index into a stack as you go to the right
        #if the next element is smaller than stack.top(), we only record its index 
        #if the next element is larget than stack.top(): 1. the next element is the next greater to stack.top()
        #2.we need to iterate through the stack because there might be previous elements recorded have this
        #larger element as the next greater.
        n = len(nums)
        stack = []
        res = [-1] * n
        
        for i in range(2*n):
            num  = nums[i % len(nums)]
            
            while len(stack) > 0 and nums[stack[-1]] < num:
                res[stack[-1]] = num
                stack.pop()
            
            if i < n:
                stack.append(i)
        
        return res
            
        