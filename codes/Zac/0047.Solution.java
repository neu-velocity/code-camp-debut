class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> ans = new ArrayList();
        Arrays.sort(nums);
        permuteHelper(nums, new int[nums.length], 0, new boolean[nums.length], ans);
        return ans;
    }

    private void permuteHelper(int[] nums, int[] cur, int index, boolean[] used, List<List<Integer>> ans) {
        if (index >= nums.length) {
            List<Integer> permutation = new ArrayList();
            for (int n : cur) {
                permutation.add(n);
            }
            ans.add(permutation);
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i] || (i > 0 && nums[i] == nums[i - 1] && used[i - 1])) {
                continue;
            }
            used[i] = true;
            cur[index] = nums[i];
            permuteHelper(nums, cur, index + 1, used, ans);
            used[i] = false;
        }
    }
}