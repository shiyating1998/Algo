# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

from typing import List

class Solution1:
    def binarySearch(self, low, high, target, nums):
        while (low <= high):
            mid = (low + high) // 2
            if (nums[mid]==target):
                return mid 
            elif (nums[mid] > target):
                high = mid - 1 
            else:
                low = mid + 1 
        return -1 

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Solution 1: find the target value and then do a linear search?
        # Solution 2: find the target value and then continue doing binary search till no more found?
        low = 0 
        right = len(nums) - 1 

        result = [-1, -1]
        output = self.binarySearch(low, right, target, nums)
        if (output == -1):
            return result 
        else:
            result = [output, output]
            left_bound = output - 1 
            right_bound = output + 1 
            while (left_bound != -1):
                left_bound = self.binarySearch(low, left_bound, target,nums)
                if (left_bound != -1):
                    result[0] = left_bound 
                    left_bound -= 1 
            while (right_bound != -1):
                right_bound = self.binarySearch(right_bound, right, target,nums) 
                if (right_bound != -1):
                    result[1] = right_bound 
                    right_bound += 1 
        return result 


# interesting solution, find target + 0.5 and find target - 0.5

# Issue with my approach, repeated binary search
# Refined Approach:
# Perform binary search twice:
# Left Binary Search: Locate the leftmost (starting) index of the target.
# Right Binary Search: Locate the rightmost (ending) index of the target.
# If the target is not found during either search, return [-1, -1].


# Analysis: First find the leftbound, then find the rightbound

class Solution2:
    def binarySearch(self, target, nums):
        low = 0
        high = len(nums) - 1
        while (low <= high):
            mid = (low + high) // 2
            if (nums[mid]==target):
                return mid 
            elif (nums[mid] > target):
                high = mid - 1 
            else:
                low = mid + 1 
        return -1 

    def find_left_bound(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def find_right_bound(self,nums,target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(target, nums)
        if left == -1:
            return [-1, -1]
        left_bound = self.find_left_bound(nums, target)
        right_bound = self.find_right_bound(nums, target)
        return [left_bound, right_bound]
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
nums = [5,7,7,8,8,10]
target = 8
s = Solution2()
assert s.searchRange(nums,target) == [3,4]

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
nums = [5,7,7,8,8,10]
target = 6
s = Solution2()
assert s.searchRange(nums,target) == [-1,-1]    

# Input: nums = [], target = 0
# Output: [-1,-1]

nums = []
target = 0
s = Solution2()
assert s.searchRange(nums,target) == [-1,-1]