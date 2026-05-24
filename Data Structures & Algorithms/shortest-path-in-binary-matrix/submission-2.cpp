class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int ROWS = grid.size(), COLS = grid[0].size();
        if (grid[0][0] == 1 || grid[ROWS - 1][COLS - 1] == 1) {
            return -1;
        } 
        vector<vector<int>> visit(ROWS, vector<int>(COLS, 0));
        queue<pair<int, int>> queue;
        queue.push(pair<int, int>(0, 0));
        visit[0][0] = 1;

        int length = 1;
        while (queue.size()) {
            int queueLength = queue.size();
            for (int i = 0; i < queueLength; i++) {
                pair<int, int> curPair = queue.front();
                queue.pop();
                int r = curPair.first, c = curPair.second;
                if (r == ROWS - 1 && c == COLS - 1) {
                    return length;
                }

                int neighbors[8][2] = {
                    {r - 1, c - 1}, {r - 1, c}, {r - 1, c + 1},
                    {r, c - 1},                 {r, c + 1},
                    {r + 1, c - 1}, {r + 1, c}, {r + 1, c + 1}
                };
                for (int j = 0; j < 8; j++) {
                    int newR = neighbors[j][0], newC = neighbors[j][1];
                    if (min(newR, newC) < 0 || newR == ROWS || newC == COLS ||
                        visit[newR][newC] || grid[newR][newC]) {
                            continue;
                    }
                    queue.push(pair<int, int>(newR, newC));
                    visit[newR][newC] = 1;
                }
            }
            length++;
        }
        return -1;
    }
};