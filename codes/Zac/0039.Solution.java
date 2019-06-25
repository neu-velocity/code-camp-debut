class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList();
        dfs(candidates, 0, target, new ArrayList(), ans);
        return ans;
    }

    private void dfs(int[] candidates, int index, int target, List<Integer> cur, List<List<Integer>> ans) {
        if (target <= 0 || index == candidates.length) {
            if (target == 0) {
                ans.add(new ArrayList(cur));
            }
            return;
        }
        for (int i = 0; i * candidates[index] <= target; i++) {
            for (int j = 0; j < i; j++) {
                cur.add(candidates[index]);
            }
            dfs(candidates, index + 1, target - i * candidates[index], cur, ans);
            for (int j = 0; j < i; j++) {
                cur.remove(cur.size() - 1);
            }
        }
    }
}