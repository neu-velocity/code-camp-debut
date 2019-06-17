class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int s = 0, e = nums.size()-1;
        while(s <= e) {
            int mid = s + (e - s) / 2;
            if(nums[mid] == target)
                return true;
            if(nums[mid] > nums[e]) {
                if(nums[s] <= target && nums[mid] > target) {
                    e = mid - 1;
                }else {
                    s = mid + 1;
                }
            }else if(nums[mid] < nums[e]) {
                if(nums[mid] < target && nums[e] >= target) {
                    s = mid + 1;
                }else{
                    e = mid -1;
                }
            }else{
                e--;
            }
        }
        return false;
    }
};