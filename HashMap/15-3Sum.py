
# https://leetcode.cn/problems/3sum/description/
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 


 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue 
            if nums[i] > 0:
                break 
            for j in range(i + 1, len(nums)):
                if j != i + 1 and nums[j] == nums[j-1]:
                    continue 
                for z in range(j + 1, len(nums)):
                    if z != j + 1 and nums[z] == nums[z-1]:
                        continue 
                    if nums[i] + nums[j] + nums[z] == 0:
                        output.append([nums[i],nums[j],nums[z]])

        return output

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
print(Solution().threeSum(nums = [-1,0,1,2,-1,-4]))
assert Solution().threeSum(nums = [-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
assert Solution().threeSum(nums = [0,1,1]) == []
# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
assert Solution().threeSum(nums = [0,0,0]) == [[0,0,0]]

nums = [0,0,0,0]
assert  Solution().threeSum(nums = nums) == [[0,0,0]]

# Note: 一开始找双数之和，学会了去重。想要简化三数之和为两数之和，用哈希，但是写着写着发现不对，因为应该z>j>i。
# 后来3循环找三数之和，依靠sorted array去重。
# Time complexity: O(nlogn) for sorting, O(n^2) for looping
# Space complexity: O(1) for output



class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        #print(nums)
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue 
            if nums[i] > 0:
                break 
            
            j = i + 1 
            z = len(nums) - 1 
            while j < z:
                if j != i + 1 and nums[j] == nums[j-1]:
                    j += 1 
                    continue 
                if z != len(nums) - 1 and nums[z] == nums[z+1]:
                    z -= 1 
                    continue 
                s = nums[i] + nums[j] + nums[z]

                if s > 0:
                    z -= 1 
                if s < 0:
                    j += 1 
                if s == 0:
                    output.append([nums[i],nums[j],nums[z]])
                    j += 1 
                    z -= 1

        return output

# Note: 前一种方法三循环超时了，双指针法收敛，会快了很多…