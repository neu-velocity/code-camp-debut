class Solution {
    TreeNode first = null, second = null, pre= null;
    public void recoverTree(TreeNode root) {
        inorder(root);
        if(first!=null && second!=null) swap(first, second);
    }
    public void inorder(TreeNode root){
        if(root==null) return;
        inorder(root.left);
        if(pre==null) pre=root;
        else{
            if(pre.val>root.val){
                if(first==null) first = pre;
                second = root;
            }
            pre = root;
        }
        inorder(root.right);
    }
    
    public void swap(TreeNode first, TreeNode second){
        int tmp = first.val;
        first.val = second.val;
        second.val = tmp;
    }
}