class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for x in prerequisites:
            graph[x[0]].append(x[1])

        visited  = set()
        def dfs(node):
            if node in visited:
                return False
            if not graph[node]:
                return True
            
            visited.add(node)
            
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            visited.remove(node)
            graph[node] = []
            
            return True
        
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

         


            