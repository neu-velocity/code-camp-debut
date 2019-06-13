/*
 * @lc app=leetcode id=236 lang=cpp
 *
 * [236] Lowest Common Ancestor of a Binary Tree
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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        return help(root, p, q);
    }

    TreeNode* help(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == NULL)
            return root;
        TreeNode *left = help(root->left, p, q);
        TreeNode *right = help(root->right, p, q);
        if(left == NULL && right == NULL) {
            if(root == p || root == q)
                return root;
            return NULL;
        }else if(left != NULL && right != NULL) {
            return root;
        }else {
            if(root == p || root == q) {
                return root;
            } else {
                return left == NULL ? right : left;
            }
        }
    }
};