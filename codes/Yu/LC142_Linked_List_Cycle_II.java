/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

// Hash Table, 6 ms, 35.3 MB
public class Solution {
    public ListNode detectCycle(ListNode head) {
        Set<ListNode> nodeSeen = new HashSet<>();
        while (head != null) {
            if (nodeSeen.contains(head)) {
                return head;
            }
            nodeSeen.add(head);
            head = head.next;
        }
        return null;
    }
}

// Two Pointers, 0 ms, 36.2 MB
// https://leetcode.com/problems/linked-list-cycle-ii/discuss/308124/O(n)-time-O(1)-space-solution
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) { // cycle detected
                while (head != slow) {
                    head = head.next;
                    slow = slow.next;
                }
                return head;
            }
        }
        return null;
    }
}