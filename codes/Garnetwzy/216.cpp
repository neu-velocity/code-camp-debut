class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> ret;
        vector<int> cur;
        dfs(ret, cur, 0, k, n, 1);
        return ret;
    }
    
    void dfs(vector<vector<int>>& ret, vector<int>& cur, int sum, int k, int n, int index) {
        if(cur.size() > k)
            return;
        if(sum > n)
            return;
        if(cur.size() == k && sum == n) {
            ret.push_back(cur);
            return;
        }
        
        for(int i = index; i <= 9; i++) {
            cur.push_back(i);    
            dfs(ret, cur, sum + i, k, n, i+1);
            cur.pop_back();
        }
    }
};