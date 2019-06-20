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
    int minDepth(TreeNode* root) {
        if(root == NULL)
            return 0;
        queue<TreeNode *> q;
        q.push(root);
        int height = 1;
        while(!q.empty()) {
            int size = q.size();
            for(int i = 0; i < size; i++) {
                TreeNode *front = q.front();
                q.pop();
                if(front->left == NULL && front->right == NULL)
                    return height;
                if(front->left)
                    q.push(front->left);
                if(front->right)
                    q.push(front->right);
            }
            height++;
        }
        return -1;
            
    }
    
    int getMinHeight(TreeNode* root) {
        if(root == NULL)
            return 0;
        if(root->left == NULL && root->right == NULL) {
            return 1;
        }
        int left = getMinHeight(root->left) + 1;
        int right = getMinHeight(root->right) + 1;
        return min(left, right);
    }
};