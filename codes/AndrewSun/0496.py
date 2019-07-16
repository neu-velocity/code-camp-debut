class Solution:
    def nextGreaterElement(self, nums1, nums2):
        cache = {}
        stack = []
        ans = [-1] * len(nums1)
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                cache[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        for i in range(len(nums1)):
            if nums1[i] in cache:
                ans[i] = cache[nums1[i]]
        return ans

print(Solution().nextGreaterElement([4,1,2], [1,3,4,2]))