class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root==null) return root;
        if(root.val>Math.max(p.val, q.val)) 
            return lowestCommonAncestor(root.left, p, q);
        else if(root.val<Math.min(p.val, q.val)) 
            return  lowestCommonAncestor(root.right, p, q);
        else return root;
    }
}