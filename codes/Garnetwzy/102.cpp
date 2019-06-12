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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ret;
        dfs(ret, 0, root);
        return ret;
    }
    
    void dfs(vector<vector<int>>& ret, int height, TreeNode *root) {
        if(root == NULL)
            return;
        if(height == ret.size()) {
            ret.push_back(vector<int>());
        }
        ret[height].push_back(root->val);
        dfs(ret, height+1, root->left);
        dfs(ret, height+1, root->right);
    }
};