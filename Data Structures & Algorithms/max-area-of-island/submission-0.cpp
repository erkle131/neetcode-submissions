class Solution {
private:
    vector<vector<int>> visit;
    int ROWS, COLS;
    
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        ROWS = grid.size();
        COLS = grid[0].size();
        visit.assign(ROWS, vector<int>(COLS, 0));

        int cur_max = 0;
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                cur_max = max(cur_max, dfs(grid, r, c, visit));
            }
        }
        return cur_max;
    }

    int dfs(vector<vector<int>>& grid, int r, int c, vector<vector<int>>& visit) {
        if (min(r, c) < 0 || r == ROWS || c == COLS ||
            visit[r][c] || grid[r][c] == 0) {
                return 0;
        }
        
        visit[r][c] = 1;
        int area = 1;
        area += dfs(grid, r + 1, c, visit);
        area += dfs(grid, r - 1, c, visit);
        area += dfs(grid, r, c + 1, visit);
        area += dfs(grid, r, c - 1, visit);
        return area;
    }
};