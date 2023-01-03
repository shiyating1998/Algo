# question: https://leetcode.com/problems/maximum-product-subarray/description/

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # define dp[i][0] to be the maxProduct subarray of nums[0:i+1] that contains nums[i]
        # define dp[i][1] to be the maxProduct subarray of nums[0:i+1] that contains nums[i]
        # then, dp[i+1][0] = max(nums[i+1]*dp[i][0], nums[i+1]*dp[i][1], nums[i+1])


        dp = [[0,0] for _ in range(len(nums))]

        dp[0][0] = nums[0]
        dp[0][1] = nums[0]

        output = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(nums[i]*dp[i-1][0], nums[i]*dp[i-1][1], nums[i])
            dp[i][1] = min(nums[i]*dp[i-1][0], nums[i]*dp[i-1][1], nums[i])
            output = max(output, dp[i][0])

        return output


s = Solution()
print(s.maxProduct([2,3,-2,4]))
print(s.maxProduct([-2,0,-1]))
print(s.maxProduct([2,3,-2,-4]))