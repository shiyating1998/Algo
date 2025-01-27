

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Precompute hash sets for rows, columns, and subgrids
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrids = [set() for _ in range(9)]

        # Fill hash sets with initial board values
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    subgrids[(i // 3) * 3 + (j // 3)].add(num)

        def backtrack(x, y):
            if x == 9:  # Completed the board
                return True

            next_x, next_y = (x + (y + 1) // 9), (y + 1) % 9

            if board[x][y] != ".":
                return backtrack(next_x, next_y)

            for num in map(str, range(1, 10)):
                subgrid_idx = (x // 3) * 3 + (y // 3)
                if num not in rows[x] and num not in cols[y] and num not in subgrids[subgrid_idx]:
                    # Place the number
                    board[x][y] = num
                    rows[x].add(num)
                    cols[y].add(num)
                    subgrids[subgrid_idx].add(num)

                    # Recur to the next cell
                    if backtrack(next_x, next_y):
                        return True

                    # Undo the placement
                    board[x][y] = "."
                    rows[x].remove(num)
                    cols[y].remove(num)
                    subgrids[subgrid_idx].remove(num)

            return False

        backtrack(0, 0)


class Solution2:

    def isValid(self, board, x, y, num):
        num = str(num)
        # Check horizontally
        for i in range(9):
            if board[x][i] == num:
                return False

        # Check vertically
        for i in range(9):
            if board[i][y] == num:
                return False

        # Check 3x3 subgrid
        subgrid_x = (x // 3) * 3
        subgrid_y = (y // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[subgrid_x + i][subgrid_y + j] == num:
                    return False

        return True


    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def h(board, x, y):
            if x == 9 and y == 0:
                return True 

            next_y = y + 1
            next_x = x 
            if next_y == 9:
                next_x += 1 
                next_y = 0

            if board[x][y] != '.':                
                return h(board, next_x, next_y)

            else:
                for i in range(1, 10):
                    if self.isValid(board,x,y,i):
                        #print(x, y, i)
                        board[x][y] = str(i)
                        if h(board, next_x, next_y):
                            return True                         
                        board[x][y] = "."
            return False
        h(board,0,0)
        return board