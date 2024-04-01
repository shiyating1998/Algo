#https://leetcode.cn/problems/search-insert-position/description/
'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            # mid = (left+right) // 2
            mid = (right-left) // 2 + left # prevent overflow
            t = nums[mid]
            if t == target:
                return mid
            elif t < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


nums = [1,3,5,6]
target = 7

nums = [1,3,5,6]
target = 2

nums = [1,3,5,6]
target = 5
s = Solution()
print(s.searchInsert(nums,target))


