class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.sum_matrix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.sum_matrix[r][c + 1]
                self.sum_matrix[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottom_right = self.sum_matrix[row2][col2]
        above = self.sum_matrix[row1 - 1][col2]
        left = self.sum_matrix[row2][col1 - 1]
        top_left = self.sum_matrix[row1 - 1][col1 - 1]

        return bottom_right - above - left + top_left