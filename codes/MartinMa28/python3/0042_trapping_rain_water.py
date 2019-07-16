class Solution:
    # brute force solution
    def trap_brute_force(self, height: list) -> int:
        water = 0
        for ind, h in enumerate(height, 0):
            max_left = max(height[:ind + 1])
            max_right = max(height[ind:])
            water += min((max_left, max_right)) - h

        return water


    # dynamic programming
    def trap(self, height: list) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        temp = 0
        for ind, h in enumerate(height):
            if h > temp:
                temp = h
            max_left[ind] = temp

        temp = 0
        for ind in range(len(height)):
            if height[len(height) - 1 - ind] > temp:
                temp = height[len(height) - 1 - ind]
            max_right[len(height) - 1 - ind] = temp

        return sum(map(lambda x: min((x[0], x[1])) - x[2], zip(max_left, max_right, height)))
 

if __name__ == "__main__":
    solu = Solution()
    t = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(solu.trap(t))