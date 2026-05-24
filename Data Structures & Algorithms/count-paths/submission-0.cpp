class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> cache(m, vector<int>(n, 0));
        return dfs(0, 0, m, n, cache);
    }

    int dfs(int r, int c, int rows, int columns, vector<vector<int>>& cache) {
        if (r == rows || c == columns) {
            return 0;
        }
        if (cache[r][c] > 0) {
            return cache[r][c];
        }
        if (r == rows - 1 && c == columns - 1) {
            return 1;
        }

        cache[r][c] = dfs(r + 1, c, rows, columns, cache) +
                      dfs(r, c + 1, rows, columns, cache);
        return cache[r][c];
    }
};
