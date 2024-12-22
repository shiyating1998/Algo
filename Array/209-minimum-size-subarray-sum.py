# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
# whose sum is greater than or equal to target. If there is no such subarray, return 0 instead. 

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104


# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        output = len(nums)
        s = sum(nums)
        if s >= target:
            i = 0
            j = 0
            s = 0
            while j < len(nums):
                s += nums[j]
                while s >= target:
                    output = min(output, j - i + 1)
                    s -= nums[i]
                    i += 1                    
                j += 1
            return output
        else:
            return 0

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

assert Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]) == 2

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1
assert Solution().minSubArrayLen(target=4, nums=[1, 4, 4]) == 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
assert Solution().minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]) == 0

target = 2 
nums = [1, 1, 1, 1, 1, 1, 1, 1]
assert Solution().minSubArrayLen(target=target, nums=nums) == 2

target = 2 
nums = [1, 2, 1, 1, 1, 1, 1, 1]
assert Solution().minSubArrayLen(target=target, nums=nums) == 1

target = 2 
nums = [2]
assert Solution().minSubArrayLen(target=target, nums=nums) == 1


# Note: detail on variable updates, the order is important
# sliding window, however, it didn't miss any of the possible subarrays