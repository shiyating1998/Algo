from typing import List 

# Time complexity: O(mn), traverse the grid 
# Space complexity: O(1), no additional space

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        output = 0 

        # keep track of the size of the island 
        def dfs(i,j):            
            if i>=0 and i<row and j>=0 and j<col and grid[i][j]==1:
                grid[i][j] = 0            
                return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
            return 0 

        row = len(grid)
        col = len(grid[0])
        
        # traverse each cell to find the max 
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]==1:
                    output = max(output, dfs(i,j))                
        
        return output
        

