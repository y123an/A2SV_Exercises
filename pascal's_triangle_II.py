# time complexity of O(K^2)
# space complexity of O(k)

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]

        for i in range(1,rowIndex + 1):
            ans.append(1)
            for j in range(len(ans)-2,0,-1):
                ans[j] += ans[j-1]
        return ans
           