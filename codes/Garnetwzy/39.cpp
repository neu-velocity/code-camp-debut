class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ret;
        sort(candidates.begin(), candidates.end());
        vector<int> cur;
        dfs(ret, cur, 0, target, candidates, 0);
        return ret;
    }
    
    void dfs(vector<vector<int>>& ret, vector<int>& cur, int sum, int target, vector<int>& candidates, int index) {
        if(sum == target) {
            ret.push_back(cur);
            return;
        }
        if(sum > target)
            return;
        
        for(int i = index; i < candidates.size(); i++) {
            cur.push_back(candidates[i]);
            dfs(ret, cur, sum + candidates[i], target, candidates, i);
            cur.pop_back();
        }
    }
};