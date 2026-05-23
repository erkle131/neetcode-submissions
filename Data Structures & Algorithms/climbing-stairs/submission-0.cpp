class Solution {
public:
    // Dynamic programming top-down solution
    int climbStairs(int n) {
        vector<int> cache;
        cache.resize(n, -1);
        return dfs(n, 0, cache);
    }

    int dfs(int n, int i, vector<int>& cache) {
        if (i == n) {
            return 1;
        }
        if (i > n) {
            return 0;
        }
        if (cache[i] != -1) {
            return cache[i];
        }

        cache[i] = dfs(n, i + 1, cache) + dfs(n, i + 2, cache);
        return cache[i];
    }
};
