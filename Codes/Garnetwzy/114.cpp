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
    void flatten(TreeNode* root) {
        help(root);
    }
    
    TreeNode* help(TreeNode* root) {
        if(root == NULL)
            return NULL;
        if(root && root->left == NULL && root->right == NULL)
            return root;
        TreeNode *cLeft = help(root->left);
        TreeNode *cRight = help(root->right);
        if(cLeft) {
            root->left = NULL;
            root->right = cLeft;
            while(cLeft->right) {
                cLeft = cLeft->right;
            }
            cLeft->right = cRight;
        }
        return root;
    }
};