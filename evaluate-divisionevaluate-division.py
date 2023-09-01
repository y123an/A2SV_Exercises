class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = collections.defaultdict(list)

        for i,equation in enumerate(equations):
            graph[equation[0]].append([equation[1],values[i]])
            graph[equation[1]].append([equation[0],1/values[i]])
        
        def dfs(src, target):
            if src not in graph or target not in graph:
                return -1

            stack =  []
            visited = set()
            stack.append([src,1])
            visited.add(src)
            while stack:
                node,w = stack.pop()
                if node == target:
                    return w
                for nei, value in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        stack.append([nei,w * value])
            
            return -1


        ans = []
        for query in queries:
            ans.append(dfs(query[0],query[1]))
        
        return ans
        
        