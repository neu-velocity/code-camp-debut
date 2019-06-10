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
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList();
        Stack<TreeNode> stack = new Stack();
        while (!stack.isEmpty() || root != null) {
            if (root != null) {
                res.add(root.val);
                stack.push(root);
                root = root.right;
            } else {
                root = stack.pop().left;
            }
        }
        Collections.reverse(res);
        return res;
    }
}