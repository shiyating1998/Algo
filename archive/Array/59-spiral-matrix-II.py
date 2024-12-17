'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 https://leetcode.cn/problems/spiral-matrix-ii/description/
'''
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output = [[0] * n for _ in range(n)]


        loop = n//2
        mid = n//2

        startx = 0
        starty = 0

        num = 1
        for offset in range(1, loop + 1):
            # top row
            for j in range(startx, n - offset):
                output[startx][j] = num
                num += 1
            # rightmost col
            for i in range(starty, n - offset):
                output[i][n - offset] = num
                num += 1
            # bottom row
            for j in range(n - offset, startx, -1):
                output[n - offset][j] = num
                num += 1
            # leftmost col
            for i in range(n - offset, starty, -1):
                output[i][starty] = num
                num += 1

            startx += 1
            starty += 1

        if n % 2 != 0:
            output[mid][mid] = num

        return output


s = Solution()
print(s.generateMatrix(5))

# 总是写不对，需要二刷