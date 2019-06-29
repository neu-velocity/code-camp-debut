// O(n^2)/O(n)
// dp[i] = max {dp[j] + 1, 0 <= j < i, nums[j]<nums[i]}

class Solution {
    public int lengthOfLIS(int[] nums) {
        if ((nums == null) || (nums.length == 0)) return 0;
        int[] dp = new int[nums.length];
        int max = 1;
        for (int i = 0; i < nums.length; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if ((nums[i] > nums[j]) && (dp[j] >= dp[i])) {
                    dp[i] = dp[j] + 1;                    
                }                
            }
            if (max <= dp[i]) max = dp[i];
        }
        return max;
    }
}

// O(nlogn)/O(n), binary search
// tails[i] : min num at i length; tails array is Monotonically Increasing 
// https://yzmduncan.iteye.com/blog/1546503 单调队列

    public int lengthOfLIS(int[] nums) {
        int[] tails = new int[nums.length];
        int size = 0;
        for (int x : nums) {
            int i = 0, j = size;
            while (i != j) {
                int m = (i + j) / 2;
                if (tails[m] < x)
                    i = m + 1;
                else
                    j = m;
            }
            tails[i] = x;
            if (i == size) ++size;
        }
        return size;
    }