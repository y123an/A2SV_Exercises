class Solution:

    def inBound(self, row: int, col: int, grid: List[List[int]]) -> bool:

        if row < 0 or row >= len(grid):
            return False

        if col < 0 or col >= len(grid[0]):
            return False

        return True



    def getNeighbors(self, row: int, col: int, grid: List[List[str]]) -> List[Tuple[int]]:

        nbrs = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x, y in directions:
            new_row, new_col = row+x, col+y
            if self.inBound(new_row, new_col, grid) and grid[row][col] == grid[new_row][new_col]:
                nbrs.append((new_row, new_col))

        return nbrs


    def hasCycle(self, row: int, col: int, last_cell: Tuple[int], grid: List[List[str]], color: List[List[int]]) -> bool:

        if color[row][col] == 1:
            return True

        if color[row][col] == 2:
            return False

        color[row][col] = 1
        for nbr_row, nbr_col in self.getNeighbors(row, col, grid):
            if (nbr_row, nbr_col) == last_cell:
                continue
            if self.hasCycle(nbr_row, nbr_col, (row, col), grid, color):
                return True

        color[row][col] = 2
        return False


    # O(v + e) time, 
    # O(v) space,
    def containsCycle(self, grid: List[List[str]]) -> bool:
        '''
            0: neutral, 1: open, 2: closed
        '''
        n, m = len(grid), len(grid[0])
        color = [[0 for _ in range(m)] for _ in range(n)]

        for row in range(n):
            for col in range(m):
                if color[row][col] == 0:
                    if self.hasCycle(row, col, (-1, -1), grid, color):
                        return True

        return False
