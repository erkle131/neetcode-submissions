class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int ROWS = grid.size(), COLS = grid[0].size();
        vector<vector<int>> visit(ROWS, vector<int>(COLS, 0));
        queue<pair<int, int>> queue;
        int fresh = 0;

        // Find entry points to grid
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 2) {
                    queue.push(pair<int, int>(r, c));
                    visit[r][c] = 1;
                }
                if (grid[r][c] == 1) fresh++;
            }
        }

        int minutes = 0;
        // run BFS from starting rotten oranges out to adjacent ones
        while (queue.size() && fresh > 0) {
            int queueLength = queue.size();
            for (int i = 0; i < queueLength; i++) {
                pair<int, int> curPair = queue.front();
                queue.pop();
                int r = curPair.first, c = curPair.second;

                int neighbors[4][2] = {
                              {r + 1, c},
                    {r, c - 1},         {r, c + 1},
                              {r - 1, c}
                };
                for (int j = 0; j < 4; j++) {
                    int newR = neighbors[j][0], newC = neighbors[j][1];
                    if (min(newR, newC) < 0 || newR == ROWS || newC == COLS ||
                        visit[newR][newC]) {
                            continue;
                    }
                    if (grid[newR][newC] == 1) {
                        queue.push(pair<int, int>(newR, newC));
                        visit[newR][newC] = 1;
                        fresh--;
                    }
                }
            }
            minutes++;
        }

        return fresh == 0 ? minutes : -1;
    }
};