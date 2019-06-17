class Solution {
    public int search(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        int lo = 0, hi = nums.length - 1;
        while (lo + 1 < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] > target) {
                if (nums[mid] > nums[lo] && target < nums[lo]) {
                    lo = mid;
                } else {
                    hi = mid;
                }
            } else if (nums[mid] < target) {
                if (nums[mid] < nums[hi] && target > nums[hi]) {
                    hi = mid;
                } else {
                    lo = mid;
                }
            } else {
                return mid;
            }
        }
        if (nums[lo] == target) {
            return lo;
        } else if (nums[hi] == target) {
            return hi;
        } else {
            return -1;
        }
    }
}