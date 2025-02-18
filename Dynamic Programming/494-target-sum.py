class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = (sum(nums) + target) // 2 
        if sum(nums) < abs(target):
            return 0
        if (sum(nums) + target) % 2 != 0:
            return 0 
        dp = [0] * (s+1)
        dp[0] = 1 

        for num in nums:
            for j in range(s, num - 1, -1): 
                dp[j] = dp[j] + dp[j - num]
        # print(dp)
        return dp[-1]
        
        