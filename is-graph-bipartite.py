class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)

        def dfs(i):
            if color[i]:
                return True

            stack = [i]

            color[i] = 1
            
            while stack:
                i = stack.pop()
                for nei in graph[i]:
                    if color[i] == color[nei]:
                        return False
                    elif not color[nei]:
                        stack.append(nei)
                        if color[i] == 2:
                            color[nei] = color[i] - 1
                        elif color[i] == 1:
                            color[nei] = color[i] + 1
            
            return True


        for i in range(len(graph)):
            if not dfs(i):
                return False
            

        return True