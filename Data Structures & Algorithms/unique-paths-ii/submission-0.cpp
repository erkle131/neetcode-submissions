class Solution {
    int ROWS, COLS;
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        ROWS = obstacleGrid.size();
        COLS = obstacleGrid[0].size();
        vector<vector<int>> cache(ROWS, vector<int>(COLS, 0));
        return dfs(obstacleGrid, 0, 0, cache);
    }

    int dfs(vector<vector<int>>& obstacleGrid, int r, int c, vector<vector<int>>& cache) {
        if (r == ROWS || c == COLS) {
            return 0;
        }
        if (obstacleGrid[r][c]) { // Hit an obstacle (1)
            return 0;
        }
        if (cache[r][c] > 0) {
            return cache[r][c];
        }
        if (r == ROWS - 1 && c == COLS - 1) {
            return 1;
        }

        cache[r][c] = dfs(obstacleGrid, r + 1, c, cache) +
                      dfs(obstacleGrid, r, c + 1, cache);
        return cache[r][c];
    }
};