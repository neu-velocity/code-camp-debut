/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// dfs
class DFS_Solution {
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        if (root.left == null && root.right == null) {
            return 1;
        }
        int leftDepth = (root.left == null) ? Integer.MAX_VALUE : minDepth(root.left) + 1;
        int rightDepth = (root.right == null) ? Integer.MAX_VALUE : minDepth(root.right) + 1;
        return Math.min(leftDepth, rightDepth);
    }
}

// bfs
class BFS_Solution {
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Queue<TreeNode> queue = new LinkedList();
        queue.offer(root);
        int depth = 1;
        while (!queue.isEmpty()) {
            int s = queue.size();
            while (s-- > 0) {
                TreeNode node = queue.poll();
                if (node.left == null && node.right == null) {
                    return depth;
                }
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            depth++;
        }
        return depth;
    }
}