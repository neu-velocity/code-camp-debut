class Solution {
    public boolean isValidBST(TreeNode root) {
        ArrayList<Integer> list = new ArrayList<>();
        preOrder(list, root);
        for(int i=0;i<list.size()-1;i++){
            if(list.get(i)>=list.get(i+1)) return false;
        }
        return true;
    }
    public void preOrder(ArrayList<Integer> list,TreeNode root){
        if(root==null) return;
        if(root.left!=null) preOrder(list, root.left);
        list.add(root.val);
        if(root.right!=null) preOrder(list, root.right);
        
    }
}