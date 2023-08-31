class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if (r<0 or r == nrow or c < 0 or c == ncol or grid[r][c] == 0 or (r,c) in visited):
                return 0

            visited.add((r,c))

            return 1 + (dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
            

        maxi = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxi = max(maxi,dfs(r,c))

        return maxi