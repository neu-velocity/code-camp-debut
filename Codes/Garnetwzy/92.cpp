/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode* dummy = new ListNode(1);
        dummy->next = head;
        ListNode *first = dummy;
        ListNode *tail = dummy;
        for(int i = 1; i < m; i++) {
            first = first->next;
        }
        for(int i = 1; i <= n; i++) {
            tail = tail->next;
        }
        while(first->next != tail) {
            ListNode *tmp = first->next;
            first->next = tmp->next;
            tmp->next = tail->next;
            tail->next = tmp;
        }
        return dummy->next;
    }
};