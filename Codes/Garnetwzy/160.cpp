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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *p1 = headA;
        ListNode *p2 = headB;
        int len1 = 0;
        int len2 = 0;
        while(p1) {
            len1++;
            p1 = p1->next;
        }
        while(p2) {
            len2++;
            p2 = p2->next;
        }
        p1 = headA;
        p2 = headB;
        int diff = abs(len1 - len2);
        if(len1 < len2) {
            while(diff > 0) {
                p2 = p2->next;
                diff--;
            }
        }else if(len1 > len2) {
            while(diff > 0) {
                p1 = p1->next;
                diff--;
            }
        }
        while(p1 != p2) {
            p1 = p1->next;
            p2 = p2->next;
        }
        return p1;
    }
};