class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()

        for i in range(len(intervals)):
            if not ans:
                ans.append(intervals[i])
            else:
                x = ans[-1]

                if x[1] >= intervals[i][0]:
                    ans[-1][1] = max(x[1],intervals[i][1])
                else:
                    ans.append(intervals[i])
        
        return ans