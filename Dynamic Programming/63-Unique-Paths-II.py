class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [ [0]*n for _ in range(m)]
        
        # init first row
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1 
        
        # init first col
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break 
            dp[i][0] = 1 
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]

        