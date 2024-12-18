# https://leetcode.cn/problems/valid-perfect-square/description/

# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

# Example 1:
# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

# Example 2:
# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
 

# Constraints:

# 1 <= num <= 231 - 1

# Author: Jennifer Shi
# Date: 12/18/2024
# Input: positive integer num
# Expected Output: boolean
# Analysis:
    # Solution 1: perform a binary search between 0 and num  
    # if mid * mid == num:
    #     return True

from ast import Num


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == num:
                return True 
            elif mid * mid > num:
                high = mid - 1 
            else:
                low = mid + 1
        return False

# Example 1:
# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
assert Solution().isPerfectSquare(16) == True

# Example 2:
# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
assert Solution().isPerfectSquare(14) == False

assert Solution().isPerfectSquare(1) == True

assert Solution().isPerfectSquare(2) == False