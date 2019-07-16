class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> ans = new ArrayList();
        Arrays.sort(nums);
        subsetHelper(nums, new ArrayList(), 0, ans);
        return ans;
    }

    private void subsetHelper(int[] nums, List<Integer> cur, int index, List<List<Integer>> ans) {
        if (index == nums.length) {
            ans.add(new ArrayList(cur));
        } else {
            if (cur.isEmpty() || nums[index] != nums[index - 1] || nums[index] != cur.get(cur.size() - 1)) {
                subsetHelper(nums, cur, index + 1, ans);
            }
            cur.add(nums[index]);
            subsetHelper(nums, cur, index + 1, ans);
            cur.remove(cur.size() - 1);
        }
    }
}