# https://leetcode.cn/problems/binary-search/description/
'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1


提示：

你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = (left + right ) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1

        return -1

nums = [-1,0,3,5,9,12]
target = 9

nums = []
target = 2

nums = [2]
target = 2

nums = [2,4,6]
target = 2

s = Solution()
print(s.search(nums,target))

# Time complexity: O(logn)
# Space complexity: O(1), no additional space needed
# 一次过，不错
# 2024/3/30

#重点是定义区间