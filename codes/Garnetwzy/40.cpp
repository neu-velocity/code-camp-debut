class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> ret;
        sort(candidates.begin(), candidates.end());
        vector<int> cur;
        dfs(ret, candidates, cur, 0, 0, target);
        return ret;
    }
    
    void dfs(vector<vector<int>>& ret, vector<int>& candidates, vector<int>& cur, int index, int sum, int target) {
        if(sum == target) {
            ret.push_back(cur);
        }
        if(sum > target)
            return;        
        for(int i = index; i < candidates.size(); i++) {
            if(i > index && candidates[i-1] == candidates[i])
                continue;
            cur.push_back(candidates[i]);
            dfs(ret, candidates, cur, i+1, sum + candidates[i], target);
            cur.pop_back();
        }
    }
};