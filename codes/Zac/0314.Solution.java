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
    public List<List<Integer>> verticalOrder(TreeNode root) {
        Map<TreeNode, Integer> offsetMap = new HashMap();
        traverse(root, 0, offsetMap);

        Map<Integer, List<Integer>> columnMap = new TreeMap();
        Queue<TreeNode> queue = new LinkedList();
        if (root != null) {
            queue.offer(root);
        }
        while (!queue.isEmpty()) {
            int s = queue.size();
            while (s-- > 0) {
                TreeNode node = queue.poll();
                int offset = offsetMap.get(node);
                List<Integer> column = columnMap.getOrDefault(offset, new ArrayList());
                column.add(node.val);
                columnMap.put(offset, column);
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
        }
        return new ArrayList(columnMap.values());
    }

    private void traverse(TreeNode node, int offset, Map<TreeNode, Integer> offsetMap) {
        if (node == null) {
            return;
        }
        offsetMap.put(node, offset);
        traverse(node.left, offset - 1, offsetMap);
        traverse(node.right, offset + 1, offsetMap);
    }
}