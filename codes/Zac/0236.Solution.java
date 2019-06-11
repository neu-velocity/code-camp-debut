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
    // HashMap
    // TC: O(N)
    // SC: O(N)
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == p || root == q) {
            return root;
        }
        if (p == q) {
            return p;
        }
        Map<TreeNode, TreeNode> parents = new HashMap();
        Queue<TreeNode> queue = new LinkedList();
        queue.offer(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node.left != null) {
                queue.offer(node.left);
                parents.put(node.left, node);
            }
            if (node.right != null) {
                queue.offer(node.right);
                parents.put(node.right, node);
            }
            if (parents.containsKey(p) && parents.containsKey(q)) {
                break;
            }
        }
        Set<TreeNode> seen = new HashSet();
        seen.add(p);
        while (parents.containsKey(p)) {
            p = parents.get(p);
            seen.add(p);
        }
        while (!seen.contains(q)) {
            q = parents.get(q);
        }
        return q;
    }

    // Recursive
    // TC: O(N) - every node will be visited once
    // SC: O(N) - an implicit stack used
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) {
            return root;
        }
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left != null && right != null) {
            return root;
        } else if (left != null) {
            return left;
        } else if (right != null) {
            return right;
        } else {
            return null;
        }
    }
}