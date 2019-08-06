class Solution:
    def largestRectangleArea(self, heights) -> int:
        # left[i], right[i] represent how many bars are >= than the current bar (including the current bar)
        left = [1] * len(heights)
        right = [1] * len(heights)
        largestArea = 0
        # left 
        for i in range(0, len(heights)):
            j  = i - 1 #  start from the first left element
            while (j >= 0):
                if heights[j] >= heights[i]: # the bar is higher than the current one
                    left[i] += left[j]  # update the left[]
                    j -= left[j] # jump to the next bar non-linearly
                else: 
                    break
        # right
        for i in range(len(heights)-1, -1, -1):
            j = i + 1 #  start from the first right element
            while (j < len(heights)):
                if heights[j] >= heights[i]:
                    right[i] += right[j]
                    j += right[j]
                else:
                    break
        # Find the largest area with regard to the bars
        for i in range(len(heights)):
            largestArea = max(largestArea, heights[i] * (left[i] + right[i] - 1))

        return largestArea

print(Solution().largestRectangleArea([3,6,5,7,4,8,1,0]))