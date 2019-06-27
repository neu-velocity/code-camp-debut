class Solution {
public:
    int jump(vector<int>& nums) {
        int jump = 0, furthest = 0, curEnd = 0;
        for(int i = 0; i < nums.size()-1; i++) {
            furthest = max(furthest, nums[i] + i);
            if(i == curEnd) {
                jump++;
                curEnd = furthest;
            }
        }
        return jump;
    }
};