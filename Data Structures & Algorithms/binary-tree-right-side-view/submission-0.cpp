/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        // The nodes visible in the right-side view are the last nodes at each
        // level of the tree.

        // For each level, push the last node added to the queue's value to the result
        // list to get right-side view
        queue<TreeNode*> queue;

        if (root) {
            queue.push(root);
        }

        vector<int> res;
        while (queue.size() > 0) {
            TreeNode* rsv = queue.back();
            res.push_back(rsv->val);

            int length = queue.size();
            for (int i = 0; i < length; i++) {
                TreeNode* curr = queue.front();
                queue.pop();

                if (curr->left) queue.push(curr->left);
                if (curr->right) queue.push(curr->right);
            }
        }
        return res;
    }
};
