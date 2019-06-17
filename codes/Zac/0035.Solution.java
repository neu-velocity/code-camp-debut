class Solution {
    public int searchInsert(int[] nums, int target) {
        if (target <= nums[0]) return 0;
        if (target > nums[nums.length - 1]) return nums.length;
        int left = 0, right = nums.length - 1;
        int mid = (left + right) / 2;
        while (mid > left) {
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                right = mid;
            } else if (nums[mid] < target) {
                left = mid;
            }
            mid = (left + right) / 2;
        }
        return left + 1;
    }
}