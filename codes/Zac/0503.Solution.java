class Solution {
    // monotonous stack
    // TC: O(N)
    // SC: O(N)
    public int[] nextGreaterElements(int[] nums) {
        if (nums == null || nums.length == 0) {
            return nums;
        }
        int[] ans = new int[nums.length];
        // when you need to find the first greater element: use monotonous decreasing stack
        Stack<Integer> stack = new Stack();
        for (int i = 2 * nums.length - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() <= nums[i % nums.length]) {
                stack.pop();
            }
            if (stack.isEmpty()) {
                ans[i % nums.length] = -1;
            } else {
                ans[i % nums.length] = stack.peek();
            }
            stack.push(nums[i % nums.length]);
        }
        return ans;
    }
}