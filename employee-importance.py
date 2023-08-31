"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        emap = {e.id:e for e in employees}


        def dfs(emp):
            ans = emap[emp].importance

            for x in emap[emp].subordinates:
                ans += dfs(x)
            
            return ans

            
        return dfs(id)
       
