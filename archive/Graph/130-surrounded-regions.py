# https://leetcode.com/problems/surrounded-regions/description/

class UnionFind:

    def __init__(self, n):
        self.count = n         # number of connected components 
        self.parent = [0] * n  # parent[x] is the parent node of x 
        for i in range(n):
            self.parent[i] = i
    

    # Important!!! The time complexity of the UNIONFIND algorithm depends on this!
    # since both connected and union depend on find()
    # some very delicate method of flatten the graph, can check article[1] to 
    # learn more 

    # find the root of x recursively
    # while flattening the graph 
    # averages out to be O(1)
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # union two nodes, connect them by joining them with the same root
    # O(1)
    def union(self,p,q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp!=rootq:
            self.parent[rootp] = rootq
            self.count -= 1
    
    # check if two nodes are connected by checking if they have the same root
    # O(1) since the graph is flat 
    def connected(self,p,q):
        return self.find(p)==self.find(q)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(r,c):
            if r>=0 and r<row and c>=0 and c<col:
                board[r][c] = '#'
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)

        row = len(board)
        col = len(board[0])

        uf = UnionFind(row*col)+1)

        for i in range(row):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][col-1] =='O':
                dfs(i, col-1)
        
        for j in range(col):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[row-1][j] == 'O':
                dfs(row-i, j)




    