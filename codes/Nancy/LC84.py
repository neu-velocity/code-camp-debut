class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #kinda brute force?
        #the key here is to find the local max, and then iterate through its previous heights
        res = 0
        for i in range(len(heights)):
            if i + 1 < len(heights) and heights[i+1] >= heights[i]:
                continue
            
            height = heights[i]
            j = i
            while j >= 0:
                height = min(height, heights[j])
                area = height * (i - j + 1)
                res = max(res, area)
                j -= 1
        
        return res