/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

// Hash Table, 7 ms (21.62%), 39.3 MB (26.75%)
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set<ListNode> setA = new HashSet<>();
        while (headA != null) {
            setA.add(headA);
            headA = headA.next;
        }
        while (headB != null) {
            if (setA.contains(headB)) {
                return headB;
            } else {
                headB = headB.next;
            }
        }
        return null;
    }
}

// Two Pointers, 1 ms (97.44%), 38.7 MB (47.92%)
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }
        ListNode currA = headA;
        ListNode currB = headB;
        while (currA != currB) {
            if (currA == null) {
                currA = headB;
            } else if (currB == null) {
                currB = headA;
            } else {
                currA = currA.next;
                currB = currB.next;
            }
        }
        return currA;
    }
}