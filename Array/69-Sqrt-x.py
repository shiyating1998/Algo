# https://leetcode.cn/problems/sqrtx/description/
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

# Constraints:

# 0 <= x <= 231 - 1

# Author: Jennifer Shi
# Date: 12/18/2024
# Input: non-negative integer x
# Expected Output: non-negative integer
# Analysis:
    # Solution 1: perform a binary search between 0 and x  
    # if mid * mid == x:
    #     return mid
    # elif mid * mid > x:
    #     right = mid - 1
    # else:
    #     left = mid + 1    
# time complexity: O(logn)
# space complexity: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0 
        high = x 
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid 
            elif mid * mid > x:
                high = mid - 1 
            else:
                low = mid + 1 
        return high # return high instead of low since we round down 

# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
x = 4
assert Solution().mySqrt(x) == 2

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
x = 8
assert Solution().mySqrt(x) == 2