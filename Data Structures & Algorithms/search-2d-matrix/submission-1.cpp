class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // Determine which row target may be in
        int searchRowIdx = -1;
        for (int i = 0; i < matrix.size(); i++) {
            if (target >= matrix[i][0]) {
                searchRowIdx = i;
            }
        }

        if (searchRowIdx == -1) return false;

        // Perform binary search on row for target
        int L = 0, R = matrix[searchRowIdx].size() - 1;

        while (L <= R) {
            int mid = L + (R - L) / 2;

            if (target > matrix[searchRowIdx][mid]) {
                L = mid + 1;
            } else if (target < matrix[searchRowIdx][mid]) {
                R = mid - 1;
            } else {
                return true;
            }
        }

        return false;
    }
};
