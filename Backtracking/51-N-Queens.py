class Solution:
    def isValid(self, board, x, y, n):
        # if not interfering horizontally
        for i in range(n):
            if board[x][i] == 'Q':
                return False 
        # if not interfering vertically
            if board[i][y] == 'Q':
                return False 
        # if not interfering diagonally
            if x - i >= 0 and y - i >= 0:
                if board[x-i][y-i] == 'Q':
                    return False 
            
            if x + i < n and y + i < n:
                if board[x+i][y+i] == 'Q':
                    return False 
            

            if x - i >= 0 and y + i < n:
                if board[x-i][y+i] == 'Q':
                    return False 
            
            if x + i < n and y - i >= 0:
                if board[x+i][y-i] =='Q':
                    return False 

        return True 

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        #print(board)
        result = []

        def h(n, i):
            if i == n:
                result.append(["".join(row) for row in board])
                return 
            for j in range(n):
                if self.isValid(board,i,j,n):
                    board[i][j] = 'Q'
                    h(n, i + 1)
                    board[i][j] = '.'
        h(n,0)
        return result


# Note: Check for diagonally, both left diagonal and right diagonal
# should not interfere with each other

# Note: String is immutable, should use list