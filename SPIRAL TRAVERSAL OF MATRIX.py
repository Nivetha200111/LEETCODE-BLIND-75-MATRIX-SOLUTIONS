class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n-1, 0, m-1
        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            for i in range(top + 1, bottom + 1):
                result.append(matrix[i][right])
            if top != bottom:
                for j in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom][j])
            if left != right:
                for i in range(bottom - 1, top, -1):
                    result.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return result
