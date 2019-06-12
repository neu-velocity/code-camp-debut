class Solution {
    public ListNode sortList(ListNode head) {
        if(head==null||head.next==null) return head;
        ListNode slow = head, fast = head, pre = head;
        while(fast!=null &&fast.next!=null){
            pre = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        pre.next = null;
        return merge(sortList(head), sortList(slow));
    }
    
    public ListNode merge(ListNode l1, ListNode l2){
        ListNode head = new ListNode(0);
        ListNode p = head;
        while(l1!=null&&l2!=null){
            if(l1.val<l2.val){
                p.next = l1;
                l1 = l1.next;
            }else{
                p.next = l2;
                l2 = l2.next;
            }
            p = p.next;
        }
        if(l1!=null) p.next = l1;
        if(l2!=null) p.next = l2;
        return head.next;
    }
}