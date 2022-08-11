/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


bool isValidBST(struct TreeNode* root){
        
    bool dfs(struct TreeNode* tree, int left, int right, bool l_flag, bool r_flag) {
        if(!tree) {
            return true;
        }
        
        if (!((tree->val > left || l_flag) && (tree->val < right || r_flag))) {
            return false;
        }
        
        return dfs(tree->left, left, tree->val, l_flag, false) && dfs(tree->right, tree->val, right, false, r_flag);
    }
    
    return dfs(root, 0, 0, true, true);

}