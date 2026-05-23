class Solution {
public:
    int rob(vector<int>& nums) {
        vector<int> memo(nums.size(), -1);
        return dfs(nums, 0, memo);
    }

    int dfs(vector<int>& nums, int i, vector<int>& memo) {
        if (i >= nums.size()) {
            return 0;
        }
        if (memo[i] != -1) {
            return memo[i];
        }

        int skip = dfs(nums, i + 1, memo);
        int rob = nums[i] + dfs(nums, i + 2, memo);

        memo[i] = max(skip, rob);
        return memo[i];
    }
};
