/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

// 0 ms (100.00%), 34.2 MB (100.00%)
// https://leetcode.com/problems/reverse-linked-list-ii/discuss/300120/JAVA%3A-Simple-and-Concise-solution-with-detailed-explanation
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        ListNode start = head;

        for (int i = 0; i < m - 1; i++) {
            prev = prev.next;
            start = start.next;
        }

        // 1->2->3->4->5->6->7 | 1->2->4->3->5->6->7 | 1->2->5->4->3->6->7 |
        // 1->2->6->5->4->3->7 | 1->2->7->6->5->4->3
        for (int i = 0; i < n - m; i++) {
            ListNode curr = start.next;
            if (curr.next == null) {
                start.next = null;
            } else {
                start.next = curr.next;
            }
            curr.next = prev.next;
            prev.next = curr;
        }
        return dummy.next; // return head; is wrong when m = 1
    }
}