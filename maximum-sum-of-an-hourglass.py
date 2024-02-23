# time complexity = O(n*m)
# space compleixty = O(1)

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        ans = 0

        # itrating through the matrix in the row wise
        for idx_col in range(m):
            for idx_row in range(n):
                
                # checkin the eadge cases to not get index out of bound
                if idx_col > 0  and idx_col < m-1 and idx_row < n-2:

                    top_row = grid[idx_row][idx_col-1] + grid[idx_row][idx_col] + grid[idx_row][idx_col + 1]
                    middle = grid[idx_row+1][idx_col]              
                    bottom_row = grid[idx_row+2][idx_col-1] + grid[idx_row+2][idx_col] + grid[idx_row+2][idx_col + 1]

                    ans = max(ans, top_row + middle + bottom_row)

        return ans

        