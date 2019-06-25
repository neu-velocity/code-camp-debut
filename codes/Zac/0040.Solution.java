class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList();
        Arrays.sort(candidates);
        dfs(candidates, 0, target, new ArrayList(), ans);
        return ans;
    }

    private void dfs(int[] candidates, int index, int target, List<Integer> cur, List<List<Integer>> ans) {
        if (target < 0) {
            return;
        }
        if (index == candidates.length) {
            if (target == 0) {
                ans.add(new ArrayList(cur));
            }
            return;
        }

        if (cur.isEmpty() || candidates[index] != cur.get(cur.size() - 1)) {
            dfs(candidates, index + 1, target, cur, ans);
        }
        cur.add(candidates[index]);
        dfs(candidates, index + 1, target - candidates[index], cur, ans);
        cur.remove(cur.size() - 1);
    }
}