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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *newHead = new ListNode(0);
        ListNode *p1 = l1;
        ListNode *p2 = l2;
        ListNode *head = newHead;
        ListNode *tmp;
        while(p1 && p2) {
            if(p1->val < p2->val) {
                head->next = p1;
                tmp = p1->next;
                p1->next = NULL;
                p1 = tmp;
            } else {
                head->next = p2;
                tmp = p2->next;
                p2->next = NULL;
                p2 = tmp;
            }
            head = head->next;
        }
        if(p1) {
            head->next = p1;
        }
        if(p2) {
            head->next = p2;
        }
        return newHead->next;
    }
};