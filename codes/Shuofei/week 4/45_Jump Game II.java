// O(n^2)/O(n), f[i + 1~nums[i]] = min{self, f[i] + 1}, initial f[0~n-1] = maxint
class Solution {
    public int jump(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, Integer.MAX_VALUE >> 2);
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 1; j <= Math.min(n - 1 - i, nums[i]); j++) {
                dp[i + j] = Math.min(dp[i + j], dp[i] + 1);
            }
        }
        return dp[n - 1];
    }
}

// O(n^2)/O(n), BFS

// O(n)/O(1), greedy
// https://leetcode.wang/leetCode-45-Jump-Game-II.html
class Solution {
    public int jump(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int max = 0, bound = 0, step = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            max = Math.max(i + nums[i], max);
            if (i == bound) {
                bound = max;
                step++;
            }          
        }
        return step;
    }
}