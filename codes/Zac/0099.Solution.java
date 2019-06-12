/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    // inorder traverse and sorting
    // TC: O(N + NlogN)
    // SC: O(N)
    public void recoverTree(TreeNode root) {
        List<Integer> values = new ArrayList();
        List<TreeNode> inorder = new ArrayList();
        Stack<TreeNode> stack = new Stack();
        TreeNode node = root;
        while (node != null || !stack.isEmpty()) {
            if (node != null) {
                stack.push(node);
                node = node.left;
            } else {
                node = stack.pop();
                inorder.add(node);
                values.add(node.val);
                node = node.right;
            }
        }
        Collections.sort(values);
        for (int i = 0; i < values.size(); i++) {
            inorder.get(i).val = values.get(i);
        }
    }
}