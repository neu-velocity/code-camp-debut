class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList();
        subsetHelper(nums, new ArrayList(), 0, ans);
        return ans;
    }

    private void subsetHelper(int[] nums, List<Integer> cur, int index, List<List<Integer>> ans) {
        if (index == nums.length) {
            ans.add(new ArrayList(cur));
        } else {
            subsetHelper(nums, cur, index + 1, ans);
            cur.add(nums[index]);
            subsetHelper(nums, cur, index + 1, ans);
            cur.remove(cur.size() - 1);
        }
    }
}
