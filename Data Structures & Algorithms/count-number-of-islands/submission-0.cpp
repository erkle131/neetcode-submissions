class Solution {
private:
    vector<vector<int>> visit;
    int ROWS, COLS;

public:
    int numIslands(vector<vector<char>>& grid) {
        ROWS = grid.size();
        COLS = grid[0].size();
        visit.assign(ROWS, vector<int>(COLS, 0));

        int num_islands = 0;
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == '1' && !visit[r][c]) {
                    num_islands++;
                    dfs(grid, r, c, visit);
                }
            }
        }
        return num_islands;
    }

    void dfs(vector<vector<char>>& grid, int r, int c, vector<vector<int>>& visit) {
        if (min(r, c) < 0 || r == ROWS || c == COLS ||
            grid[r][c] == '0' || visit[r][c] == 1) {
                return;
        }

        visit[r][c] = 1;
        dfs(grid, r + 1, c, visit);
        dfs(grid, r - 1, c, visit);
        dfs(grid, r, c + 1, visit);
        dfs(grid, r, c - 1, visit);
    }
};