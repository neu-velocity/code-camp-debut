/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode slow = head, fast = head;
        while(fast!=null &&fast.next!=null){
            slow = slow.next;
            fast = fast.next.next;
        }
        if(fast!=null){
            slow.next = reverseList(slow.next);
            slow = slow.next;
        }else{
            slow = reverseList(slow);
        }
        fast = head;
        while(slow!=null){
            if(fast.val!=slow.val) return false;
            slow = slow.next;
            fast = fast.next;
        }
        
        return true;
    }
    
    public ListNode reverseList(ListNode head){
        ListNode prev = null;
        ListNode curr = head;
        
        while(curr!=null){
            ListNode tmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tmp;
        }
        return prev;
    }
}