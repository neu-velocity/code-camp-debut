class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ret;
        vector<bool> visit(nums.size(), false);
        vector<int> cur = {};
        dfs(ret, visit, cur, nums);
        return ret;
    }
    
    void dfs(vector<vector<int>>& ret, vector<bool>& visit, vector<int>& cur, vector<int>& nums) {
        if(cur.size() == nums.size()) {
            ret.push_back(cur);
            return;
        }
            
        for(int i = 0; i < nums.size(); i++) {
            if(visit[i])
                continue;
            cur.push_back(nums[i]);
            visit[i] = true;
            dfs(ret, visit, cur, nums);
            visit[i] = false;
            cur.pop_back();
        }
    }
};