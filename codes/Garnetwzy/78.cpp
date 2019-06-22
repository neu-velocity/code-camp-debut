class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ret;
        if(nums.size() == 0)
            return ret;
        vector<bool> visit(nums.size(), false);
        vector<int> cur = {};
        for(int i = 0; i <= nums.size(); i++) {
            dfs(ret, cur, nums, visit, i, 0);
        }
        return ret;
    }
    
    void dfs(vector<vector<int>>& ret, vector<int>& cur, vector<int>& nums, vector<bool>& visit, int len, int index) {
        if(cur.size() == len){
            ret.push_back(cur);
            return;
        }
        for(int i = index; i < nums.size(); i++) {
            if(visit[i])
                continue;
            visit[i] = true;
            cur.push_back(nums[i]);
            dfs(ret, cur, nums, visit, len, i+1);
            cur.pop_back();
            visit[i] = false;
        }
    }
};