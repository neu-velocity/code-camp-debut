class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        if(root==null) return list;
        Stack<TreeNode> stack = new Stack<>();
        TreeNode head = root;
        stack.push(root);
        while(!stack.isEmpty()){
            TreeNode node = stack.peek();
            if((node.left==null && node.right==null) ||node.left==head||node.right==head){
                list.add(node.val);
                stack.pop();
                head = node;
            }else{
                if(node.right!=null) stack.push(node.right);
                if(node.left!=null) stack.push(node.left);
            }
        }
        return list;
    }
}
     