class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> ans = new ArrayList();
        dfs(k, n, 1, new ArrayList(), ans);
        return ans;
    }

    private void dfs(int k, int n, int digit, List<Integer> list, List<List<Integer>> ans) {
        if (n <= 0 || k <= 0 || digit > 9) {
            if (n == 0 && k == 0) {
                ans.add(new ArrayList(list));
            }
            return;
        }
        dfs(k, n, digit + 1, list, ans);
        list.add(digit);
        dfs(k - 1, n - digit, digit + 1, list, ans);
        list.remove(list.size() - 1);
    }
}