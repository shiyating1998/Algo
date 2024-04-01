'''
https://leetcode.cn/problems/move-zeroes/description/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        read = 0
        write = 0
        while read < len(nums):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
            read += 1
        while write < len(nums):
            nums[write] = 0
            write += 1

s = Solution()
nums = [0,1,0,3,12]
nums = [0]
nums = [0,0,0,0]
s.moveZeroes(nums)
print(nums)