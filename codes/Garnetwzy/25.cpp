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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(k == 1)
            return head;
        ListNode *dummy = new ListNode(0);
        dummy->next = head;
        ListNode *pre = dummy;
        ListNode *tail = dummy;
        while(tail) {
            ListNode *tmp = pre->next;
            for(int i = 1; i <= k && tail; i++) {
                tail = tail->next;
            }
            if(!tail)
                break;
            reverse(pre, tail);
            pre = tmp;
            tail = tmp;
        }
        return dummy->next;
    }
    
    void reverse(ListNode *pre, ListNode *tail) {
        while(pre->next != tail) {
            ListNode *tmp = pre->next;
            pre->next = tmp->next;
            tmp->next = tail->next;
            tail->next = tmp;
        }
    }
};