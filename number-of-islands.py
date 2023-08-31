class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        nrow, ncol = len(grid),len(grid[0])

        visited = set()
        island = 0

        def dfs(r,c):
            stack = []
            visited.add((r,c))
            stack.append((r,c))

            while stack:
                row, col = stack.pop()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]

                for dr,dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(nrow) and c in range(ncol) and (r,c) not in visited and grid[r][c] == "1"):
                        stack.append((r,c))
                        visited.add((r,c))
            

        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    island += 1
        
        return island
