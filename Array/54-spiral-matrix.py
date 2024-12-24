# Given an m x n matrix, return all elements of the matrix in spiral order.

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix[0])
        n = len(matrix)
        output = [0]*(m*n)

        i,j = 0,0
        c = 0

        while m > 1 and n > 1:
            for _ in range(m-1):
                output[c] = matrix[i][j]
                c += 1
                j += 1
            for _ in range(n-1):
                output[c] = matrix[i][j]
                c += 1
                i += 1
            for _ in range(m-1):
                output[c] = matrix[i][j]
                c += 1
                j -= 1
            for _ in range(n-1):
                output[c] = matrix[i][j]
                c += 1
                i -= 1

            m -= 2
            n -= 2
            i += 1
            j += 1

        if m == 1:
            for _ in range(n):
                output[c] = matrix[i][j]
                c += 1
                i += 1
        elif n == 1:
            for _ in range(m):
                output[c] = matrix[i][j]
                c += 1
                j += 1

        return output

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

print(Solution().spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
print(Solution().spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))