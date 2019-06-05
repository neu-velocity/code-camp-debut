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
    ListNode *detectCycle(ListNode *head) {
        if(head == NULL)
            return head;
        ListNode *first = head;
        ListNode *second = head;
        while(second->next && second->next->next) {
            first = first->next;
            second = second->next->next;
            if(first == second)
                break;
        }
        if(second->next == NULL || second->next->next == NULL)
            return NULL;
        first = head;
        while(first != second) {
            first = first->next;
            second = second->next;
        }
        return first;
    }
};