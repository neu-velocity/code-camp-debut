class Solution {
    public boolean search(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return false;
        }
        int lo = 0, hi = nums.length - 1;
        if (nums[lo] == target || nums[hi] == target) {
            return true;
        }
        while (lo + 1 < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == nums[lo] || nums[mid] == nums[hi]) {
                if (nums[mid] == nums[lo]) {
                    lo++;
                }
                if (nums[mid] == nums[hi]) {
                    hi--;
                }
                continue;
            }
            if (nums[mid] > target) {
                if (nums[mid] > nums[lo] && target < nums[lo]) {
                    lo = mid;
                } else {
                    hi = mid;
                }
            } else if (nums[mid] < target) {
                if (nums[mid] < nums[lo] && target > nums[lo]) {
                    hi = mid;
                } else {
                    lo = mid;
                }
            } else {
                return true;
            }
        }
        return nums[lo] == target || nums[hi] == target;
    }
}