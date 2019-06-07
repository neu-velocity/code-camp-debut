/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        return help(head, NULL);
    }
    
    TreeNode* help(ListNode* head, ListNode *tail) {
        if(head == tail)
            return NULL;
        ListNode *first = head;
        ListNode *second = head;
        while(second != tail && second->next != tail) {
            first = first->next;
            second = second->next->next;
        }
        TreeNode *root = new TreeNode(first->val);
        root->left = help(head, first);
        root->right = help(first->next, tail);
        return root;
    }
};