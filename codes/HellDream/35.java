class Solution {
    public int searchInsert(int[] nums, int target) {
        if(nums.length==0) return 0;
        int low = 0, high = nums.length-1;
        while(low<=high){
            int mid = (low+high)/2;
            if(nums[mid]==target) return mid;
            if(nums[mid]>target) high = mid-1;
            else low = mid+1;
        }
        if(low<nums.length&&target<=nums[low]) return low;
        return high+1;
    }
}