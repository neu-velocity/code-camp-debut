class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ret;
        vector<bool> visit(nums.size(), false);
        vector<int> cur = {};
        dfs(ret, cur, nums, visit);
        return ret;
    }
    
    void dfs(vector<vector<int>>& ret, vector<int>& cur, vector<int>& nums,  vector<bool> visit) {
        if(cur.size() == nums.size()) {
            ret.push_back(cur);
            return;
        }
        
        int i = 0;
        int j;
        while(i < nums.size()) {
            if(visit[i]) {
                i++;
                continue;
            }
            visit[i] = true;
            cur.push_back(nums[i]);
            dfs(ret, cur, nums, visit);
            visit[i] = false;
            cur.pop_back();
            j = i+1;
            while(j < nums.size() && nums[j] == nums[j-1]) {
                j++;
            }
            i = j;
        }
    }
};