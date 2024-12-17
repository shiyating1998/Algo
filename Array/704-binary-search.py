# https://leetcode.com/problems/binary-search/description/

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.


# Author: Jennifer Shi
# Date: 12/17/2024
# Analysis:
# Input: (int) Sorted array - unique value,  (int)target value
# Expected output: (int) index of target value or -1 if not found
# Solution 1: Brute force, O(n)
# Solution 2: Binary search, O(logn)
# Time complexity: O(logn)
# Space complexity: O(1), no additional space needed    
# Key Takeaways: 
    # The loop invariant is that the interval is [low, high] in our case, inclusive on both ends
    # if the loop invariant is [low, high), not inclusive on high, then the condition and variable update is different
      

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums) - 1
        while (low <= high):
            mid = (low+high)//2
            if (nums[mid] == target):
                return mid 
            elif (nums[mid] > target):
                high = mid - 1
            else:
                low = mid + 1
        return -1 


# Test case 1
# Expected output: 4
nums = [-1,0,3,5,9,12]
target = 9
t1 = Solution()
assert t1.search(nums,target) == 4

# Test case 2
# Expected output: -1
nums = [-1,0,3,5,9,12]
target = 2  
t2 = Solution()
assert t2.search(nums,target) == -1

# Test case 3 - array length of 1, not found
# Expected output: -1
nums = [1]
target = 2 
t3 = Solution()
assert t3.search(nums,target) == -1

# Test case 4 - array leng of 1, found 
nums = [1]
target = 1
t4 = Solution()
assert t4.search(nums,target) == 0 