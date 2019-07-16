/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

// Two Pointers, 1 ms (98.33%), 39.6 MB (99.95%)
// https://leetcode.com/problems/palindrome-linked-list/discuss/316814/Java-Solution-Using-Two-Pointers-Half-Reverse-or-O(1)-space
class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) {
            return true;
        }
        ListNode mid = findMid(head);
        ListNode left = head;
        ListNode right = reverse(mid.next);
        while (right != null) {
            if (left.val != right.val) {
                return false;
            } else {
                left = left.next;
                right = right.next;
            }
        }
        return true;
    }

    private ListNode reverse(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode prev = null;
        while (head != null) {
            ListNode nextTemp = head.next;
            head.next = prev;
            prev = head;
            head = nextTemp;
        }
        return prev;
    }

    private ListNode findMid(ListNode head) { // left-leaning
        if (head == null || head.next == null) {
            return head;
        }
        ListNode slow = head;
        ListNode fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}