class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)

        dp[0] = 1 
        dp[1] = 1 

        for i in range(2, n + 1):
            for j in range(0, i):
                dp[i] += dp[i - j - 1] * dp[j]

        # print(dp)
        return dp[-1]

# 推导条件不是很好找，主要是以有多少个可能的头节点来算。