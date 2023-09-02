class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        nrow, ncol = len(board), len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1],[-1,-1],[1,1],[1,-1],[-1,1]]
        
        def numMine(r,c):
            counter = 0
            for dr, dc in directions:
                row, col = r+dr,c+dc
                if row in range(nrow) and col in range(ncol) and board[row][col] == "M":
                    counter += 1
            
            return counter
       
        def dfs(r,c):
            if board[r][c] != "E":
                return  
            
            if numMine(r,c) > 0:
                board[r][c] = str(numMine(r,c))
                return 
            else:
                board[r][c] = "B"
                for dr, dc in directions:
                    row, col = r+dr,c+dc
                    if row in range(nrow) and col in range(ncol):
                        dfs(row,col)
            
        r, c = click
             
        if board[r][c] == "M":
            board[r][c] = "X"
            return board
        else:
            dfs(r,c)
            print(board)
        

        return board
        