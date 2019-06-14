class Solution {
    // find left and right bounds
    // TC: O(N) - three passes
    // SC: O(N)
    public int trap(int[] height) {
        int[] leftBounds = new int[height.length];
        int[] rightBounds = new int[height.length];
        int max = 0;
        for (int i = 0; i < leftBounds.length; i++) {
            leftBounds[i] = max;
            max = Math.max(max, height[i]);
        }
        max = 0;
        for (int i = rightBounds.length - 1; i >= 0; i--) {
            rightBounds[i] = max;
            max = Math.max(max, height[i]);
        }
        int water = 0;
        for (int i = 0; i < height.length; i++) {
            int limit = Math.min(leftBounds[i], rightBounds[i]);
            water += Math.max(0, limit - height[i]);
        }
        return water;
    }

    // two pointers
    // TC: O(N)
    // SC: O(1)
    public int trap(int[] height) {
        int water = 0;
        int left = 0, right = height.length - 1;
        while (left + 1 < right) {
            if (height[left] <= height[right]) {
                int tmp = left + 1;
                while (tmp < right && height[tmp] <= height[left]) {
                    water += height[left] - height[tmp];
                    tmp++;
                }
                left = tmp;
            } else {
                int tmp = right - 1;
                while (tmp > left && height[tmp] <= height[right]) {
                    water += height[right] - height[tmp];
                    tmp--;
                }
                right = tmp;
            }
        }
        return water;
    }
}