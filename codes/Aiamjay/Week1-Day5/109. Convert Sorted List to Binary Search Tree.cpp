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
        if (head == NULL)
            return NULL;
        int len = length(head);
        int* array = create_array(head, len);
        return buildTree(0, len - 1, array);
    }

    TreeNode* buildTree(int left, int right, int* array) {
        int mid = left + (right - left) / 2;
        auto tree = new TreeNode(array[mid]);

        if (mid - 1 == left)
            tree->left = new TreeNode(array[left]);
        if (mid - 1 > left)
            tree->left = buildTree(left, mid - 1, array);

        if (mid + 1 == right)
            tree->right = new TreeNode(array[right]);
        if (mid + 1 < right)
            tree->right = buildTree(mid + 1, right, array);
        return tree;
    }

    // find the moddle
    int length(ListNode* head) {
        int length = 0;
        while (head != NULL) {
            head = head->next;
            length++;
        }
        return length;
    }

    int* create_array(ListNode* head, int length) {
        auto result = new int[length];
        for (int i = 0; i < length; i++) {
            result[i] = head->val;
            head = head->next;
        }
        return result;
    }
};