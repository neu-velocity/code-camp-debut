class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists==null||lists.length==0) return null;
        for(int i=1;i<lists.length;i++){
            lists[i] = merge(lists[i-1], lists[i]);
        }
        return lists[0];
    }
    
    public ListNode merge(ListNode l1, ListNode l2) {
        ListNode listNode = new ListNode(-1);
        ListNode p = listNode;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                p.next = l1;
                l1 = l1.next;
                p = p.next;
            } else {
                p.next = l2;
                l2 = l2.next;
                p = p.next;
            }
        }
        if (l1 != null) {
            p.next = l1;
        }
        if (l2 != null) {
            p.next = l2;
        }
        return listNode.next;
    }
}