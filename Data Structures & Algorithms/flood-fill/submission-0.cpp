class Solution {
private:
    int startColor;
    int targetColor;
    int ROWS, COLS;

public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        startColor = image[sr][sc];
        targetColor = color;

        if (startColor == targetColor) return image;

        ROWS = image.size();
        COLS = image[0].size();

        dfs(image, sr, sc);
        return image;
    }

    void dfs(vector<vector<int>>& image, int r, int c) {
        int ROWS = image.size(), COLS = image[0].size();
        if (min(r, c) < 0 || r == ROWS || c == COLS ||
            image[r][c] != startColor) {
                return;
        }

        image[r][c] = targetColor;
        dfs(image, r + 1, c);
        dfs(image, r - 1, c);
        dfs(image, r, c + 1);
        dfs(image, r, c - 1);
    }
};