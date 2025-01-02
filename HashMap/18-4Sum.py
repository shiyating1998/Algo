# https://leetcode.cn/problems/4sum/description/

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 
# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 
# Constraints:

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):            
            if i != 0 and nums[i] == nums[i-1]:
                continue 
            for j in range(i + 1, len(nums)):
                if j != i + 1 and nums[j] == nums[j-1]:
                    continue 
                
                l = j + 1 
                r = len(nums) - 1
                while l < r:
                    if l != j + 1 and nums[l] == nums[l-1]:
                        l += 1 
                        continue 
                    if r != len(nums) - 1 and nums[r] == nums[r+1]:
                        r -= 1 
                        continue
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s > target:
                        r -= 1 
                    elif s < target:
                        l += 1 
                    elif s == target:
                        output.append([nums[i],nums[j], nums[l],nums[r]])
                        l += 1 
                        r -= 1 
                        
        return output 

#Note: we are looking for target, in which target could be any number. Therefore, we couldn't break early. As 3 sum where we are looking to add up to 0.