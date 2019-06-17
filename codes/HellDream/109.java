class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if(head==null) return null;
        ListNode slow =head, fast =head, last=head;
        while(fast!=null&&fast.next!=null){
            last = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        TreeNode root = new TreeNode(slow.val);
        fast = slow.next;
        last.next = null;
        if(head!=slow){
            root.left = sortedListToBST(head);
            root.right = sortedListToBST(fast);
            
        }
        return root;
    }
}