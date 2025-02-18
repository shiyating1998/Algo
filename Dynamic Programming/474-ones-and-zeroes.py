class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        #output = 0
        for string in strs:
            ones = string.count("1")
            zeros = string.count("0")
            for i in range(m, zeros -1, -1):
                for j in range(n, ones-1, -1):
                    
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
                        #output = max(output,dp[i][j])
        return dp[-1][-1]