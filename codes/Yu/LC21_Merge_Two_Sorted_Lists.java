/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
	public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
		ListNode l = new ListNode(0);
		ListNode head = l;

		while (l1 != null || l2 != null) {
			if (l1 == null) {
				l.next = new ListNode(l2.val);
				l2 = l2.next;
			} else if (l2 == null) {
				l.next = new ListNode(l1.val);
				l1 = l1.next;
			} else {
				if (l1.val <= l2.val) {
					l.next = new ListNode(l1.val);
					l1 = l1.next;
				} else {
					l.next = new ListNode(l2.val);
					l2 = l2.next;
				}
			}
			l = l.next;
		}

		return head.next;
	}
}

// fast and cleaner solution
class Solution {
	public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
		ListNode l = new ListNode(0);
		ListNode head = l;

		while (l1 != null && l2 != null) {
			ListNode nextNode = l1.val < l2.val ? l1 : l2;
			l.next = nextNode;
			l = l.next;
			// l.next = null; cannot be here because l is l1 or l2 now

			if (nextNode == l1)
				l1 = l1.next;
			else
				l2 = l2.next;
			l.next = null;
		}

		if (l1 != null)
			l.next = l1;
		else
			l.next = l2;

		return head.next;
	}
}