class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ret;
        if(nums.size() == 0)
            return ret;
        vector<int> cur;
        help(ret, nums,0, cur);
        return ret;
    }
    
    void help(vector<vector<int>>& ret, vector<int>& nums, int start, vector<int>& cur) {
        ret.push_back(cur);
        int i;
        while(start < nums.size()) {
            cur.push_back(nums[start]);
            help(ret, nums, start+1, cur);
            i = start+1;
            while(i < nums.size() && nums[i] == nums[i-1]) {
                i++;
            }
            start = i;
            cur.pop_back();
        }
    }
};