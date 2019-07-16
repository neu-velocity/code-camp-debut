//dp, O(n^2)/O(n)
class Solution {
    public boolean canJump(int[] nums) {
        if (nums.length == 0) return false;
        boolean[] f = new boolean[nums.length];
        f[0] = true;
        for (int i = 0; i < nums.length; i++) {
            if (f[i]) {
                for (int j = 1; j <= nums[i]; j++) {
                    if ((i + j) >= nums.length)
                        break;
                    f[i + j] = true;
                }
            }
        }
        return f[nums.length - 1];
    }
}

//dp, O(n)/O(1)
class Solution {
    public boolean canJump(int[] nums) {
        if (nums.length == 0) return false;
        int max = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > max) 
                return false;
            max = Math.max(i + nums[i], max);
            if (max >= nums.length - 1)
                return true;            
        }
        return true;
    }
}