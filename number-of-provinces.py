class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        nrow, ncol = len(isConnected), len(isConnected[0])

        for r in range(nrow):
            for c in range(ncol):
                if isConnected[r][c] == 1:
                    graph[r].append(c)
        
        visited = set()
        count = 0

        def dfs(node):
            visited.add(node)
            for x in graph[node]:
                if x not in visited:
                    dfs(x)
            

        for x in graph:
            if x not in visited:
                dfs(x)
                count += 1
            
        return count

