class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # define dp[i][j] to be the min amt of money you need to win
        # from numbers i to j

        # initialize to inf

        # then, when i==j, the cost is 0
        # when j-i=1, the cost is i
        # when j-i=2, the cost is j-1
        # o.w the cost is the min cost of all possible 
        # ways to select the k as the root (where k is between (i,j))
        # for all k in between i to j:
        # dp[i][j] = min(dp[i][j], max(dp[i][k-1] + k, k + dp[k+1][j]))

        # the min amt of money you need to win from 1 to n is dp[1][n]


        dp = [[float('inf')]*(n+1) for _ in range(n+1)]

        for j in range(1, n+1):
            # since we require dp[k+1][j] to build dp[i][j], (where i<k)
            # we need to build it from bottom up 
            for i in range(j, 0, -1):
                # print("i: ",i," j:",j)
                if i == j:
                    dp[i][j] = 0
                    continue
                if j - i == 1:
                    dp[i][j] = i 
                    continue
                if j - i == 2:
                    dp[i][j] = j - 1 
                    continue
              
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], max(dp[i][k-1] + k, k + dp[k+1][j]))

        #for row in dp:
            #print(row)
        return dp[1][n]


sol = Solution()
print(sol.getMoneyAmount(1))
print(sol.getMoneyAmount(2))
print(sol.getMoneyAmount(10))
print(sol.getMoneyAmount(5))


