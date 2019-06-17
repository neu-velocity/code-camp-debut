    1 	class Solution {
    2 	    public void flatten(TreeNode root) {
    3 	        if(root==null) return;
    4 	        if(root.left!=null) flatten(root.left);
    5 	        if(root.right!=null) flatten(root.right);
    6 	        TreeNode right = root.right;
    7 	        root.right = root.left;
    8 	        root.left = null;
    9 	        while(root.right!=null) root = root.right;
   10 	        root.right = right;
   11 	    }
   12 	}
