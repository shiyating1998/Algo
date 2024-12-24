# https://leetcode.cn/problems/spiral-matrix-ii/description/

# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

# Example 1:
# 123
# 894
# 765
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

# Example 2:
# Input: n = 1
# Output: [[1]]
 

# Constraints:
# 1 <= n <= 20

from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        num = 1
        i,j = 0,0
        output = [[0]*n for _ in range(n)]
        print(output)

        while n > 1:
            for _ in range(n-1):
                output[i][j] = num
                num += 1
                j += 1
            for _ in range(n-1):
                output[i][j] = num
                num += 1
                i += 1
            for _ in range(n-1):
                output[i][j] = num
                num += 1
                j -= 1
            for _ in range(n-1):
                output[i][j] = num
                num += 1
                i -= 1
            n -= 2
            i += 1
            j += 1

        if n == 1:
            output[i][j] = num
        return output
# Example 1:
# 123
# 894
# 765
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

print(Solution().generateMatrix(3))

# Example 2:
# Input: n = 1
# Output: [[1]]
print   (Solution().generateMatrix(1))
print   (Solution().generateMatrix(6))

print   (Solution().generateMatrix(5))
