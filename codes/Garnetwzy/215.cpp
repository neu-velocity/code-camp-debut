class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        return nums[findIndex(nums, k, 0, nums.size()-1)];
    }
    
    int findIndex(vector<int>& nums, int k, int left, int right) {
        int index = partision(nums, left, right);
        if(index == k-1)
            return index;
        if(index < k-1)
            return findIndex(nums, k, index+1, right);
        return findIndex(nums, k, left, index-1);
    }
    
    int partision(vector<int>& nums, int s, int e) {
        int target = nums[s];
        int i = s, j = e;
        while(i < j) {
            while(nums[j] <= target && j > i) {
                j--;
            }
            if(nums[j] > target) {
                nums[i] = nums[j];
            }
            while(nums[i] >= target && j > i) {
                i++;
            }
            if(nums[i] < target) {
                nums[j] = nums[i];
            }
        }
        nums[i] = target;
        return i;
    }
};